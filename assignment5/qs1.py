
# 121 → 121
# Check whether the number is palindrome or not

# 123→ 321 (not palindrome)
# 777 → 777 (palindrome)

n=int(input("Enter the Number = "))
x=n
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
if(x==rev):
        print("Number is Plaindrome")
else:
    print("Number is Not palimdrome")
