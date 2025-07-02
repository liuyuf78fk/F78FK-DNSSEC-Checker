#!/bin/bash
set -e

APP_NAME="F78FK-DNSSEC-Checker"
PY_FILE="${APP_NAME}.py"
VERSION="1.0.4"
ARCH="amd64"
OS_NAME="linux"

pyinstaller \
  --onefile \
  --name "$APP_NAME" \
  "$PY_FILE"

mkdir -p release
mv "dist/$APP_NAME" "release/f78fk_dnssec_checker_${VERSION}_${ARCH}-${OS_NAME}"
