# F78FK-DNSSEC-Checker
 
[中文](./README.md)

A backend service that verifies complete DNSSEC protocol support on your network, powering the detection service at [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)

## ✨ Features
- Detects whether your network's DNS fully supports **DNSSEC** protocol
- After installation, visit [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) to run detection

## 🖥️ System Requirements
- Windows 10
- Windows 11
- Linux (AMD64)
- macOS (ARM64)

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


<br>

### 🔍 Verifying Releases

To ensure the authenticity and integrity of the files you download, please follow these verification steps:

#### 1. Import our public GPG key

Run the following command to fetch and import our official public key from the Ubuntu keyserver:

```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys 9DDB7DB5ACD5B60A
```

####  2. Verify the signature on the checksum file

Check that the checksum file is correctly signed by us:

```bash
gpg --verify sha256sums.asc
```

You should see a message indicating a good signature from `F78FK <f78fk@live.com>`.

####  3. Verify the SHA256 hashes of the downloaded files

Run the following command to confirm that your downloaded files match the official checksums:

```bash
sha256sum -c SHA256SUMS
```

If all files pass the checksum verification, your downloads are authentic and untampered.