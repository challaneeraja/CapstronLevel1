import sqlite3
connect=sqlite3.connect('c:/sqlite/hcl.db')
cur=connect.cursor()
sql="""insert into filelog1 values(?,?);"""
data=(100,'c:/neeru/file.html')
cur.execute(sql,data)
connect.commit()
cur.execute("Select * from filelog1")
rows=cur.fetchall()
for r in rows:
    print(r)