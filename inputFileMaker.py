#This programs generates random seat reservation requests for about 1000 seats.
'''
    file format:
    R001 2
    R002 4
    R003 4
    R004 3
'''

import random
x=0
inputFile=open("InputFile.txt","w+")
i=1
while x<1000:
     seatsReserved=random.randint(1,20)
     x=+seatsReserved
     inputFile.write('{} {}{}'.format("R"+'{:04d}'.format(i),seatsReserved,'\n'))
     i=i+1

inputFile.close()
