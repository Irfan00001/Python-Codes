# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 18:24:20 2019

@author: Aakash Jha
"""
stages = ["________       ",
         "|        |      ",
         "|        |      ",
         "|        0      ",
         "|       /|\     ",
         "|       / \     "
          ]

player=1
name=input("Enter the word to guess: ")

print(chr(27) + "[2J")
Length=len(name)
List=['_']*Length
print(List)
player=2
i=1
j=0
count=0
Bool=False
for x in stages:
    while(True):
        char=input("Enter the character of the name entered by player 1: ")
        print("char and name j",name[j])
        if(char==name[j]):
            List[j]=char
            print(List)
            j+=1
            i+=1
            Length2=len(List[0:j])
            print(Length2)
            if(Length==Length2):
               break

        else:
            count+=1
            for i in range(0, count):
                print(stages[i])
                print("\n")
            break
    if(count>=6):
        print("Player 2 loses")
        break
    for y in range(0, Length):
        if (name[y] == List[y]):
            Bool = True
        else:
            Bool = False
    if (Bool == True):
       print("Player 2 wins")
