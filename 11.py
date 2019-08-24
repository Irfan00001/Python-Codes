Artist = "Shawn Mendes"
Genre = "Pop"
Year = 1998


def artist():
    try:
      print(str(Artist))
    except:
        print("Error occured")
    finally:
        print("Final statement")


def genre():
    try:
       print(int(Genre))
    except Exception as e:
        print("Value Error")
        print(str(e))

def year():
   try:
    print(int(Year))
   except:
       print("Value Error")

year()
genre()
artist()

#We can do the same thing with lists as well to check the index error as follows
a = [1, 2, 3]
try:
    print("Second element = ",a[1])

    # Will show in
    print("Fourth element =",a[3])

except IndexError:
    print("An Index error occurred")
