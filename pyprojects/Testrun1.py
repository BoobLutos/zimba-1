'''
Created on Feb 2, 2020

@author: Lutaaya
'''
import logging
logging.basicConfig(level=logging.DEBUG, filename='pylog.log', filemode='a', format='%(asctime)s-%(process)d-%(name)s-%(levelname)s-%(message)s')
logging.warning("This is a warning message")

''''a = "high five"
print("a =", a)

b=13
c=12
print("b+c =", b+c)
print("b*c =", b*c)
print("b/c =", b/c)
print("b//c =", b//c)
print("b%c =", b%c)
print("b^c =", b**c)'''

inputString = input('')
#print('The entered string is:', inputString)


'''name    = input("Enter Employee Name")
salary  = input("Enter salary")
company = input ("Enter Company name")
print("Printing Employee Details")
print ("Name", "Salary", "Company")
print (name, salary, company)'''

f=open("discreet.txt","w+")
f.write(inputString)
logging.info("discreet logging completed")
f.close()

