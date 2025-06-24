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

__version__ = "1.0.0"
__author__ = "Liu Yu"
__license__ = "GPLv3"

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
            [DIG_PATH] + args, capture_output=True, text=True, timeout=10, env=clean_env
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
    logs = []
    logs.append(f"Parsed nic.cz: AD={nic['ad']}, Status={nic['status']}")
    logs.append(
        f"Parsed dnssec-failed.org: AD={failed['ad']}, Status={failed['status']}"
    )

    if nic["error"] or failed["error"]:
        return {
            "result": "tool-error",
            "logs": logs,
            "nic": nic,
            "failed": failed,
            "error": nic["error"] or failed["error"],
        }

    if not nic["debug"].get("output") or not failed["debug"].get("output"):
        logs.append("Missing dig output — possible network issue.")
        return {
            "result": "unknown",
            "logs": logs,
            "nic": nic,
            "failed": failed,
            "error": None,
        }

    if nic["ad"] and not failed["ad"] and failed["status"] == "SERVFAIL":
        result = "secure"
        logs.append("Secure: local resolver validates DNSSEC correctly.")

    elif not nic["ad"] and failed["status"] == "SERVFAIL":
        result = "medium"
        logs.append("Medium: local resolver does not validate, but upstream does.")

    elif failed["status"] != "SERVFAIL":
        result = "insecure"
        logs.append("Insecure: failed domain resolved without SERVFAIL.")

    else:
        result = "unknown"
        logs.append("Unknown state: unable to determine DNSSEC status.")

    return {"result": result, "logs": logs, "nic": nic, "failed": failed, "error": None}


async def handler(websocket):

    print("[*] New WebSocket connection from browser")

    nic_result = query_domain("nic.cz", ["+dnssec", "+multi", "nic.cz", "A"])
    failed_result = query_domain(
        "dnssec-failed.org", ["+dnssec", "dnssec-failed.org", "A"]
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

    print("[  OK  ] F78FK-DNSSEC WebSocket (port 11111)")
    try:
        async with websockets.serve(handler, "127.0.0.1", 11111):
            await asyncio.Future()
    except Exception:
        print("[ERROR] WebSocket startup failed:")
        traceback.print_exc()


if __name__ == "__main__":

    try:
        asyncio.run(main())
    except RuntimeError:
        print(
            "[WARNING] Current environment does not support asyncio.run(), please run in local terminal."
        )
