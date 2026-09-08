import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sample_DB"
)

print("MySQL connection successful!", db.is_connected())

cur = db.cursor()

eid = int(input("Enter Employee ID: "))

cur.execute(
    "UPDATE EMPLOYEE SET sal = sal + 5000 WHERE eid = %s",
    (eid,)
)

db.commit()



cur.execute("SELECT * FROM EMPLOYEE WHERE eid = %s", (eid,))

r = cur.fetchone()


print("Updated Employee Record:", r)

cur.close()
db.close()
