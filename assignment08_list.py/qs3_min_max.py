# list=[12,23,34,45,54,43,32,21,]






numbers = [12, 23, 34, 45, 54, 43, 32, 21]
b = int(input("Enter the Number : "))

if b ==min(numbers):
    print("Number is Minimum")
elif b > min(numbers):
    print("Number is Maximum")
else:
    print("Null")