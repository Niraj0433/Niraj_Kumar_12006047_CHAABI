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