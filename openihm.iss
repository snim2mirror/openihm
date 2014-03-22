; OpenIHM 1.5 setup

[Setup]
AppName=OpenIHM
AppVersion=1.5.2.sqlalchemy
DefaultDirName={sd}\Python27\Lib\site-packages\OpenIHM
DefaultGroupName=OpenIHM_1.5.2.sqlalchemy
UninstallDisplayIcon={app}\resources\images\openihm.png
Compression=lzma2
SolidCompression=yes
OutputBaseFilename=OpenIHM-Setup-1.5.2.sqlalchemy
OutputDir=.\setupfiles

[Files]
Source: ".\src\openihm\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\binaries\sqlalchemy\*"; DestDir: "{app}\..\sqlalchemy"; Flags: onlyifdoesntexist recursesubdirs createallsubdirs

[Icons]
Name: "{group}\OpenIHM_1.5.2.sqlalchemy"; Filename: "{app}\openihmlauncher.bat"; WorkingDir: "{app}"
Name: "{group}\Update OpenIHM"; Filename: "{app}\openihmupdator.bat"; WorkingDir: "{app}"

