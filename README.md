# F78FK-DNSSEC-Checker

[English](./README.en.md)  <!-- 跳转到英文版 -->

用于检测当前网络是否完整支持 DNSSEC 协议，是为了给 [ip.f78fk.com/dnssec](https://ip.f78fk.com/dnssec) 提供后端检测服务的程序

## ✨ 功能
- 检测当前网络的 DNS 是否完整支持 **DNSSEC**
- 安装后, 可以访问 [f78fk.com](https://ip.f78fk.com/dnssec) 开始检测

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
   - 安装完成后,打开浏览器访问 [f78fk.com](https://ip.f78fk.com/dnssec) 即可,浏览器会自动调用本程序进行检测

3. **Linux**  
   - 进入下载目录,赋予执行权限：  
     ```bash
     chmod +x f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - 运行程序：  
     ```bash
     ./f78fk_dnssec_checker_<version>_amd64-linux
     ```  
   - 程序运行后,打开浏览器访问 [f78fk.com](https://ip.f78fk.com/dnssec) 即可

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
   - 程序运行后,打开浏览器访问 [f78fk.com](https://ip.f78fk.com/dnssec) 即可
   - Safari 浏览器目前不支持, 推荐使用 Firefox

## 📜 许可证与依赖
- **本软件**：遵循 [GNU GPL 3.0](./LICENSE)
- **依赖工具**：
  - 使用 [ISC 的 `dig` 工具](https://www.isc.org/downloads/)（来自 BIND 工具集），遵循 [MPL 2.0](dig/MPL-2.0.txt)
  - `dig.exe` 版权归 [Internet Systems Consortium (ISC)](https://www.isc.org/) 所有

## 🔒 安全声明
- 代码完全开源，无后门，用户可自行审查


<br>

### 🔍 验证发布文件

为确保您下载的文件的真实性和完整性，请按以下步骤验证：

#### 1. 导入我们的公钥

执行以下命令，从 Ubuntu 公钥服务器导入我们的官方公钥：

```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys 9DDB7DB5ACD5B60A
```

#### 2. 验证校验文件签名

确认校验文件是由我们签名的：

```bash
gpg --verify sha256sums.asc
```

您应看到显示来自 `F78FK <f78fk@live.com>` 的有效签名

#### 3. 导出纯文本的 SHA256 校验文件

```bash
gpg --decrypt sha256sums.asc > sha256sums
```

#### 4. 用纯文本文件对下载的文件做完整性校验

```bash
sha256sum -c sha256sums
```
