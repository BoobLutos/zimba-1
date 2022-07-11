#import wmi

# connecting to local machine
#c = wmi.WMI() 

'''DRIVE_TYPES = {
  0 : "Unknown",
  1 : "No Root Directory",
  2 : "Removable Disk",
  3 : "Local Disk",
  4 : "Network Drive",
  5 : "Compact Disc",
  6 : "RAM Disk"
}

conn = wmi.WMI()
for drive in c.Win32_LogicalDisk():
    print (drive.Caption, DRIVE_TYPES[drive.DriveType])'''

import wmi
c = wmi.WMI()

for process in c.Win32_Process ():
    print (process.ProcessId, process.Name)
