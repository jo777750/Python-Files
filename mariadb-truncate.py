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
	
cur=conn.cursor()    
cur.execute("TRUNCATE gender")    
cur.execute("TRUNCATE employees")    
cur.execute("TRUNCATE salaries")    

conn.commit()
conn.close()