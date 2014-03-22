@echo off
if "%ProgramFiles(x86)%"=="" goto :x86
set PF=%ProgramFiles(x86)%
goto :pfset
:x86
set PF=%ProgramFiles%
:pfset
