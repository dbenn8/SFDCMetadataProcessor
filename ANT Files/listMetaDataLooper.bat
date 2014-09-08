:Loop
echo off
: the variable below should have no spaces surrounding the '=' and is the name of the file to be outputted.
:set "output=output-8-11-14.xml"
for /f "tokens=1-5 delims=/ " %%d in ("%date%") do set "output=output2-%%e-%%f-%%g.txt"

echo.
echo ::::::::::::::::::::::::::::::::::::::::::::::::::::
echo           Dan Bennett -- listMetaData looper
echo ::::::::::::::::::::::::::::::::::::::::::::::::::::
echo.
echo This runs listMetaData on each available metadata type appends the output in %output%
echo.
echo Calling listMetadataCustomObject...
call ant listMetadataCustomObject >> %output%
echo listMetadataCustomObject appended to %output%
echo Calling listMetadataApexClass...


  call ant listMetadataApexClass >> %output%
  call ant listMetadataApexComponent >> %output%
  call ant listMetadataApexPage >> %output%
  call ant listMetadataApexTrigger >> %output%
  call ant listMetadataBusinessProcess >> %output%
  call ant listMetadataCustomApplication >> %output%
  call ant listMetadataCustomField >> %output%
  call ant listMetadataCustomLabels >> %output%
:dup  call ant listMetadataCustomObject >> %output%
  call ant listMetadataCustomObjectTranslation >> %output%
:  GOTO End
  call ant listMetadataCustomPageWebLink >> %output%
  call ant listMetadataCustomSite >> %output%
  echo 33 percent of calls complete
  call ant listMetadataCustomTab >> %output%
:folder  call ant listMetadataDashboard >> %output%
  call ant listMetadataDataCategoryGroup >> %output%
  call ant listMetadataDocument >> %output%
  call ant listMetadataEmailTemplate >> %output%
:  call ant listMetadataEntitlementTemplate >> %output%
  call ant listMetadataFieldSet >> %output%
  call ant listMetadataFlow >> %output%
:  call ant listMetadataFolder >> %output%
:  call ant listMetadataGroup >> %output%
  call ant listMetadataHomePageComponent >> %output%
  call ant listMetadataHomePageLayout >> %output%
  call ant listMetadataLayout >> %output%
  call ant listMetadataLetterhead >> %output%
  echo 66 percent of calls complete
  call ant listMetadataListView >> %output%
  call ant listMetadataNamedFilter >> %output%
  call ant listMetadataPermissionSet >> %output%
:  call ant listMetadataPortal >> %output%
  call ant listMetadataProfile >> %output%
  call ant listMetadataQueue >> %output%
  call ant listMetadataRecordType >> %output%
  call ant listMetadataRemoteSiteSetting >> %output%
:folder  call ant listMetadataReport >> %output%
:folder?  call ant listMetadataReportType >> %output%
  call ant listMetadataRole >> %output%
  call ant listMetadataScontrol >> %output%
  call ant listMetadataSharingReason >> %output%
  call ant listMetadataStaticResource >> %output%
:failed because Territory not in org  call ant listMetadataTerritory >> %output%
:  call ant listMetadataTranslations >> %output%
  call ant listMetadataValidationRule >> %output%
:failed  call ant listMetadataWeblink >> %output%
  call ant listMetadataWorkflow >> %output%
  echo 100 percent of calls complete
:END
 pause
REM goto Loop