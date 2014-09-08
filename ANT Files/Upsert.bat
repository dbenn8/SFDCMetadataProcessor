:Loop
echo off
echo.
echo ::::::::::::::::::::::::::::::::::::::::::::::::::::
echo           ServiceMax Migrator 1.0
echo ::::::::::::::::::::::::::::::::::::::::::::::::::::
echo.
echo edit upsert.bat call to ant -v Upsert for verbose error checking
echo edit upsert.bat call to ant Upsert to disable verbose error checking
echo.
call ant Upsert
pause
REM goto Loop