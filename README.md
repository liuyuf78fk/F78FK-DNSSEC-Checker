# F78FK-DNSSEC-Checker

[English](./README.en.md)  <!-- 跳转到英文版 -->

用于检测当前网络是否完整支持 DNSSEC 协议，是为了给 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) 提供后端检测服务的程序

## ✨ 功能
- 检测当前网络的 DNS 是否完整支持 **DNSSEC**
- 安装后, 可以访问 [ip.f78fk.com/dnssec](ip.f78fk.com/dnssec) 开始检测

## 🖥️ 系统支持
- Windows 10
- Windows 11
- Linux (AMD64)
- macOS (ARM64)

## 🚀 安装与使用
1. **下载安装包**：
   - 从 [Releases 页面](https://github.com/liuyuf78fk/F78FK-DNSSEC-Checker/releases) 获取 `F78FK-DNSSEC-Setup.exe`
2. **运行安装向导**：
   - 双击安装程序，按提示完成安装
3. **开始检测**：
   - 打开 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec)，页面将自动调用本程序检测您的网络是否完整支持 DNSSEC 安全扩展标准

## 📜 许可证与依赖
- **本软件**：遵循 [GNU GPL 3.0](./LICENSE)
- **依赖工具**：
  - 使用 [ISC 的 `dig` 工具](https://www.isc.org/downloads/)（来自 BIND 工具集），遵循 [MPL 2.0](dig/MPL-2.0.txt)
  - `dig.exe` 版权归 [Internet Systems Consortium (ISC)](https://www.isc.org/) 所有

## 🔒 安全声明
- 代码完全开源，无后门，用户可自行审查
