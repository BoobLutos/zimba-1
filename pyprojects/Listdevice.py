import wmi
import logging
logging.basicConfig(level=logging.DEBUG, filename='pylog.log', format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

DRIVE_TYPES = {
    0 : "Unknown",
    1 : "No Root Directory",
    2 : "Removable Disk",
    3 : "Local Disk",
    4 : "Network Drive",
    5 : "Compact Disc",
    6 : "RAM Disk"
}
conn = wmi.WMI()
for drive in conn.Win32_LogicalDisk():
    print (drive.Caption, DRIVE_TYPES[drive.DriveType])
logging.warning("New devices have been detected")
