#this is the Question 11 of the Backend assignment given by CHAABi in which we have to find the op of the given code 
def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
#the whole explantion is done just below please read it. It might look huge but its simple and easy to understand
f(2)  ---> [0,1]
f(3,[3,2,1]) ---> [3,2,1,0,1,4]
f(3) ---> [0,1,0,1,4]

'''ANS-->>:'''
#here the the function named f is called three time each time pasing different values teh op or changes will be as follows
#the op will be a 1D list of [0,1] in which the function is called with x=2 and the argument l is not given
#rather than giving the array it will use the default value that is provided to us i.e [] the loop runs for values 0 and 1
#and appending there squares in the list it will be become [0]-> [0,1] which will be printed after execution of the loop
#after that the function with val 3 and a list is passed this time the default list will not be used
# and again the loop executes for 0,1,2 to append the values 0,1,4 which are squares of the given no 
# now the last part comes in this is where the amgic will happend we will try to use default value of l as []
#but did we forgot that we updated the default value while our first function call so the op will be become 
#[0,1,0,1,4]
