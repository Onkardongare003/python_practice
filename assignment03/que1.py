   
# Calculate the simple interest 

# duration
# Senior citizen roi
# General citizen
# 0 to 2 years # 2 to 4 years
# 3.5%
# 2.5%
# 2.5%
# 1.5%
# 2 to 4 years
# 3.5%
# 2.5%
# 4 to 6 years
# 4.5%
# 3.5%
# Above 6 years
# 5%
# 4%
# Senior citizen is having age>=60
# General citizen is having age<60

p=int(input("Enter how many Money you want ="))
age=int(input("Enter your age ="))
time=int(input("Enter How many year you want ="))

if(age>=60):
    if(time<=0 and time>=2):
        r=2.5
    elif(time<=2 and time>=4):
        r=3.5
    elif(time<=4 and time>=6):
        r=4.5
    else:
        r=5
else:
    if(time<=0 and time>=2):
        r=1.5
    elif(time<=2 and time>=4):
        r=2.5
    elif(time<=4 and time>=6):
        r=3.5
    else:
        r=4

si=(p*r*time)/100

print("Rate of Intresent is =",r)
print("Simple intresent is ", si    )
    









  






