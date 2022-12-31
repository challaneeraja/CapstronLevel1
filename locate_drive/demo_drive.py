import win32api
import os
def GetDrive():
    drives=win32api.GetLogicalDriveStrings()
    print(drives)
    drives=drives.split('\000')[:-1]
    return drives
print(GetDrive())
