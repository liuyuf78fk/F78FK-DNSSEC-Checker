# F78FK-DNSSEC-Checker
 
[中文](./README.md)

A local helper program for detecting whether your current DNS resolution path validates DNSSEC (i.e., properly blocks invalid/bogus domain signatures). 

It works alongside the online test dashboard at **[ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)**.

> ⚠️ **Note**: This tool tests your **local network / DNS server capabilities**, NOT the DNSSEC configuration of individual website domain names.


## ❓ Why is a Local Program Required?

Browsers often bypass system DNS settings due to internal caching or built-in DoH (DNS-over-HTTPS). Furthermore, browsers themselves do not perform raw DNSSEC validation.
To accurately test whether your router or ISP's DNS resolver strictly enforces DNSSEC validation, this lightweight local tool uses the dig utility to query your active system resolver directly—testing two benchmark domains (one with a valid DNSSEC signature and one with a broken bogus signature)—and sends the validation results to the browser interface.

## ✨ Features
- Detects whether your network's DNS fully supports **DNSSEC** protocol
- After installation, visit [https://ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) to run detection

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
   - After installation, open your browser and visit [https://ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec). The browser will automatically invoke the program for detection

3. **Linux**  
   - Navigate to the download directory and grant execute permission:  
     ```bash
     chmod +x f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - Run the program:  
     ```bash
     ./f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - After running the program, open your browser and visit [https://ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)

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
   - After running the program, open your browser and visit [https://ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)
   - Safari browser is currently not supported; Firefox is recommended

## 📜 License & Dependencies
- **This software**: Licensed under [GNU GPL 3.0](./LICENSE)
- **Dependencies**:
  - Uses [ISC's `dig` tool](https://www.isc.org/downloads/) (from BIND tools), licensed under [MPL 2.0](dig/MPL-2.0.txt)
  - `dig.exe` is copyrighted by [Internet Systems Consortium (ISC)](https://www.isc.org/)
