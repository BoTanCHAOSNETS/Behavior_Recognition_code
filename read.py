text_file= open("rawdata.txt", "r")  #the name of reading file
lines=text_file.readlines()
print("Total number of lines")
print(len(lines))
#initial settings: user wants to read data (Y=Yes), the right and the left bounds of reading segment a and b 
ans='Y'
a=0
b=0
while (ans=='Y'):       #read until a user press any other key
    number=int(input("Put the number of lines to read:\n"))
    while (number<=0) or (number>len(lines)):     #check the number is in range or not
        print("Error! The number is out of range. Please try again\n")
        number=int(input("Put the number of lines to read:\n"))
    b+=number
    for i in range(a,b):
        print(lines[i])
    a=b    
    ans=input("Do you want to continue the reading?[Y, N]\n")
    if (ans!='Y'):
        break
text_file.close()
