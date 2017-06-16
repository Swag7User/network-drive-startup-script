import time
import subprocess
import sys
#import wmi
import os
#import win32api

print("This is a startupscript for properly connecting network drives and starting qbittorrent on very fast booting mashines.") 
time.sleep(15)

#kill explorer process, may be necessary because microsoft can't get it together....

# Disconnect anything on V
#print("Disconnect anything on W") 

#print("kill explorer") 

#for process in wmi.WMI().Win32_Process ():
#    if process.Name == 'explorer.exe':
#        PROCESS_TERMINATE = 1
#        handle = win32api.OpenProcess(PROCESS_TERMINATE, False, process.ProcessId)
#        win32api.TerminateProcess(handle, -1)
		
#print("start explorer") 
#time.sleep(3)
#subprocess.Popen([r'explorer'])
#print("map V again") 

#time.sleep(3)

# Connect to shared drive, use drive letter V
subprocess.call(r'net use s: "\\Netowrklocation\drive1" password /u:user', shell=True)
subprocess.call(r'net use t: "\\Netowrklocation\drive2" password /u:user', shell=True)
subprocess.call(r'net use u: "\\Netowrklocation\drive3" password /u:user', shell=True)
subprocess.call(r'net use v: "\\Netowrklocation\drive4" password /u:user', shell=True)
subprocess.call(r'net use w: "\\Netowrklocation\drive5" password /u:user', shell=True)
subprocess.call(r'net use x: "\\Netowrklocation\drive6" password /u:user', shell=True)
subprocess.call(r'net use y: "\\Netowrklocation\drive7" password /u:user', shell=True)
subprocess.call(r'net use z: "\\Netowrklocation\drive8" password /u:user', shell=True)

#subprocess.Popen(r'explorer /select,"V:\startup"')
#subprocess.Popen(r'explorer /select,"W:\startup"')

# drive1
f = open(r'\\Netowrklocation\drive1\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

# drive2
f = open(r'\\Netowrklocation\drive2\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

# drive3
f = open(r'V:\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

# drive4
f = open(r'W:\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

# drive5
f = open(r'X:\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

# drive6
f = open(r'Y:\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

# drive7
f = open(r'Z:\startup.txt', "r")
line = f.readline()

while line:
    print (line)
    line = f.readline()
f.close()

time.sleep(2)

#now execute qbittorrent
subprocess.Popen([r'C:\Program Files (x86)\qBittorrent\qbittorrent.exe'])

print("All done, qbittorrent should start now") 

sys.exit(1)