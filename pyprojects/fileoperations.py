import logging
logging.basicConfig(level=logging.DEBUG, filename='pylog.log', format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#logging.debug("This is a debug message")

f=open("counting.txt","w+")

for i in range(10):
    f.write("This is rank %d\r" %(i+1))

logging.info("Counting complete")
   
f.close()


f=open("counting.txt","a+")

for i in range(4):
    f.write("This is rank %d\r" %(i+1))
logging.info("4 files have been appended")
   
f.close()


f=open("counting.txt","r")

if f.mode=="r":
    contents=f.read()
    
print (contents)
logging.info("Contents of a file have been read")
   
f.close()



