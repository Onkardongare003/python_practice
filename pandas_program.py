# #series = one 1d one row data
# dataframe = 2d table(inlcude row and table)

#series 
# import pandas
# s=pandas.sroe([10,20,30,40,50,60,70,80,80,90,100])
# print(s)


#DataFrame 2d data

import pandas
data = {
    "name": [
        "onkar", "kiran", "ganesh", "siddhika", "priya",
        "amit", "neha", "sachin", "pooja", "rohit"
    ],

    "age": [18, 20, 22, 21, 23, 19, 24, 20, 25, 22],

    "city": [
        "ahhilyanagar", "nashik", "pune", "mumbai", "nagpur",
        "kolhapur", "satara", "solapur", "aurangabad", "jalgaon"
    ],

    "Mobile Number": [
        "9876543210", "9123456789", "9988776655", "9000011111", "9555566666",
        "9888899999", "9012345678", "9090909090", "9111122222", "9333344444"
    ],

    "email": [
        "onkar@gmail.com", "kiran@gmail.com", "ganesh@gmail.com", "siddhi@gmail.com", "priya@gmail.com",
        "amit@gmail.com", "neha@gmail.com", "sachin@gmail.com", "pooja@gmail.com", "rohit@gmail.com"
    ],

    "course": [
        "Data Science", "Python", "Java", "Web Dev", "AI",
        "ML", "Cloud", "Cyber Security", "DevOps", "Blockchain"
    ],

    "fees_paid": [25000, 20000, 22000, 24000, 26000, 21000, 27000, 23000, 28000, 22500]
}

df=pandas.DataFrame(data)
print(df)

<<<<<<< HEAD
=======

>>>>>>> a8b4637ef7456e34876af8a9561572a6de40be96
