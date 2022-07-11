'''
Created on Feb 2, 2020

@author: Lutaaya
'''
import logging
logging.basicConfig(level=logging.DEBUG, filename='pylog.log', filemode='a', format='%(asctime)s-%(process)d-%(name)s-%(levelname)s-%(message)s')
logging.warning("This is a warning message")


inputString = input('')

f=open("discreet.txt","w+")
f.write(inputString)
logging.info("discreet logging completed")
f.close()

