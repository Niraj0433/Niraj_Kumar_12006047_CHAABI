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










