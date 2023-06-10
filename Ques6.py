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