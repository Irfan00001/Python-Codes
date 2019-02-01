#Function for Songs
#Below are the functions created for each details as shown below
artist="Micheal"
album="They Don't Care About Us"
year="ISN"


def Artist():
    try:
        artistname=artist
    except:
        print("Not A String")
    return artistname

def Year():
    try:
        year=int(year)
    except Exception as e:
        print("Error Logged : ",e)


#Calling each function and storing it in a Variable for further use
artistname=Artist()
yearint=Year()


#Printing the data wich we get from the functionations
try:
    print(artistname)
    print(yearint)
    print(asdfepo)## Printing some Incorrect Data
except SyntaxError:
    print("SyntaxError")
except Exception as e:
    print("Something Wrong with the Print Code")
