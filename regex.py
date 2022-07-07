#^
import re
import winsound
from playsound import playsound
#from pygame import mixer
#from playsound import playsound
#soundfile='C:\Users\Lutaaya\Downloads\Behold (Then Sings My Soul) - Hillsong Worship [360p].mp4'


#txt = "23-567+65+23456+098-4679-345"
#x = re.search(r"^\d+(?:[+-]\d+)+", txt)
#print(x.group())




txt = '8\r33'
substr="\r"
if re.search(substr, txt):
    print("found")
else:
    print("not found")
    

winsound.Beep(400, 300)
#winsound.PlaySound(soundfile, winsound.SND_FILENAME)
#playsound('E:\EclipseProjects\Startpython\VID00041.wav')
