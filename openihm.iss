; OpenIHM setup

#include "version.iss"

[Setup]
AppName=OpenIHM
AppVersion={#AppVersion}
DefaultDirName={sd}\Python27\Lib\site-packages\OpenIHM
DefaultGroupName=OpenIHM_{#AppVersion}
UninstallDisplayIcon={app}\resources\images\openihm.png
Compression=lzma2
SolidCompression=yes
OutputBaseFilename=OpenIHM-Setup-{#AppVersion}
OutputDir=.\setupfiles

[Files]
Source: ".\src\openihm\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\binaries\sqlalchemy\*"; DestDir: "{app}\..\sqlalchemy"; Flags: onlyifdoesntexist recursesubdirs createallsubdirs

[Icons]
Name: "{group}\OpenIHM_{#AppVersion}"; Filename: "{app}\openihmlauncher.bat"; WorkingDir: "{app}"
Name: "{group}\Update OpenIHM"; Filename: "{app}\openihmupdator.bat"; WorkingDir: "{app}"

