import sqlite3
import random


db = sqlite3.connect("information.db")
db.execute("DROP TABLE Admin")
db.commit()
db.row_factory = sqlite3.Row
db.execute("create table if not exists Admin(Internet text,age text,employee_number int)")


while True:
    Internet=input("enter your Internet:" )
    age=input("enter your age:" )
    print(type(Internet),type(age))#string object
    db.execute(
    "insert into Admin(Internet,age,employee_number) values(?,?,?)",
    (Internet, age, random.randint(0, 999))
    )
    print("any more:y/n")
    if input() == 'n' :
        break;
    
    
# db.execute(
    # "insert into Admin(Internet,age,employee_number) values(?,?,?)", ("Tony", "86", 77)
# )

# cusror = db.execute("select * from Admin where Internet = 'Mark' ")

# for row in cusror:
    # print(*row, sep="\t")


# curs = db.cursor()
# curs.execute("SELECT * FROM Admin where Internet = 'Tony' ")

# for row in curs:
    # print(*row, sep="\t")
    # print("\nAnother type of output\n")
    # print(f"{row['Internet'],row['Age']}")
    


cursor = db.execute("SELECT rowid, * FROM Admin ORDER BY rowid")
print("\nHere is a listing of the rows in the table\n")
for row in cursor:
    print(*row, sep="\t")

print(type(cursor))
#<class 'sqlite3.Cursor'>

print(type(row))
#<class 'sqlite3.Row'>

db.commit()
cursor.close()
