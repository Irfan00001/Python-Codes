#Basic Loops
"""Created a For Loop in which testing if the number is Divisible
by 3 or 5 or a prime Number"""

for x in range(1,101,1):
    if x%3==0 and x%5==0:
        x="fizzbuzzz"
    elif x%3==0:
        x="fizz"
    elif x%5==0:
        x="buzz"
    elif x%2!=0:
        x="Prime"

    print(x)
