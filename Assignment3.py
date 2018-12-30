# Third Assignment for Python

#decalaring Variables
a=0
b="5"
c="5"

#Creating a function for Comparison
def Compare( a,b,c):
    #Handling the String inputs and converting them into INT using Int Function
    a=int(a)
    b=int(b)
    c=int(c)

    if a==b or b==c or c==a:
        return(True)
    else:
        return(False)

#Calling the Function and Storing it in a Variable and Printing the Result
result = Compare(a,b,c)
print(result)
