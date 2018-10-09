# Movie-Theatre-Seating-Arrangement
Algorithm to implement seating arrangement in a movie theatre to maximize both customer satisfaction and theater utilization.

Summary: 

This algorithm arranges the seats for the customer such that the customer sattisfaction is received by allocating majority seats of the reservation together and maximising theater utilisation . 

Description: 

Given a theatre with seating capacity of 20 seats in each of the 10 rows (200 seats), the algorithm needs to assign seats to the customer to maximise theatre utilisation and gaurantees customer sattisfaction. 

Input: 

An input file which would contain one line of input for each reservation request. The order of the lines in the file reflects the order in which the reservation requests were received. Each line in the file will be comprised of a reservation identifier, followed by a space, and then the number of seats requested. The reservation identifier will have the format: R####.
Example: 
R001 2 
R002 4 
R003 4 
R004 3

Output: 

The program should output a file containing the seating assignments for each request. Each row in the file should include the reservation number followed by a space, and then a comma-delimited list of the assigned seats.
Example: 
R001 I1,I2
R002 F16,F17,F18,F19 
R003 A1,A2,A3,A4 
R004 J4,J5,J6

Please Note: The reservations that could not be accomodated in the theatre have 0 seats. 
example: R005 0 represents the reservation cannot be fullfilled at this time.

Approach to solution: 

This problem is a type of Constraint sattisfaction problem in which set of objects whose state must satisfy a number of constraints or limitations. CSPs represent the entities in a problem as a homogeneous collection of finite constraints over variables, which is solved by constraint satisfaction methods. These kind of problems have high complexity and generally cannot be solved in polynomial time thus making them a part of NP Hard problems. 

Why the problem is a CSP: 

Formally as stated in wiki a CSP is: 
Formally, a constraint satisfaction problem is defined as a triple <X,D,C> where
X={X1,,,,,,Xn} is a set of variables,
D={D1,,,,,,Dn} is a set of the respective domains of values, and
C={C1,,,,,,Cm} is a set of constraints.
Each variable X can take on the values in the nonempty domain D. Every constraint in C is in turn a pair <Ti,Ri> , where Ti belongs to X is a subset of k variables and R is a  k-ary relation on the corresponding subset of domains Di. An evaluation of the variables is a function from a subset of variables to a particular set of values in the corresponding subset of domains. An evaluation v satisfies a constraint  if the values assigned to the variable satisfies the relation.[1]


Assumptions made while implementing the Algorithm:

1. Cost of all the seats in the theatre are same. 
2. Seats are reserved on the First come first serve basis. 
3. Customers who reserves the seat first are offered better seats(seats that are far from the screen) than the customers who are reserve later. 
4. When no row is empty and only vacant seats need to be full filled reservation that suits the both sattisfaction are selected first.  
5. After the theatre has few vacant seats the Groups are splitted to adjust in the vacant seats. 
6. Every booking wants to get the seats even if the seats allocated are in seperate rows. 

Approach to the implement the solution: 

 1. Algorithm uses Greedy approach with Priority Queue implemented using Linked List.
 2. Each Row is considered as a node and has the following attributes: name, totalSeats, pointer to next node,seatsOccupied       and seatsEmpty
 3. New rows(I,H,G....A) are added when the seats to be reserved are greater than continguous seats empty in the Linked List. 
    If seats in J are smaller than the seats requested a new node with name I is added to the linked list.
 3. If the row is Full, it is removed from the List and replaced with next row. Example if J is full it was deleted from the       tree and I becomes the node.
 4. Program exits if the all the rows(nodes) are full or cannot accomodate the rest of the reservation with the vacant seats. 
 
 Why Using Greedy Approach than Backtracking: 
 1. This problem can also be solved using backtracking but backtracking may compromise customer sattisfaction due to high         constraint enforced. The complexity for solving the problem backtracking grows with increasing nodes in the tree. 
 2. In the worst case where each reservation would require 200 calculations which would only happen if 200 reservation             requests are recieved each with 1 seat.
 3. Linked list helps in easy insertion and deletion as compared to lists. 
 
 Scope of improvement: 
 1. Linked List can be replaced by Binary Search Tree where the root node is always the Last Row with Empty Seats. It will help to reduce the search time through the nodes. 
 2. Rather than allocating every reservation the best seats on First Come First Serve basis algorithm can use threshold for each reservation such that it meets Customer Sattisfaction and Theatre Utilisation. 
 3. Bulk seat booking reservation(>=100)will be given more priority than small bookings. 
 
 Program Files: 
 1. InputFileMaker.py: Uses random library to generate random reservation requests.
 2. InputFileParser.py: Parse the given input file of above format into list of reservations
 3. greedySeatAllocation: Uses greedy approach to allocate seats.

 
 How to run the program: 
 1. Open Command prompt or terminal. 
 2. Move to the directory where the program is stored. Make sure all the program files are in the same folder before running the program.
 3. The program accepts only text files of the format where each line in the file will be comprised of a reservation identifier, followed by a space, and then the number of seats requested. The reservation identifier will have the format: R####. as displayed above. 
 3. Type the following command in the  Command Prompt or Terminal. 
            python greedySeatAllocation.py *inputFilePath*
4. It takes input file path as system arrgument. 
5. The output generated is a text file, Each row in the file should include the reservation number followed by a space, and then a comma-delimited list of the assigned seats.
6. Program also generate the debug logs for event logging. 

 
 
 
 
 
 
