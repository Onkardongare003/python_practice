#Writte a program to read subject marks sub calculate percenrage


#Read marks of three subjects and calculate their percentage
#per>=75 → distinction
#per>=50 and per<75 → first class
#Per >=45 and per<50 → second class
#Else → fail



m1=float(input("Enter the M1 marks:"))
m2=float(input("Enter the M2 marks:"))
m3=float(input("Enter the M3 marks:"))

percentage=m1+m2+m3/3

if(percentage>=75):
    print("Distinction")
elif(percentage>50 and percentage<=75):
    print("Frist Class")
elif(percentage>=45 and percentage>=50):
    print("Second Class")
else:
    print("fail")  
