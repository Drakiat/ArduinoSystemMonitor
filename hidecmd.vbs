Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c C:\Users\Felipe\Documents\PCMonitorPython\pcmonitor.bat"
oShell.Run strArgs, 0, false