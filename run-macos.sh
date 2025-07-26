#!/bin/bash

target=$(find . -maxdepth 1 -type f -iname "*arm64-macos*" | head -n 1)

if [ -z "$target" ]; then
    echo "Error: Target file not found."
    exit 1
fi

xattr -d com.apple.quarantine "$target" 2>/dev/null
chmod +x "$target"
./"$target"

