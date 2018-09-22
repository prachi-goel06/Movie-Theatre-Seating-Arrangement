from inputFileParser import inputParser
import os

output=[]
seats=20

class tnode_0:                                     #Nil Node
    def __init__(self,seats):
        self.level=0
        self.name=None
        self.seatsPresent=[0*seats]
        self.seatsEmpty=None
        self.subs=[None,None]
        self.seatsOccupied = [0 for i in range (seats)]


NIL_NODE = tnode_0(seats)
# NIL_NODE.subs = [NIL_NODE,NIL_NODE]


class tnode:  # Creates New Node
    def __init__(self,name,seats,seatRequested,reservationID):
        self.isFull = False
        self.name=name
        self.totalSeats = 20
        self.subs=[None,None]
        self.seatsOccupied=[0 for i in range (seats)]
        self.seatsReserved(seatRequested,reservationID)
        self.seatsEmpty = self.vacantSeat(seats)

    def vacantSeat(self, seats):  # estimating number of vacant seats
        count=0
        for i in range(seats):
            if self.seatsOccupied[i]==0:
                count+=1
        return count

    def seatsReserved(self, seatRequested,reservationID):  # adding the reservation ID to the reserved seats
        seatsAssigned = []
        for i in range(len(self.seatsOccupied)):
            if seatRequested != 0:
                if self.seatsOccupied[i] == 0:
                    self.seatsOccupied[i] = reservationID
                    seatRequested -= 1
                    seatsAssigned.append(self.name+str(i))
            else:
                break

        output.append(reservationID+" "+",".join(seatsAssigned))
        return self.seatsOccupied






class BST:   #binary search tree to find the correct row and seats
    def __init__(self):
        self.totalNodes = 10
        self.root=NIL_NODE
        self.lastinsert=None
        self.totalSeats = 20
        self.seatsAvailable = self.totalNodes * self.totalSeats


    def height(self):
        return self.root.level

    def lookup(self,seatRequested):         #finding if the number of seats exist
        if self.root != NIL_NODE:
            # print("Root already present")
            return self.__lookup(self.root, seatRequested)

    def __lookup(self, tnode, seatRequested):
        # print ("Current Node is: ", tnode.name)
        if tnode.seatsEmpty >= seatRequested:
            return tnode
        else:
            sub=tnode.subs[1]
            if sub != None:
                # print("Child is present: going to child")
                return self.__lookup(sub, seatRequested)
            else:
                # print ("Child not present: Have to create a new child")
                return None

    def insert(self, seatRequested,reservationID,seats):
        # print("Inserting a new Node --------------")

        if self.root != NIL_NODE: # we are not an empty tree
            self.lastinsert = self.insertNode(self.root, seatRequested, self.totalNodes, reservationID)

        else: #adding the root to the tree
            name=chr(self.totalNodes+64)
            self.root = tnode(name,seats,seatRequested,reservationID)
            self.totalNodes -= 1
            self.lastinsert = self.root
            self.substractSeats (seatRequested)
        # print ("Exiting Insertion --------------")

    def insertNode(self, currentNode, seatRequested,totalNodes,reservationID):

        # print("Into insertNode: ")
        if seatRequested <= currentNode.seatsEmpty: # key exists, update value
            currentNode.seatsOccupied=self.seatsReserved(seatRequested,currentNode.reservationID)
            currentNode.seatsEmpty=self.vacantSeat(currentNode.seatsOccupied)
            self.substractSeats (seatRequested)
        elif seatRequested > currentNode.seatsEmpty:
            # print ("Current Node is: ", currentNode.name)
            # print ("Current Node seats are: ", currentNode.seatsOccupied)
            if(currentNode.subs[1]):
                # print ("Going into Right Row")
                return self.insertNode(currentNode.subs[1], seatRequested, totalNodes, reservationID)
            elif currentNode.subs[1]==None and totalNodes > 0:
                self.substractSeats (seatRequested)
                name = chr(self.totalNodes + 64)
                # print ("New Row Creation: total nodes current: ", self.totalNodes, " Name: ", name)
                currentNode.subs[1] = tnode(name,seats,seatRequested,reservationID)
                self.totalNodes -= 1
                return currentNode.subs[1]
        return currentNode.subs[1]

    def verifySeats(self, seatRequested, reservationID):  #checking if any back row with seats exists
        # print ("Seat Requested : ", seatRequested, " Reservation ID: ", reservationID)
        # print("total nodes are: ", self.totalNodes)
        tnode = self.lookup(seatRequested)
        # print ("")
        if tnode == None and self.totalNodes >0:
            # print ("creating new Node")
            self.insert(seatRequested, reservationID, seats)
            tnode = self.lastinsert
        elif (tnode != None):
            # print ("No need to create new Node")
            self.substractSeats(seatRequested)
            tnode.seatsReserved( seatRequested, reservationID)
            tnode.seatsEmpty = tnode.vacantSeat(seats)
        elif (self.totalNodes is 0):
            return

        # print("Current Node is: ", tnode.name)
        # print ("Current Node seats are: ", tnode.seatsOccupied)
        return tnode

    def substractSeats(self, seatsRequested):
        self.seatsAvailable -= seatsRequested

    def print_tree(self):
        print("******** Printing Tree ********")
        start_node = self.root
        while (start_node != None):
            print("Current Node: {}, Current Seat: {}".format(start_node.name, start_node.seatsOccupied) )
            start_node = start_node.subs[1]

    def writingOutput(self,seatsAssigned):
        outfile=open("outfile.txt", 'w+')
        for i in seatsAssigned:
            outfile.write(i+"\n")

if __name__ == '__main__':
    FilePath=input("Please Enter the File Path: ")
    data = inputParser(FilePath)
    Arrangement = BST()
    # print(data)
    for eachReservation in data:
        print("%%%%%%%%%%%%%%%%%%%: ", Arrangement.seatsAvailable)
        if Arrangement.seatsAvailable == 0:
            print("Theatre is full")
            break
        Arrangement.verifySeats(eachReservation[1], str(eachReservation[0]))

    Arrangement.print_tree()
    Arrangement.writingOutput(output)
    outputFilePath=os.getcwd()+'/'+'outfile.txt'
    print (outputFilePath)


