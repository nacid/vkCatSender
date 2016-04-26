@echo OFF
for /f "delims== tokens=1,2" %%G in (sender.properties) do set %%G=%%H
if not exist "%SAVE_PATH%" mkdir "%SAVE_PATH%"
%EXEC% sender.py %TOKEN% %SAVE_PATH% %TARGET%