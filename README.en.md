# F78FK-DNSSEC-Checker
 
[中文](./README.md)

A program for detecting whether the current network fully supports the DNSSEC protocol, providing backend detection services for [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)

## ✨ Features
- Detects whether your network's DNS fully supports **DNSSEC** protocol
- After installation, visit [f78fk.com](https://ip.f78fk.com/dnssec) to run detection

## 🖥️ System Requirements
- Windows 10 (AMD64)
- Windows 11 (AMD64)
- Linux (AMD64)
- macOS (ARM64)

## 🚀 Installation and Usage

1. **Download the package**  
   - Get the executable file for your operating system from the [Releases](https://github.com/liuyuf78fk/F78FK-DNSSEC-Checker/releases)

2. **Windows**  
   - Double-click `F78FK-DNSSEC-Setup.exe` and follow the installation instructions  
   - After installation, open your browser and visit [f78fk.com](https://ip.f78fk.com/dnssec). The browser will automatically invoke the program for detection

3. **Linux**  
   - Navigate to the download directory and grant execute permission:  
     ```bash
     chmod +x f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - Run the program:  
     ```bash
     ./f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - After running the program, open your browser and visit [f78fk.com](https://ip.f78fk.com/dnssec)

4. **macOS**  
   - Navigate to the download directory and extract the archive
     ```bash
     tar -xzvf f78fk_dnssec_checker_<version>_arm64-macos.tar.gz
     ```
   - Grant execute permission and run the program：
     ```bash
     cd DNSSEC-Checker
	 ```
	 ```bash
	 chmod +x run-macos.sh
	 ```
	 ```bash
	 ./run-macos.sh
     ```
   - After running the program, open your browser and visit [f78fk.com](https://ip.f78fk.com/dnssec)
   - Safari browser is currently not supported; Firefox is recommended

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

You should see a message indicating a good signature from `F78FK <f78fk@live.com>`

#### 3. Export the plain-text SHA256 checksum file

```bash
gpg --decrypt sha256sums.asc > sha256sums
```

#### 4. Verify the integrity of the downloaded files using the plain text checksum file

```bash
sha256sum -c sha256sums
```