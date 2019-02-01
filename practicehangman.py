import os

hang=["----------",
    "|         |",
    "|         O",
    "|        /|/",
    "|         |",
    "|        / /"]

word=input("Please ask the user to enter the word : ")
length=len(word)
data=[(" ")]*(length)

print(data)
print
i=0
j=0
os.system('cls||clear')

while (True):
    guess=input("ask the user to guess the word : ")
    if guess==word[j]:
        data[j]=guess
        print(data)
        if (data[length-1]!=" "):
            print("You Won")
        j+=1
        continue
    else:

        i+=1
        for x in range(0,i):
            print(hang[x])
        if i>=6:
            print("You Loose")
            break
