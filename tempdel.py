#!/Python27/python.exe
print"content-type:text/html\n\r"
import MySQLdb
import cgi
db=MySQLdb.connect("127.0.0.1","root","root","project1",3306)
mycursor=db.cursor()
delete="delete from temp"
mycursor.execute(delete)
db.commit()
print"<script language=javascript>location.href='index.py';</script>"
