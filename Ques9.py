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