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
Each variable X can take on the values in the nonempty domain D. Every constraint in C is in turn a pair <Ti,Ri> , where Ti belongs to X is a subset of k variables and R is a  k-ary relation on the corresponding subset of domains Di. An evaluation of the variables is a function from a subset of variables to a particular set of values in the corresponding subset of domains. An evaluation v satisfies a constraint  if the values assigned to the variables {\displaystyle t_{j}} t_{j} satisfies the relation {\displaystyle R_{j}} R_{j}.


#Assumptions made while implementing the Algorithm:
1. Cost of all the seats in the theatre are same. 
2. Seats are reserved on the First come first serve basis. 
3. Customers who reserves the seat first are offeredn better seats(seats that are far from the screen) than the customers who are reserve later. 
4. Bookings greater than 20 will always be in multiple of 2. 
