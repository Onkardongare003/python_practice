import mysql.connector
db=mysql.connector.connect(
    host="localhost"
    user="root"
    password="onkar"
    database="siddhika"
)

mycursor=db.cursor()
id=int(input("Enter the your id = "))
salary=int(input("Enter Your Salary = "))
age=int(input("Enter the Your age = "))
address=input("Enter your address = ")
eduacation=int(input("Enter your address = "))


s="insert into sidd(empid,empsalary,empage,empaddress,empeduaction) values(%s,%s,%s,%s,%s)"
v=(id,salary,age,address,eduacation)

