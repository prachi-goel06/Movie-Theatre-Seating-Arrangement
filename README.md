# Movie-Theatre-Seating-Arrangement
Algorithm to implement seating arrangement in a movie theatre to maximize both customer satisfaction and theater utilization.

#Summary: 
This algorithm arranges the seats for the customer such that the customer sattisfaction is received by allocating majority seats of the reservation together and maximising theater utilisation . 

#Description: 
Given a theatre with seating capacity of 20 seats in each of the 10 rows (200 seats), the algorithm needs to assign seats to the customer to maximise theatre utilisation and gaurantees customer sattisfaction. 

#Input: 
An input file which would contain one line of input for each reservation request. The order of the lines in the file reflects the order in which the reservation requests were received. Each line in the file will be comprised of a reservation identifier, followed by a space, and then the number of seats requested. The reservation identifier will have the format: R####.
Example: 
R001 2 
R002 4 
R003 4 
R004 3

#Output: 
The program should output a file containing the seating assignments for each request. Each row in the file should include the reservation number followed by a space, and then a comma-delimited list of the assigned seats.
Example: 
R001 I1,I2
R002 F16,F17,F18,F19 
R003 A1,A2,A3,A4 
R004 J4,J5,J6

#Approach to solution: 
This problem is a type of Constraint sattisfaction problem in which set of objects whose state must satisfy a number of constraints or limitations. CSPs represent the entities in a problem as a homogeneous collection of finite constraints over variables, which is solved by constraint satisfaction methods. These kind of problems have high complexity and generally cannot be solved in polynomial time thus making them a part of NP Hard problems. 

Why the problem is a CSP: 
Formally as stated in wiki a CSP is: 
Formally, a constraint satisfaction problem is defined as a triple <X,D,C> where
X={X1,,,,,,Xn} is a set of variables,
D={D1,,,,,,Dn} is a set of the respective domains of values, and
C={C1,,,,,,Cm} is a set of constraints.
Each variable X can take on the values in the nonempty domain D. Every constraint in C is in turn a pair <Ti,Ri> , where Ti belongs to X is a subset of k variables and R is a  k-ary relation on the corresponding subset of domains Di. An evaluation of the variables is a function from a subset of variables to a particular set of values in the corresponding subset of domains. An evaluation v satisfies a constraint  if the values assigned to the variable satisfies the relation.[1]


#Assumptions made while implementing the Algorithm:
1. Cost of all the seats in the theatre are same. 
2. Seats are reserved on the First come first serve basis. 
3. Customers who reserves the seat first are offered better seats(seats that are far from the screen) than the customers who are reserve later. 
4. Bulk seat booking reservation(>=100)will be given more priotity than small bookings. 
5. Small Reservations for 2 seats or greater which will split into different rows or a customer might need to sit alone will be given less priority than other reservations that can be accumalted nicely. Example: 2 seats are left in A and 1 seat is left in B, the reservation for 2 seats will be given priority over reservation for 3 seats 
6. Customer likes to sit in the middle of the row in the theatres. 

Approach to the implement the solution: 
 1. Implemented a Binary search tree starting with row 'J' as the root.
 2. Added new rows(I,H,G....A) when the seats to be reserved are greater than seats empty in the tree. 
    If seats in I are greater than J becomes the right child of the node else the left child. 
 3. If the row is Full, it is removed from the tree and replaced with next row. example if J is full it was deleted from the       tree and I becomes the node. 
 4. Program exits if the tree is empty again after adding 20 nodes or cannot accomodate the rest of the reservation. 
 
 Why Using BST: 
 we want to accomodate the seats in first come first serv. 
 
 
