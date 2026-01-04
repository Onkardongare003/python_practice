
# i=100
# while(i>=1):
#     print(i)
#     i=i-1


n = int(input("Enter the Number for Factorial: "))
f = 1
i = 1

while(i <= n):
    f = f * i   # Multiply current total by the counter
    i = i + 1   # Move to the next number

print("The Factorial is", f)