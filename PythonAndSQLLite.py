import sqlite3

try:

    db = sqlite3.connect("InternetWebsites.db")
    cursorx= db.execute("select * from Adkkkmin")
    print(type(cursorx))#<class 'sqlite3.Cursor'>
    #fetch 1st row-singleton tuple
    print(cursorx.fetchone())
   
    #fetch 2nd row
    print(cursorx.fetchone())
    
    #fetch from 3d row to the 5th row
    print(cursorx.fetchmany(3))   
   
    #fetch 5th row to the last row
    print(cursorx.fetchall())
    
   
    print("--------try printing out remaining rows...no output")
    for row in cursorx: 
        print(*row, sep="\t")#no output
    
    
    print(">>>>>>>>reinitialise cursor so as to point to top of table")
    
    cursorx= db.execute("select * from Admin")
    print(cursorx.fetchall())
    

except sqlite3.OperationalError as e:
    print(f"Oops!  That was no Tablecalled {e}")
    print("Oops!  That was no Tablecalled {}".format(e))

db.execute("create table if not exists Admin(InternetWebsites text)")
print(type(db))
#<class 'sqlite3.Connection'>

while True:
    InternetWebsites=input("enter your InternetWebsites:" )
    print(type(InternetWebsites))#<class 'str'>

    db.execute("insert into Admin(InternetWebsites) values(?)",[InternetWebsites])
    print("any more,yes/no:" , end=' ' )# default line terminator new line but now with end variable its a space
    if input() == 'no' :
        break;
     

db.commit()


for row in (db.execute("select * from Admin ")):
    print(*row, sep="\t")
    
