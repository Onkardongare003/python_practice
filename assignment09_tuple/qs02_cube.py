# # Print every 3rd element raised to the power 3

# n=int(input("Enter the Number = "))
# for i in range(1,n**3,1):
#      print(i**3)


n = int(input("Enter the Number = "))

t = (n,)

print(t[0] ** 3)
