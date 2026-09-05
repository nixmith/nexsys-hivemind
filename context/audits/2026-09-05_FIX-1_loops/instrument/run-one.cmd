@echo off
setlocal
set TREE=%~1
set LOG=%~2
set RCF=%~3
shift
shift
shift
set ARGS=
:collect
if "%~1"=="" goto run
set ARGS=%ARGS% %1
shift
goto collect
:run
cd /d %TREE%
if not exist %TREE%\gradlew.bat (
  echo run-one: no gradlew.bat under %TREE% > %LOG%
  >%RCF% echo 98
  exit /b 98
)
call %TREE%\gradlew.bat %ARGS% > %LOG% 2>&1
>%RCF% echo %ERRORLEVEL%
endlocal
