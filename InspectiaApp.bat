@echo off
SETLOCAL
set OSGEO4W_ROOT=C:/Program Files/QGIS 3.40.10
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
REM start /B python .\InspectiaApp.py
start pythonw .\InspectiaApp.py
REM start python -X faulthandler .\InspectiaApp.py
ENDLOCAL
