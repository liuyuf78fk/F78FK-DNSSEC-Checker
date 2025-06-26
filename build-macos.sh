#!/bin/bash
set -e

# Required dependency: create-dmg
# Install via Homebrew: brew install create-dmg

# === Configuration ===
APP_NAME="F78FK-DNSSEC-Checker"
PY_FILE="${APP_NAME}.py"
ICON_FILE="${APP_NAME}.icns"
INFO_PLIST="Info.plist"

# Customize version and architecture here
VERSION="1.0.3"
ARCH="arm64"

# Final output file name
OUTPUT_NAME="f78fk_dnssec_checker_${VERSION}_${ARCH}-macos"

rm -rf dist

# === Build with PyInstaller ===
pyinstaller \
  --onefile \
  --windowed \
  --noconfirm \
  --name "$APP_NAME" \
  --icon="$ICON_FILE" \
  --osx-bundle-identifier com.f78fk.dnssecchecker \
  "$PY_FILE"

# === Replace Info.plist ===
cp "$INFO_PLIST" "dist/${APP_NAME}.app/Contents"

# === Create DMG ===
create-dmg \
  --volname "$APP_NAME" \
  --window-pos 200 120 \
  --window-size 500 300 \
  --icon-size 100 \
  --icon "${APP_NAME}.app" 100 120 \
  --app-drop-link 380 120 \
  "${OUTPUT_NAME}.dmg" \
  "dist/"

# === Move DMG to release directory ===
mkdir -p release
mv "${OUTPUT_NAME}.dmg" release/

echo "macOS DMG package created: release/${OUTPUT_NAME}.dmg"
