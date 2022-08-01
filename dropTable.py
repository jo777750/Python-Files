import sqlite3
import os
z=os.getcwd()
print(z)



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)#<class 'str'>

print(type(BASE_DIR))#<class 'str'>
input1=input("enter DB filename for Conn String:" )
db_path = os.path.join(BASE_DIR, input1)
print (db_path)
#x="DROP TABLE " + z + "\\" + input2

db = sqlite3.connect("InternetWebsites.db")
chk=input('confirm y to drop table:')
if chk == "y":
    print("done")
    try:
        db.execute("DROP TABLE Admin")
    except sqlite3.OperationalError:
        print (r" Admin table doesnt exist")
        print("ok")

db.commit()
db.close()        