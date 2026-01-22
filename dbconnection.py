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
