#!/bin/bash
set -e

APP_NAME="F78FK-DNSSEC-Checker"
PY_FILE="${APP_NAME}.py"
ICON_FILE="${APP_NAME}.icns"

VERSION="1.0.3"
ARCH="arm64"
OUTPUT_NAME="f78fk_dnssec_checker_${VERSION}_${ARCH}-macos"

rm -rf dist build "__pycache__" "${APP_NAME}.spec"

pyinstaller \
  --onefile \
  --noconfirm \
  --name "$APP_NAME" \
  --icon="$ICON_FILE" \
  --osx-bundle-identifier com.f78fk.dnssecchecker \
  "$PY_FILE"

mkdir -p release
cp "dist/${APP_NAME}" "release/${OUTPUT_NAME}"

TMP_DIR="DNSSEC-Checker"
rm -rf "$TMP_DIR"
mkdir "$TMP_DIR"

cp "release/${OUTPUT_NAME}" "$TMP_DIR/"
cp "run-macos.sh" "$TMP_DIR/"

# Clean extended attributes to avoid "._" files
xattr -rc "$TMP_DIR"

tar -czf "${OUTPUT_NAME}.tar.gz" "$TMP_DIR"
rm -rf "$TMP_DIR"
mv "${OUTPUT_NAME}.tar.gz" release/

echo "Build and packaging complete: ${OUTPUT_NAME}.tar.gz"

