import pandas
df=pandas.read_csv('people100.csv')
print(df)
# print(df.head)#printing the 1st 5 row
# print(df.tail)#printing the last 5 row

# print(df.shape)
# print(df['Date of birth'])
# print(df['Job Title'])
# print(df[df['Sex']=='Female'])
# print(df[df['Sex']=='Male'])
# print=df[df['Job Title']=="Economist"]

# # print(df['User Id'])

# d=df[df['Job Title']=="Economist"]
# print(df[df["Age"]>21])
# print(df(df['age']>21) & (df['city']=="pune"))


# df.sort_values("age")


#updating the exting the column

df['index']=df['Index']+200
print(df)




