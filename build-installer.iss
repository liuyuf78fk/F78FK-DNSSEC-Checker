[Setup]
AppName=F78FK-DNSSEC-Checker
AppVersion=1.0.0
DefaultDirName={pf}\F78FK\F78FK-DNSSEC
DisableProgramGroupPage=yes
OutputDir=.
OutputBaseFilename=F78FK-DNSSEC-Setup
SetupIconFile=favicon.ico
UninstallDisplayIcon={app}\F78FK-DNSSEC-Checker.exe
CreateUninstallRegKey=yes
ArchitecturesInstallIn64BitMode=x64


[Files]
Source: "dist\F78FK-DNSSEC-Checker.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dig\dig.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dig\*.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dig\MPL-2.0.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: ".\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: ".\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: ".\README.en.md"; DestDir: "{app}"; Flags: ignoreversion


[Icons]

[Registry]
Root: HKCR; Subkey: "f78fk-dnssec"; Flags: uninsdeletekey
Root: HKCR; Subkey: "f78fk-dnssec"; ValueType: string; ValueName: ""; ValueData: "URL:F78FK DNSSEC Protocol"
Root: HKCR; Subkey: "f78fk-dnssec"; ValueType: string; ValueName: "URL Protocol"; ValueData: ""
Root: HKCR; Subkey: "f78fk-dnssec\shell\open\command"; ValueType: string; ValueData: """{app}\F78FK-DNSSEC-Checker.exe"" ""%1"""

[Run]
Filename: "{app}\F78FK-DNSSEC-Checker.exe"; Description: "Run F78FK-DNSSEC-Checker now"; Flags: nowait postinstall skipifsilent
