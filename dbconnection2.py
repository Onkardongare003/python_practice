# Step 1:
# Import the module
# Import mysql.connector
# Step2: 
# databaseobject=mysql.connector.connect(host=”localhost”,user=”root”,password=”root”,database=”databasename”_
# Step3 : 
# Create the cursor
# cursorobject=databaseobject.cursor()
# Step4 : 
# Write the query and also provide the values which are going to use in query
# Step 5: 
# Call the execute function
# cursorobject.execute(query,values)
# Step 6:
# Commit the changes
# databaseobjectname.commit()


import mysql.connector  
db=mysql.connector.connect(host="localhost",user="root",password="root",database="employee")


mycursor=db.cursor()


id=int(input("enter the id of the employee"))
name=input("enter the name of the employee")
salary=int(input("enter the salary of the employee"))
age=int(input("enter the age of the employee"))
address=input("enter the address of the employee")
s="insert into emp(empid,empname,empsalary,empage,empaddress)values(%s,%s,%s,%s,%s)"
v=(id,name,salary,age,address)


mycursor.execute(s,v)


db.commit()
