@echo off
call %~dp0\pf_find.bat
"%PF%\Inno Setup 5\ISCC.exe" openihm.iss 
