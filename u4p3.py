import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sample_DB"
)

print("MySQL connection successful!", db.is_connected())

cur = db.cursor()

# Accept employee ID
eid = int(input("Enter Employee ID: "))

# Delete employee
cur.execute(
    "DELETE FROM EMPLOYEE WHERE eid = %s",
    (eid,)
)

db.commit()

cur.execute("SELECT * FROM EMPLOYEE")
r=cur.fetchall()


print("record is deleted.")
print(r)
# Close connection
cur.close()
db.close()


