# first step open windows command prompt and enter this line "pip install mysql-connector-python"
import mysql.connector

# Step 1: Connect to MySQL

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    
print("MySQL connection successful!",db.is_connected())




cur = db.cursor()

# Step 2: Check if Sample_DB already exists

#cur.execute("CREATE DATABASE Sample_DB")
print("Sample_DB database created successfully.")

# Step 3: Select Sample_DB
cur.execute("USE Sample_DB")



# Step 4: Create EMPLOYEE table
cur.execute("""
    CREATE TABLE  EMPLOYEE (
        eid INT PRIMARY KEY,
        name VARCHAR(50),
        sal FLOAT
    )
""")

print("EMPLOYEE table is ready.")


# Step 5: Insert records
records = [
    (101, "Sandeep", 25000),
    (102, "Suhani", 30000),
    (103, "krima", 28000),
    (104, "Priya", 35000)
]

cur.executemany(
    "INSERT  INTO EMPLOYEE (eid, name, sal) VALUES (%s, %s, %s)",
    records
)

db.commit()
print("Records inserted successfully.")


# Step 6: Display all records
print("\nEMPLOYEE TABLE RECORDS:")
print("--------------------------------")

cur.execute("SELECT * FROM EMPLOYEE")

r=cur.fetchall()
print(r)


# Step 7: Close connection
cur.close()
db.close()

print("\nMySQL connection closed.")
