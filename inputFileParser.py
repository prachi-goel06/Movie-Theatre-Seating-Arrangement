#
# this program parse the input file into list of Reservations IDs and thier requested seats
# example:
# '''R0012 R002 4 R003 4 R004 3''' will return [[R001,2],[R002,4],[R003,4],[R004 3]]
# it will only have the data of reservations which will fill first 300 seats...
# Its implemented such that the algorthim meets both customer sattisfaction and theatre utilisation.
# If the algorithm is not able to adjust a booking in one row it will try to fit the next customer booking and skip the other.
#  Hence it intakes extra 100 seats booking to traverse and find the best suited.
#

import os

def inputParser(inpFile):
    if os.path.exists(inpFile):
        reservationList=[]
        inputFile=open(inpFile,'r')
        totalSeats=300
        for line in inputFile:
            if totalSeats >=0 :
                line = line.split()
                reservationList.append([line[0], int (line[1])])
                totalSeats-=1
            else:
                break
        return reservationList
    else:
        raise Exception("File Not Found Error")

