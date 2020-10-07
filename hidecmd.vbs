Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c pcmonitor.bat"
oShell.Run strArgs, 0, false
