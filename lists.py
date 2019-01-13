#Fourth Assignment

#Declaring an Empty Lists
myUniquelist=[]
myLeftovers=[]

#Defining a function for handling the new and duplicate values
'''If True that means the value was inserted or else the duplicate value is
inserted in the leftover lists'''
def add1(num):
    global myUniquelist
    global myLeftovers
    if num in myUniquelist:
        myLeftovers.append(num)
        return False
    else:
        myUniquelist.append(num)
        return True

#First Data Inserted
print("-------------Inserting New Value---------------------------")
a="80"
result=add1(a)
print(myUniquelist)
print(myLeftovers)
print(result)

#Second Data
a="050"
result=add1(a)
print("-------------Inserting New Value--------------------")
print(myUniquelist)
print(myLeftovers)
print(result)

#Third Data
a="050"
result=add1(a)
print("------------Inserting Duplicate Value----------------------------")
print(myUniquelist)
print(myLeftovers)
print(result)

#Fourth Data
a="Hello World"
result=add1(a)
print("-------------Inserting New Value-----------------------")
print(myUniquelist)
print(myLeftovers)
print(result)

#Fifth Data
a=66
result=add1(a)
print("-------------Inserting New Value-----------------------")
print(myUniquelist)
print(myLeftovers)
print(result)

#Sixth Data
a=66
result=add1(a)
print("-------------Inserting Duplicate Value-----------------------")
print(myUniquelist)
print(myLeftovers)
print(result)
