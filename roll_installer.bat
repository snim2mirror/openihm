@echo off

REM NOTE: if you want to roll an installer for a different branch
REM for testing purposes, set the IHM-BRANCH environment variable.
REM e.g. SET IHM-BRANCH=sqlalchemy

call %~dp0\pf_find.bat

IF EXIST %~dp0\binaries\.hg goto :skip_deps
echo Downloading dependencies for the first time...
hg clone https://bitbucket.org/colinnewell/open-ihm-installer-dependencies binaries
:skip_deps
rmdir /s /q %TEMP%\ihm-build
cd /d %~dp0
hg clone %~dp0 %TEMP%\ihm-build
hg clone %~dp0\binaries %TEMP%\ihm-build\binaries
cd /d %TEMP%\ihm-build
IF "%IHM-BRANCH%" == "" goto :nobranch
hg checkout -C %IHM-BRANCH%
:nobranch
call source_installer.bat
if ERRORLEVEL 1 goto :error
call dependencies_installer.bat
if ERRORLEVEL 1 goto :error
goto :end
:error
echo Error building installer
:end
