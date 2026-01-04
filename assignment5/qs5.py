
# Print the following series
# ½ + ¼ + ⅙ + ⅛ + ……1/n 


n=int(input("Enter the Number = "))
s=0
i=1
while(i<=n):
    s=s+(1/n)
    s=s+2
print("the seris will be = ",s)