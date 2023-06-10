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
