# Iterate for loop from 1 to 100
# Multiple of 3 then  print “Fizz”
# Multiple of 5 then print “Buzz”
# Multiple of 3 and 5 print “FizzBuzz”

# i = 1

# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
    
#     i = i + 1


i=1
while(i<=100):
    if(i%3==0 and i%5==0):
          print("FizzBuzz")
    elif(i%3==0):
         print("Fizz")
    elif(i%5==0):
         print("Buzz")
    else:
         print(i)
    i=i+1