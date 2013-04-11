; OpenIHM 1.5 setup

[Setup]
AppName=OpenIHM
AppVersion=1.5.1
DefaultDirName={sd}\Python27\Lib\site-packages\OpenIHM
DefaultGroupName=OpenIHM_1.5.1
UninstallDisplayIcon={app}\resources\images\openihm.png
Compression=lzma2
SolidCompression=yes
OutputBaseFilename=OpenIHM-Setup-1.5.1
OutputDir=.\setupfiles

[Files]
Source: ".\src\openihm\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\OpenIHM_1.5.1"; Filename: "{app}\openihmlauncher.bat"; WorkingDir: "{app}"
Name: "{group}\Update OpenIHM"; Filename: "{app}\openihmupdator.bat"; WorkingDir: "{app}"

