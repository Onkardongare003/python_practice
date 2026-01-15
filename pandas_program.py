# #series = one 1d one row data
# dataframe = 2d table(inlcude row and table)

#series 
# import pandas
# s=pandas.sroe([10,20,30,40,50,60,70,80,80,90,100])
# print(s)


#DataFrame 2d data

import pandas
data={
    "name":["onkar","kiran","ganesh","siddhika"],
    "age":[10,20,30,40],
    "city":["ahhilyanager","nashik","pune","Mumbai"],
    "Mobile Number":[123,456,789,12312312]
}
df=pandas.DataFrame(data)
print(df)


