# Pre-requisites: Imports od library and inputParser program.
# Loosely based on greedy algorithm and uses LinkedList.
# Each node is an instance of tnodes and represents a Theater Row.
# Reservations associated with one InputFile is an instance of BookingTheatre class.
# Different member functions of class BookingTheatre helps to perform allocate seats in the theatre.
# This program takes command line input of file path and shows the path to the output file.


from inputFileParser import inputParser
import os,sys
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
output={}
seats=20


class nilNode:  # Nil Node
    def __init__(self,seats):
        self.level=0
        self.name=None
        self.seatsPresent=[0*seats]
        self.seatsEmpty=None
        self.subs=[None,None]
        self.seatsOccupied = [0 for i in range (seats)]
        self.parent=None

NIL_NODE = nilNode(seats)
# NIL_NODE.subs = [NIL_NODE,NIL_NODE]


class tnode:  # Creates New Node
    def __init__(self,name,seats,seatRequested,reservationID,currentNode):
        self.isFull = False
        self.name=name
        self.totalSeats = 20
        self.subs=[None,None]
        self.seatsOccupied=[0 for i in range (seats)]
        self.seats_reserved(seatRequested, reservationID)
        self.seatsEmpty = self.vacant_seat(seats)
        self.parent = currentNode

    def vacant_seat(self, seats):  # estimating number of vacant seats
        count=0
        for i in range(seats):
            if self.seatsOccupied[i]==0:
                count+=1
        return count

    def seats_reserved(self, seatRequested, reservationID):  # adding the reservation ID to the reserved seats
        seats_assigned = []
        for i in range(len(self.seatsOccupied)):
            if seatRequested != 0:
                if self.seatsOccupied[i] == 0:
                    self.seatsOccupied[i] = reservationID
                    seatRequested -= 1
                    seats_assigned.append(self.name + str(i))
            else:
                break
        if reservationID not in output:
            output[reservationID]=",".join(seats_assigned)
        else:
            output[reservationID]+=","+",".join(seats_assigned)
        return self.seatsOccupied


class BookingTheatre:   # Linked List to find the correct row and seats
    def __init__(self):
        self.totalNodes = 10
        self.root=NIL_NODE
        self.lastinsert=None
        self.totalSeats = 20
        self.seatsAvailable = self.totalNodes * self.totalSeats

    def lookup(self,seatRequested):         # finding if any back row still vacant
        if self.root != NIL_NODE:
            logging.debug("Root already present")
            return self.__lookup(self.root, seatRequested)

    def __lookup(self, tnode, seatRequested): # recursive function to look for seats with empty seats
        logging.debug("Current Node is: {}".format( tnode.name))
        if tnode.seatsEmpty >= seatRequested:
            return tnode
        else:
            sub=tnode.subs[1]
            if sub != None:
                logging.debug("Current Node is {} with vacant seats{}".format(tnode.name,tnode.seatsEmpty))
                logging.debug("Trying to find better match in other nodes.....")
                return self.__lookup(sub, seatRequested)
            else:
                logging.debug("No matching vacant node found, Try creating a new node!")
                return None

    def insert(self, seatRequested,reservationID,seats):
        if self.root != NIL_NODE:  # we are not an empty tree
            self.lastinsert = self.__insert_node(self.root, seatRequested, self.totalNodes, reservationID)
            self.delete(self.lastinsert)
        else:  # adding the first node to the List
            logging.info("Adding new root row to the List")
            name = chr(self.totalNodes+64)
            self.root = tnode(name, seats, seatRequested, reservationID,None)
            self.totalNodes -= 1
            self.lastinsert = self.root
            self.substract_seats (seatRequested)
        #  ("Exiting Insertion --------------")

    def __insert_node(self, currentNode, seatRequested, totalNodes, reservationID):
        if seatRequested <= currentNode.seatsEmpty: # key exists, update value
            currentNode.seatsOccupied=currentNode.seatsReserved(seatRequested,currentNode.reservationID)
            currentNode.seatsEmpty=currentNode.vacant_seat(seats)
            self.substract_seats (seatRequested)
        elif seatRequested > currentNode.seatsEmpty: #lookup to find best place to add new node
            if(currentNode.subs[1]):
                return self.__insert_node(currentNode.subs[1], seatRequested, totalNodes, reservationID)
            elif currentNode.subs[1]==None and totalNodes > 0:  # adding a new node (row) to the linked list
                self.substract_seats (seatRequested)
                name = chr(self.totalNodes + 64)
                currentNode.subs[1] = tnode(name, seats, seatRequested, reservationID, currentNode)
                logging.info("Addign new row {} to the List".format(name))
                self.totalNodes -= 1
        return currentNode.subs[1]

    def verify_seats(self, seatRequested, reservationID):  # checking if any back row with seats exists else call insert function
        logging.debug ("Reservation ID:  Seat Requested : {} ".format(reservationID,seatRequested))
        can_insert_continous_seats = False
        if (seatRequested >20):
            return can_insert_continous_seats
        tnode = self.lookup(seatRequested)
        if tnode == None and self.totalNodes >0:
            self.insert(seatRequested, reservationID, seats)
            can_insert_continous_seats = True
        elif (tnode != None):
            logging.debug("No need to add a new node reservation can be accomodated in {}".format(tnode.name))
            self.substract_seats(seatRequested)
            tnode.seats_reserved(seatRequested, reservationID)
            tnode.seatsEmpty = tnode.vacant_seat(seats)
            parent=self.delete(tnode)
            can_insert_continous_seats = True
        elif (self.totalNodes is 0):
            return can_insert_continous_seats

        return can_insert_continous_seats

    def substract_seats(self, seatsRequested): #finding total seats available
        self.seatsAvailable -= seatsRequested

    def split_insert(self, seatsRequested, reservationID): # spliting the later bookings to utilise the theater
        logging.info("splitting the booking")
        self.substract_seats(seatsRequested)
        currentNode = self.root
        while currentNode!=None and seatsRequested!=0:
            if currentNode.seatsEmpty<=seatsRequested:
                logging.debug('current node name:{} empty seats:{} current seat requested: {}'.format(currentNode.name,str(currentNode.seatsEmpty),str(seatsRequested)))
                currentNode.seats_reserved(currentNode.seatsEmpty,reservationID)
                seatsRequested -= currentNode.seatsEmpty
                currentNode.seatsEmpty = currentNode.vacant_seat(seats)
                currentNode=currentNode.subs[1]
                self.delete(currentNode.parent)
            else:
                logging.debug('current node empty seats:{} seats requested: {}'.format(str(currentNode.seatsEmpty),str(seatsRequested)))
                currentNode.seats_reserved(seatsRequested,reservationID)
                currentNode.seatsEmpty=currentNode.vacant_seat(seats)
                seatsRequested-=seatsRequested
                self.delete(currentNode)

    def delete(self,currentNode):  # deleting the nodes(row) from the list for efficient search
        if currentNode.seatsEmpty==0:
            logging.debug("deleted node {}".format(currentNode.name))
            if currentNode == self.root and currentNode.subs[1] is not None:
                currentNode.subs[1].parent= None
                self.root=currentNode.subs[1]
                return self.root
            elif currentNode!= self.root:
                currentNode.parent.subs[1]=currentNode.subs[1]
                if currentNode.subs[1]!=None:
                    currentNode.subs[1].parent=currentNode.parent
                    return currentNode.parent
            else:
                self.root=nilNode
                return self.root

    def writing_output(self, data ,output):  # writing the output to the file
        logging.info("Program Finished....Writing seats allocated to the file")
        outfile=open("outfile.txt", 'w+')
        for eachReservation in data:
            if eachReservation[0] in output:
                outfile.write('{} {}\n'.format(eachReservation[0],output[eachReservation[0]]))
            else:
                outfile.write('{} {}\n'.format(eachReservation[0], str(0)))

if __name__ == '__main__':
    FilePath=sys.argv[1]
    data = inputParser(FilePath)
    Arrangement = BookingTheatre()
    not_inserted = []

    for eachReservation in data:  # allocating group seats in same row
        if Arrangement.seatsAvailable == 0:
            logging.info("Theatre is full no vacant seat available")
            break
        if not Arrangement.verify_seats(eachReservation[1], str(eachReservation[0])):
            not_inserted.append(eachReservation)
        logging.debug("Total seats still vacant".format(str(Arrangement.seatsAvailable)))
    more_inserted = []
    sorted_not_inserted_bookings=(sorted(not_inserted,key=lambda x:x[1]))

    for eachReservation in sorted_not_inserted_bookings:  # allocating remaining seats by splitting groups to utilize theater
        if (Arrangement.seatsAvailable == 0):
            break
        elif (eachReservation[1] > Arrangement.seatsAvailable):
            continue
        else:
            more_inserted.append(eachReservation)
            Arrangement.split_insert(eachReservation[1], str(eachReservation[0]))
        logging.debug("Total seats still vacant".format(str(Arrangement.seatsAvailable)))

    Arrangement.writing_output(data,output)
    outputFilePath=os.getcwd()+'/'+'outfile.txt'
    print ('{} {} {}\n'.format('\n','Output file location:',outputFilePath))
    logging.info("Check the terminal to fetch Output File path")


