#q1 for chaabi backend assigment This is selection sort which is implemented O(n^2) as we keep track of min element in each 
#iteration from i to N

def selectionSort(arr):
    
    for i in range(len(arr)):
        mi = i # min index defined as first index which will be updated further more
 
        for j in range(i+ 1, len(arr)):
            # the below if condition is to check whether the element is less or more than update or min indes
            if arr[j] < arr[mi]:
                mi = j
         # the minimum value's index which we get will be swapped with the ith position this will be repeated till the array is sorted
        (arr[i], arr[mi]) = (arr[mi], arr[i])
        
    
        
arr=list(map(int,input().strip().split()))
(selectionSort(arr))
print(arr)


# this is question 2 of the backend asigment given by CHAABI in which we are given extensiontype and some test
#that are to beb conducted to determine those types

def printfile(extensiontype, test):
    #we are seprating  the values so that we can create pairs of the them to add to ref_dic
    temp = [num.split(",") for num in extensiontype.split(";")]
    #here the ref_dic is created using the same temp array we build together
    ref_dic = {num[0]: num[1] for num in temp}
    #an empty dictionary as output which will be returned
    op = {}
    #we are iterating over each test case to cover them
    for n in test:
        if "." in n:
            #here we are seprating those to get the exact tracker
            extension = n.split(".")[-1]
            #here we are fetching if it exist in the dictionary otherwise will return unknown
            file_type = ref_dic.get(extension, "unknown")
        else:
            file_type = "unknown"
        #here we are matching the file_type with itself
        op[n] = file_type
    #op is returned
    return op

inputextension = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
test = ["abc.jpg", "xyz.xls", "text.csv", "123"]
#final_res stores the dictionary that we are going to ptibt after calling the fuction(not necessary) 
final_res = printfile(inputextension, test)
print(final_res)#simple print statement


# this is the third ques in CHAABI backend assignment in this the cols are sorted 
# on the basis if the key that we are provided before the function

# a simple function declarartion 
def columnsortingyay(list_of_dicts, rkey):
    # a lambda function is used to sort those given dicts on the key that we are provided
    # a lamda function is a short anonymou function with in expression
    to_be_returned = sorted(list_of_dicts, key=lambda x: x[rkey])
    return to_be_returned

# here is the list of fruits and colors it can be updated to perfrom desired operation you wissh of dict
list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

#this is a key value which can be changed accordingly
rkey = "fruit"
# this is just stored in a dictionary we can directly print it
sorted_list_of_dicts = columnsortingyay(list_of_dicts, rkey)
print(sorted_list_of_dicts)
# Done By Niraj Kumar(12006047)

#In this the fourth question of CHAABI's Backend assignment is done 
#in which we have to reverse the key value pair in the dictionary

def the_power_of_one_line(i_dict):
    #we simple iterated over each key value pair and stored it and returned it and 
    #did it as question demanded that i.e in on line
    return {value: key for key, value in dictionary.items()}

#here i created a simple imput function wghich takes key value pair as input in the format defined
i_dict_s = input("Enter the dictionary (in the format {'key1': 'value1', 'key2': 'value2', ...}): ")
#The eval() function is used to evaluate the input string and convert it into a dictionary
#note- that using eval() can be potentially unsafe sometimes
#accepting user input to avopid that we could consider using a safer 
#alternative like the ast.literal_eval() function if security is a concern.
i_dict = eval(i_dict_s)
#i stored it in final the return of the function But one can also direcytly print 
#bt putting it in the function
final = the_power_of_one_line(input_dict)
print(final)


# This is the question 5 of the Backend assignment given By CHAABI In which we have to
# tell the common and not common elements in the 2 lists the solution is as follows

# this is the function declaration in which i pass 2 lists in the functions 
def common_not_common(list1, list2):
    #here the 2 sets are crated for the elements comparison so that we can use inbuild intersection
    # and symmetric_difference to calculate or desired results
    set1 = set(list1)
    set2 = set(list2)
    #the common_elements will contain the intersection which is the common elements
    common_elements = list(set1.intersection(set2))
    #the non_common_elements will contain the symmetric_difference which is not common elements
    non_common_elements = list(set1.symmetric_difference(set2))
    #a simple return statement to the items which we have calculated
    return common_elements, non_common_elements

# here both the list are taken as input fro the user in which the the strip plit are used to convert them to int
list1 = list(map(int,input("Please Insert the elements of list 1:").strip().split()))
list2 = list(map(int,input("Please Insert the elements of list 2:").strip().split()))
#i again stored them instead of printing them as it will look more user friednly to sepcify what we 
# are printing
common, not_common = common_not_common(list1, list2)
print("Common elements:", common)
print("Not-common elements:", not_common)

#This is question 6 of CHAABI backend assignment in which i have to return the sublist 
#with a jump of indices is give

#this is just a function declaration in which we passed the array statrt and endpoint
def every_other_sublist(arr,start,end):
    #the result is intially empty we will keep appending our desired values in the following functions
    res=[]
    # a for loop in which start and end indices are defined and 2 is the jump of i+=2 is the job its doing
    for i in range(start,end,2):
        #we are appending in the result the desired val
        res.append(arr[i])
    #we are returning the res after we fill it with required elements
    return res

# the list  is taken as a input seprated by space and later starting and end point are also taken    
list_real=list(map(int,input("Please Insert the elements of list :").strip().split()))
start=int(input("Enter starting Point:"))
end=int(input("Enter End Point :"))
#here i directly printed the function without storing its return value
print(every_other_sublist(list_real,start,end))

# Done By Niraj Kumar 12006047

#This is the question 7 of the Backend assignment Given by CHAABI in which we 
#have to find the factorial of number using the lambda function

# A simple function declaration
def factorial(n):
    #this is where the real work is taking place where the user given argument is passed lambda is used
    res = lambda n: 1 if n == 0 else n * res(n-1)
    # here i directly returned the res(n) which is the op of just avove declared lambda function
    return res(n)
#lambda function is not that efficient we can use recursion for better performance    

#here the input is taken from the user
n = int(input("Enter a number: "))
#the res is stored this res is diiferent than the one used in the function
res = factorial(n)
#A user friendly print statement
print("Factorial of", n, "is", res)
# Submitted By Niraj Kumar (12006047)


#This is the question 8 of the Backend assignment Given by CHAABI in which we 
#have to tell the output of the several given inputs so lets beigin 

#the OP of A0 
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# its op willbe A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#in which the botch are combined as key value pairs zip function only keeps the element till the shorter
#one but there are ways to work around that also if we want to keep the longer elements also 

#the Op of A1 will be 
A1 = range(10)
#this will print the values from 0 to 9 as the 10 is not inclusive so we will exclude that
#the range function starts from 0 until we specify it (1,10)in this it will start from 1 we can also
#add jump by adding the third comma

#The op of A2 will be 
A2 = sorted([i for i in A1 if i in A0])
#the op will be [1,2,3,4,5]
#this will print the elements which are in A1 as well as A0 and the outer sorted func will sort them 

#the op of A3 will be 
A3 = sorted([A0[s] for s in A0])
#this will print [1,2,3,4,5]
# the s is actually a key which we are calling everytime or we could say that we are calling every key 
#that is there in A0 and printing there corresponding values which in this case are 1 2 3 4 5
# and after that we are sorting them aslo as in this case we already have sorted values so it will not make any diff

#the op of A4 will be
A4 = [i for i in A1 if i in A3]
#this again the intersection of the elements in this we are taking all the elements from A1 and checking them
#if they exists in A3 if they do we will print them else ignore them
#the res will be [1,2,3,4,5]

#the op of A5 will be 
A5 = {i: i*i for i in A1}
# this is a dictionary in which we are putting the values of A1 as key and there square as values
#so op will be A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#the op of A6 will be 
A6 = [[i, i*i] for i in A1]
#this is generally a 2D list which we also calls a list of list in which in every sublist we store the 
#the value at index 0 and and its square at index1 and we are iterating on each value of A1 which will give the op as
#A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

#the op of A7 will be 
A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
# this we will generally first calcluate the sum of 2 numbers and keeps on adding them
#first, it adds 10 and 23, resulting in 33.
#Then, it adds 33 and -45, resulting in -12.
#Finally, it adds -12 and 33, resulting in 21 which our output yayyyy!!!

#the op of A8 will be 
A8 = map(lambda x: x*2, [1, 2, 3, 4])
#this will change the values to their twice and will be ready to map them we have to use something like list to
#to store it as op which willl result in
#[2,4,6,8]

A9 = filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"])
#as the name flter suggests in this the strings which have length less than 3 will be processed out whereas
#the on with greater will move forawrd to the op 
#the values which will remain are - "want","learn","python"

#I guess thats it for this question see you in next one 





#This i sthe question 9 of the backend assignment given by CHAABI in which we have to find if the 
#given no of days lies in between the given no of days or not 

#A date and time library in python which can be used for datetime problems 
#like in c++ we could use time.h
from datetime import datetime, timedelta

#this is the declaration of the function in which we could use to solve
def date_difference(from_date, to_date, difference):
    # here the operation to convert those input string t0 something usable is done
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')

    # we calculate differnce of the dates if we care about streamlined flow
    #i.e to_date should be greater from_date we could use abs function
    diff = (to_date - from_date)

    # Check if the condition is met or not if it is met we returned True else we returned false
    if diff <= timedelta(days=difference):
        return True
    else:
        return False
        
#here the basic input is taken according to the question and move forward
from_date=input("Please Enter the intial/start date :")
to_date=input("Please Enter the Final/End date :")
difference=int(input("Please enter the number of target days or max difference allowed :"))
#here the return of the function is directly stores in the pritn function we could also store it
#before printing if we want to do any further operations on the date
print(date_difference(from_date,to_date,difference))




#this is the question 10 of the Backend Assignment given By CHAABI in this we have to take 2 inputs a date
#in yy-mm-dd format and a integer days and we have to return the date n days before the data that is given to us 

# here we imported the datetime library and basic tools from it which willl help us to solve the required problems

from datetime import datetime, timedelta
#here the declaration of the function is taking place in which we are passing the date and an integer 

def Of_date_and_days(date, n):
    # Here the conversion of date that  is given to us to a usable value 
    date = datetime.strptime(date, '%y-%m-%d')

    #the calculation of the date before the required no of days 
    before_date = date - timedelta(days=n)

    #here the conversion of the date that we calculated above we will calculate the exact date in string format
    before_date_str = before_date.strftime('%y-%m-%d')
    
    #returning of the function takes place our desired value yay!!
    return before_date_str
    
#here the input is taken with the right formats defined in the sattements to define the values

date=input("Enter the date from which the result is to be calculated in yy-mm-dd format:")
n=int(input("Enter the no of Days before which the date is to be calculated :"))
#here we directly print the values if we want to do any further operations we could store it into a variable and use it aheaf
print(Of_date_and_days(date,n))

#Done by Niraj Kumar(12006047)

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
