:Loop
echo off
: the variable below should have no spaces surrounding the '=' and is the name of the file to be outputted.

:FOR /F “TOKENS=1* DELIMS= ” %%A IN (‘DATE/T’) DO SET CDATE=%%B
:FOR /F “TOKENS=1,2 eol=/ DELIMS=/ ” %%A IN (‘DATE/T’) DO SET mm=%%B
:FOR /F “TOKENS=1,2 DELIMS=/ eol=/” %%A IN (‘echo %CDATE%’) DO SET dd=%%B
:FOR /F “TOKENS=2,3 DELIMS=/ ” %%A IN (‘echo %CDATE%’) DO SET yyyy=%%B
:SET date=%mm%%dd%%yyyy%

for /f "tokens=1-5 delims=/ " %%d in ("%date%") do set "output=test2-%%e-%%f-%%g.txt"

:set "output=test-08-11-14.xml"

echo.
echo ::::::::::::::::::::::::::::::::::::::::::::::::::::
echo           Dan Bennett -- listMetaData Password Test
echo ::::::::::::::::::::::::::::::::::::::::::::::::::::
echo.
echo This runs listMetaData on just the CustomObject and appends the output in %output%
echo Use it to test your passwords before running the looper, because if your login info is off, the looper will lock you out for too 
echo many bad attempts!!!!
echo.
call ant listMetadataLayout >> %output%
echo Calling listMetadataCustomObject...
call ant listMetadataCustomObject >> %output%
echo listMetadataCustomObject appended to %output%

 pause
REM goto Loop