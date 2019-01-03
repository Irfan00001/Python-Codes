
# | |
#-----
# | |
#-----
# | |

# | | |

#Assignment 6
"""In My Case only Even Number are able to form a proper TIC TAC TOE Box
Please correct me if i am doing wrong
I am finding it difficult to understand this program.
"""
def draw(rows,columns):
    for r in range(rows):
        if r%2==0:
            for c in range(columns+1):
                if c%2==0:
                    if c==columns:
                        print(" ")

                    else:
                        print(" ",end="")

                else:
                    print("|",end="")

        else:
            print("-----")

a=6
b=8

if (a%2==0 and b%2==0):
    draw (4,8)
else:
    print("Please Enter an Even Numbers")
