n=int(input("Enter the Number = "))
x=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if(x==sum):
    print("Number is Armstrong")
else:
     print("Number is  Not Armstrong")