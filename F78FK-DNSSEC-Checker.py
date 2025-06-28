#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
F78FK-DNSSEC Validator - Diagnoses whether your network DNS fully
supports DNSSEC security extensions
Copyright (C) 2025  Liu Yu <f78fk@live.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

===========================================================================
F78FK-DNSSEC 验证工具 - 用于诊断网络 DNS 是否完整支持 DNSSEC 安全扩展标准
版权所有 (C) 2025  Liu Yu <f78fk@live.com>

本程序是自由软件：您可以根据自由软件基金会发布的 GNU 通用公共许可证第 3 版，
或（由您自行选择）任何更高版本的条款，自由地修改和分发本程序。

本程序基于使用目的分发，但没有任何担保；包括适销性或特定用途适用性担保。
详细条款请参阅GNU通用公共许可证。

您应已随本程序收到GNU通用公共许可证的副本。如果没有, 请参阅:
<https://www.gnu.org/licenses/>
"""

__version__ = "1.0.3"
__author__ = "Liu Yu"
__license__ = "GPLv3"

PORT = 11111
HOST = "127.0.0.1"

import asyncio
import websockets
import json
import subprocess
import traceback
import re
import sys
import os
import platform
import shutil
import signal


IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    DIG_PATH = "dig.exe"
else:
    DIG_PATH = shutil.which("dig")


def run_dig(args):
    try:
        clean_env = os.environ.copy()
        clean_env.pop("LD_LIBRARY_PATH", None)

        completed = subprocess.run(
            [DIG_PATH] + args, capture_output=True, text=True, timeout=8, env=clean_env
        )
        if completed.returncode != 0:
            return None, completed.stderr.strip()
        return completed.stdout, None
    except Exception as e:
        return None, str(e)


def parse_dig_output(output):
    ad_flag = False
    rcode = "UNKNOWN"

    header_line = None
    flags_line = None

    for line in output.splitlines():
        if line.startswith(";; ->>HEADER<<-"):
            header_line = line
        elif line.startswith(";; flags:"):
            flags_line = line

    if header_line:
        m = re.search(r"status: (\w+)", header_line)
        if m:
            rcode = m.group(1)

    if flags_line:

        m = re.search(r"flags: ([\w\s]+);", flags_line)
        if m:
            flags = m.group(1).lower().split()
            ad_flag = "ad" in flags

    return ad_flag, rcode


def query_domain(domain, dig_args):
    debug = {"domain": domain, "command": " ".join([DIG_PATH] + dig_args)}

    output, error = run_dig(dig_args)
    debug["output"] = output
    debug["error"] = error

    if error:
        print(f"[ERROR] Query failed for {domain}: {error}")
        return {"ad": False, "status": "ERROR", "debug": debug, "error": error}

    ad_flag, status = parse_dig_output(output)
    debug["ad_flag"] = ad_flag
    debug["status"] = status

    return {"ad": ad_flag, "status": status, "debug": debug, "error": None}


def determine_result(nic, failed):
    """
    Determine DNSSEC validation result based on dig output of nic.cz and dnssec-failed.org.

    Parameters:
        nic (dict): Result of querying nic.cz (a DNSSEC-valid domain).
        failed (dict): Result of querying dnssec-failed.org (intentionally broken DNSSEC domain).

    Returns:
        dict: {
            "result": "secure" | "medium" | "insecure" | "unknown" | "tool-error",
            "logs": [str],
            "nic": dict,
            "failed": dict,
            "error": str or None
        }
    """
    logs = []
    logs.append(f"Parsed nic.cz: AD={nic['ad']}, Status={nic['status']}")
    logs.append(
        f"Parsed dnssec-failed.org: AD={failed['ad']}, Status={failed['status']}"
    )

    # Helper to generate consistent return result
    def make_result(result, message=None):
        if message:
            logs.append(message)
        return {
            "result": result,
            "logs": logs,
            "nic": nic,
            "failed": failed,
            "error": (
                nic["error"] or failed["error"] if result == "tool-error" else None
            ),
        }

    # If dig failed for any domain (tool or subprocess error)
    if nic["error"] or failed["error"]:
        return make_result("tool-error")

    # If dig output is missing
    if not nic["debug"].get("output") or not failed["debug"].get("output"):
        return make_result("unknown", "Missing dig output — possible network issue.")

    # If either result is a refused or malformed response
    refused_states = {"REFUSED", "FORMERR", "NOTIMP"}
    if nic["status"] in refused_states or failed["status"] in refused_states:
        return make_result(
            "unknown",
            f"Unknown state due to refused/formerr/notimp status: nic={nic['status']}, failed={failed['status']}",
        )

    # If dnssec-failed.org resolves successfully, DNSSEC is not enforced
    if failed["status"] == "NOERROR":
        return make_result("insecure", "dnssec-failed.org: NOERROR.")

    # If nic.cz could not be resolved successfully, no DNSSEC conclusion possible
    if nic["status"] != "NOERROR":
        return make_result(
            "unknown",
            f"Unknown: nic.cz could not be resolved (status: {nic['status']}).",
        )

    # Now both statuses are OK — begin DNSSEC validation check
    if nic["ad"] and not failed["ad"] and failed["status"] == "SERVFAIL":
        return make_result(
            "secure", "Secure: local resolver validates DNSSEC correctly."
        )

    elif not nic["ad"] and failed["status"] == "SERVFAIL":
        return make_result(
            "medium", "Medium: local resolver does not validate, but upstream does."
        )

    elif failed["status"] != "SERVFAIL":
        return make_result(
            "insecure", "Insecure: failed domain resolved without SERVFAIL."
        )

    # If none of the above match, return unknown
    return make_result("unknown", "Unknown state: unable to determine DNSSEC status.")


def setup_signal_handlers():
    def handle_signal(sig, frame):
        print(f"\n[INFO] Received signal {sig}, shutting down gracefully...")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_signal)
    try:
        signal.signal(signal.SIGTERM, handle_signal)
    except AttributeError:
        pass  # Windows may not support SIGTERM


async def handler(websocket):

    print("[*] New WebSocket connection from browser")

    nic_result = query_domain(
        "nic.cz", ["+dnssec", "+time=3", "+tries=2", "+multi", "nic.cz", "A"]
    )
    failed_result = query_domain(
        "dnssec-failed.org",
        ["+dnssec", "+time=3", "+tries=2", "dnssec-failed.org", "A"],
    )

    print("\n[DEBUG] nic.cz query details:")
    for k, v in nic_result["debug"].items():
        print(f"  {k}: {v}")

    print("\n[DEBUG] dnssec-failed.org query details:")
    for k, v in failed_result["debug"].items():
        print(f"  {k}: {v}")

    result = determine_result(nic_result, failed_result)

    print("\n[RESULT] Validation outcome:")
    for line in result["logs"]:
        print(" ", line)

    print(" -> Severity level:", result["result"])
    if result["error"]:
        print("Error message:", result["error"])

    await websocket.send(json.dumps(result))
    await websocket.wait_closed()


async def main():
    try:
        async with websockets.serve(handler, HOST, PORT):
            print(
                f"[  OK  ] F78FK-DNSSEC: WebSocket server listening on port {PORT} (v{__version__})"
            )
            await asyncio.Future()  # Run forever
    except OSError as e:
        # Typical failure: port already in use
        print(f"[FAILED] F78FK-DNSSEC: Failed to bind port {PORT} ({e.strerror})")
    except Exception as e:
        print(f"[FAILED] F78FK-DNSSEC: Unexpected error starting server")
        traceback.print_exc()


if __name__ == "__main__":
    setup_signal_handlers()
    try:
        asyncio.run(main())
    except RuntimeError:
        print(
            "[WARNING] Current environment does not support asyncio.run(), please run in local terminal."
        )
