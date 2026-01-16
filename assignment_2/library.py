
#Library charges the fine if the book is returned late
#First five days → 10 rupees per day
#if(days>=1 and days<5)
#6 -10 days → 20 rupees per day
#if(days>=6 and days<10)
#Above 10 days → 50 rupees per days
#Calculate and display total fine to be paid






n=int(input("How many Days you want Book="))

if(n>=1 and n<=5):
    a=n*10
    print("Your Total Fien is =",a)
elif(n>=6 and n<=10):
    b=n*20
    print("Your Total Fine is =",b)
elif(n>10):
    c=n*50
    print("Your Total Fine is =",c)
elif(n==0):
    print("No Fine")





