# F78FK-DNSSEC-Checker
 
[中文](./README.md)

A backend service that verifies complete DNSSEC protocol support on your network, powering the detection service at [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)

## ✨ Features
- Detects whether your network's DNS fully supports **DNSSEC** protocol
- After installation, visit [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) to run detection

## 🖥️ System Requirements
- Windows 10
- Windows 11

## 🚀 Installation & Usage
1. **Download installer**:
   - Get `F78FK-DNSSEC-Setup.exe` from [Releases page](https://github.com/liuyuf78fk/F78FK-DNSSEC-Checker/releases)
2. **Run installer**:
   - Double-click the setup file and follow the installation wizard
3. **Start detection**:
   - Visit [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) and the page will automatically invoke this tool to verify whether your network fully supports DNSSEC security extensions

## 📜 License & Dependencies
- **This software**: Licensed under [GNU GPL 3.0](./LICENSE)
- **Dependencies**:
  - Uses [ISC's `dig` tool](https://www.isc.org/downloads/) (from BIND tools), licensed under [MPL 2.0](dig/MPL-2.0.txt)
  - `dig.exe` is copyrighted by [Internet Systems Consortium (ISC)](https://www.isc.org/)

## 🔒 Security Notice
- Fully open-source code with no backdoors - users may audit the code
