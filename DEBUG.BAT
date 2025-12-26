ECHO Executing DEBUG.BAT >> c:\bootup.log
del debug.010 > nul

ren debug.009 debug.010 > nul
ren debug.008 debug.009 > nul
ren debug.007 debug.008 > nul
ren debug.006 debug.007 > nul
ren debug.005 debug.006 > nul
ren debug.004 debug.005 > nul
ren debug.003 debug.004 > nul
ren debug.002 debug.003 > nul
ren debug.001 debug.002 > nul

c:\stamp.exe >> debug.log
ren debug.log debug.001 > nul
ECHO scorer -dm -dl -dc -df >> c:\bootup.log
scorer -dm -dl -dc -df
