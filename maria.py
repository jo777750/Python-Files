import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="ja",
        password="abcd1234",
        host="127.0.0.1",
        port=3306,
        database="univ"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    

# Get Cursor 
cur = conn.cursor()
print(type(cur))
print(type(conn))
    

#1st way to push variable to mariadb
# statement =  "INSERT INTO salaries (AMOUNT) VALUES(7023)"
# cur.execute(statement)

#2nd way to push variable to mariadb
ame=input("enter salary amount:")
cur.execute( "INSERT INTO salaries(AMOUNT) VALUES(?)",[ame])
#for single variables insertion, now change to (ame) as cur.execute( "INSERT INTO salaries(AMOUNT) VALUES(?)",(ame)), Error thrown ;IDK WHY??

gen=input("enter  gender:")
cur.execute( "INSERT INTO gender(sex) VALUES(?)",[gen])

#2nd way to push variable to mariadb
fname=input("enter fname:")
lname=input("enter lname:")
cur.execute( "INSERT INTO employees(fname,lname) VALUES(?,?)",(fname,lname))


print("display salaries table")
print("--------------------")
cur.execute("SELECT * FROM salaries")    
for row in cur:
    print(*row, sep="\t")
    
print("display employeess table")
print("--------------------")

cur.execute("SELECT * FROM employees")    
for row in cur:
    print(*row, sep="\t")
    
    
print("display gender table")
print("--------------------")
# from internet    
def get_data():
   cur.execute("SELECT * FROM gender")    
   for row in cur:
        print(*row, sep="\t")

get_data()
conn.commit()
conn.close()