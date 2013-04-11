; Bundle of OpenIHM with Python, PyQt, PyODBC and MySQL

[Setup]
AppName=OpenIHM with Requirements
AppVersion=1.5.1
DefaultDirName={pf}\OpenIHM
DisableProgramGroupPage=yes
Compression=lzma2/ultra64
;Compression=bzip/9
SolidCompression=yes
OutputBaseFilename=OpenIHM-with-Requirements-1.5.1
OutputDir=.\setupfiles

[Files]
Source: ".\binaries\mysql-5.5.15-win32.msi"; DestDir: "{app}"
Source: ".\binaries\python-2.7.3.msi"; DestDir: "{app}"
Source: ".\binaries\PyQt-Py2.7-x86-gpl-4.9.5-1.exe"; DestDir: "{app}"
Source: ".\binaries\pyodbc-3.0.6.win32-py2.7.exe"; DestDir: "{app}"
Source: ".\setupfiles\OpenIHM-Setup-1.5.1.exe"; DestDir: "{app}"
Source: ".\binaries\mercurial-2.3.1.win32-py2.7.exe"; DestDir: "{app}"
Source: ".\binaries\MySQL-python-1.2.3.win32-py2.7.exe"; DestDir: "{app}"

[Registry]
Root: "HKLM"; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "C:\Python27;{olddata}"

[Run]
Filename: "{app}\python-2.7.3.msi"; Description: "Python Programming Language"; Flags: postinstall shellexec waituntilterminated
Filename: "{app}\PyQt-Py2.7-x86-gpl-4.9.5-1.exe"; Description: "PyQt"; Flags: postinstall shellexec waituntilterminated
Filename: "{app}\pyodbc-3.0.6.win32-py2.7.exe"; Description: "PyODBC"; Flags: postinstall shellexec waituntilterminated
Filename: "{app}\mercurial-2.3.1.win32-py2.7.exe"; Description: "Mercurial"; Flags: postinstall shellexec waituntilterminated
Filename: "{app}\mysql-5.5.15-win32.msi"; Description: "MySQL Database Server"; Flags: postinstall shellexec waituntilterminated
Filename: "{app}\MySQL-python-1.2.3.win32-py2.7.exe"; Description: "Python MySQL Database Connector"; Flags: postinstall shellexec waituntilterminated
Filename: "{app}\OpenIHM-Setup-1.5.1.exe"; Description: "OpenIHM 1.5.1 Setup"

