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
