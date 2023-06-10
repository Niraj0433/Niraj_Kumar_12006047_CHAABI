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
