@echo off

if "%ProgramFiles(x86)%"=="" goto :x86
set PF=%ProgramFiles(x86)%
goto :pfset
:x86
set PF=%ProgramFiles%
:pfset

"%PF%\Inno Setup 5\ISCC.exe" openihm.iss 
if ERRORLEVEL 1 goto :error
"%PF%\Inno Setup 5\ISCC.exe" openihm-with-requirements.iss 
if ERRORLEVEL 1 goto :error
goto :end
:error
echo Error building installer
:end
