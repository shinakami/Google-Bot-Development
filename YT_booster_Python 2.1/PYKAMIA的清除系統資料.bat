@echo off
echo processing cleaning (PYKAMIA version) now......
del /f /s /q %systemdrive%\*.tmp
del /f /s /q %systemdrive%\*._mp
del /f /s /q %systemdrive%\*.log
del /f /s /q %systemdrive%\*.gid
del /f /s /q %systemdrive%\*.chk
del /f /s /q %systemdrive%\*.old
del /f /s /q %systemdrive%\recycled\*.*
del /f /s /q %windir%\*.bak
del /f /s /q %windir%\prefetch\*.*
del /f /q %userprofile%\cookies\*.*
del /f /q %userprofile%\recent\*.*
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*"
del /f /s /q "%userprofile%\Local Settings\Temp\*.*"
del /f /s /q "%userprofile%\recent\*.*"

echo Deleting video, graphic, audio file, useless doc. in Downloads folder
del /f /s /q C:\Users\User\Downloads\*.mp4
del /f /s /q C:\Users\User\Downloads\*.mp3
del /f /s /q C:\Users\User\Downloads\*.wav
del /f /s /q C:\Users\User\Downloads\*.jpg
del /f /s /q C:\Users\User\Downloads\*.png
del /f /s /q C:\Users\User\Downloads\*.zip
del /f /s /q C:\Users\User\Downloads\*.rar
del /f /s /q C:\Users\User\Downloads\*.pdf
del /f /s /q C:\Users\User\Downloads\*.txt
del /f /s /q C:\Users\User\Downloads\*.csv
del /f /s /q C:\Users\User\Downloads\*.doc
del /f /s /q C:\Users\User\Downloads\*.exe



DEL /S /F /Q "%systemroot%\Temp\*.*"
DEL /S /F /Q "%AllUsersProfile%\「開始」功能表\程式集\Windows Messenger.lnk"
RD /S /Q %windir%\temp & md %windir%\temp
RD /S /Q "%userprofile%\Local Settings\Temp"
MD "%userprofile%\Local Settings\Temp"
RD /S /Q "%systemdrive%\Program Files\Temp"
MD "%systemdrive%\Program Files\Temp"
RD /S /Q "%systemdrive%\d"
net user aspnet /delete
cleanmgr /sagerun:99

echo Cleaning Finished！！
EXIT