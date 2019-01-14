## Assignment 8
"""FileName is test.txt"""

filename=input("Enter the File Name : ")
if filename=="test.txt":
    action=input("For Reading:r For Start Over:w For Appending:a  For Replace:replace: ")
    if action=="r":
        outputfile=open(filename,action)
        print(outputfile.read())
        outputfile.close()
    if action=="a":
        datatoappend=input("Enter the data to append : ")
        outputfile=open(filename,"a")
        outputfile.write(datatoappend)
        outputfile.close()
        outputfile=open(filename,"a")
        outputfile.write("\n")
        outputfile.close()
    if action=="w":
        datatoappend=input("Enter the data to Write : ")
        outputfile=open(filename,"w")
        outputfile.write(datatoappend)
        outputfile.write("\n")
        outputfile.close()
    if action=="replace":
        lineno=int(input("Enter the Line no to append : "))
        afterReplace=input("Enter the Data to be replace with :")
        count=0
        outputfile=open(filename,"r+")
        lineread=outputfile.readlines()

        data1=lineread[lineno]
        for line in lineread:
            if count==lineno:
                print("Total No of COunts",count)
                data1=lineread[lineno]=afterReplace
                outputfile=open(filename,"w")
                outputfile.writelines(data1)
                break
            else:
                count+=1
            #print(line)
        #print(lineread)
        outputfile.close()

else:

    data=input("Please Add data to the file")
    outputfile=open(filename,"w")
    outputfile.write(data)
    outputfile.close()
