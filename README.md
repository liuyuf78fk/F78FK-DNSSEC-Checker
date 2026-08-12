# F78FK-DNSSEC-Checker

[English](./README.en.md)  <!-- 跳转到英文版 -->

一个本地辅助程序，用于检测你**当前网络的 DNS 解析器**是否执行 **DNSSEC 校验**（即是否能正确拦截签名无效/伪造 `bogus` 的域名）。

本程序配合网站 **[ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)** 一起使用。

> ⚠️ **注意**：本工具测试的是你**本地网络 / DNS 服务器的功能与能力**，而不是某个具体网站域名的 DNSSEC 配置是否正确。


## ❓ 为什么需要本地程序？

由于内置缓存或自带的 DoH（DNS-over-HTTPS）功能，浏览器经常会绕过系统默认的 DNS 设置。此外，浏览器本身并不亲自执行底层的 DNSSEC 签名校验。

为了准确测试你的路由器或运营商（ISP）DNS 解析器是否严格执行了 DNSSEC 校验，本轻量级本地工具通过 `dig` 命令直接向你系统当前生效的解析器发起查询——分别测试两个基准域名（一个具有合法 DNSSEC 签名，另一个签名故意配置损坏/`bogus`）——并将测试结果发送至网页端显示。


## ✨ 功能
- 检测当前网络的 DNS 是否完整支持 **DNSSEC**
- 安装后, 可以访问 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) 开始检测

## 🖥️ 系统支持
- Windows 10 (AMD64)
- Windows 11 (AMD64)
- Linux (AMD64)
- macOS (ARM64)

## 🚀 安装与使用

1. **下载安装包**  
   - 从 [Releases](https://github.com/liuyuf78fk/F78FK-DNSSEC-Checker/releases) 获取您的操作系统平台对应的可执行文件

2. **Windows**  
   - 双击 `F78FK-DNSSEC-Setup.exe`,按提示完成安装
   - 安装完成后,打开浏览器访问 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) 即可,浏览器会自动调用本程序进行检测

3. **Linux**  
   - 进入下载目录,赋予执行权限：  
     ```bash
     chmod +x f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - 运行程序：  
     ```bash
     ./f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - 程序运行后,打开浏览器访问 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) 即可

4. **macOS**  
   - 进入下载目录,解压文件
     ```bash
     tar -xzvf f78fk_dnssec_checker_<version>_arm64-macos.tar.gz
     ```
   - 赋予执行权限并运行程序：
     ```bash
     cd DNSSEC-Checker
	 ```
	 ```bash
	 chmod +x run-macos.sh
	 ```
	 ```bash
	 ./run-macos.sh
     ```
   - 程序运行后,打开浏览器访问 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) 即可
   - Safari 浏览器目前不支持, 推荐使用 Firefox

## 📜 许可证与依赖
- **本软件**：遵循 [GNU GPL 3.0](./LICENSE)
- **依赖工具**：
  - 使用 [ISC 的 `dig` 工具](https://www.isc.org/downloads/)（来自 BIND 工具集），遵循 [MPL 2.0](dig/MPL-2.0.txt)
  - `dig.exe` 版权归 [Internet Systems Consortium (ISC)](https://www.isc.org/) 所有
