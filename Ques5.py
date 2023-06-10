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
