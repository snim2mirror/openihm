@echo off

if "%ProgramFiles(x86)%"=="" goto :x86
set PF=%ProgramFiles(x86)%
goto :pfset
:x86
set PF=%ProgramFiles%
:pfset

IF EXIST %~dp0\binaries\.hg goto :skip_deps
echo Downloading dependencies for the first time...
hg clone https://bitbucket.org/colinnewell/open-ihm-installer-dependencies binaries
:skip_deps
rmdir /s /q %TEMP%\ihm-build
hg clone %~dp0 %TEMP%\ihm-build
hg clone %~dp0\binaries %TEMP%\ihm-build\binaries
cd /d %TEMP%\ihm-build

"%PF%\Inno Setup 5\ISCC.exe" openihm.iss 
if ERRORLEVEL 1 goto :error
"%PF%\Inno Setup 5\ISCC.exe" openihm-with-requirements.iss 
if ERRORLEVEL 1 goto :error
goto :end
:error
echo Error building installer
:end
