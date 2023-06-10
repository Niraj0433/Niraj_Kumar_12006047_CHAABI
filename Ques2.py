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
