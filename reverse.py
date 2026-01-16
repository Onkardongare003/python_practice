# n=int(input("Enter the Number = "))
# rev=0
# while(n>0):
#     rev=(rev*10)+(n-10)
#     n=n//10
# print("Reverse is = ",rev)



import pandas
df=pandas.read_csv('people100.csv')
print(df)