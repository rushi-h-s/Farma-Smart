import mysql.connector
try:
    con =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="Raj@9104",
        database="pharmacy",
        port=3306
        # UseSSL=false
    )
    cursor=con.cursor()
    cursor.execute("SELECT * FROM appuser WHERE userRole='Admin'")
    res=cursor.fetchall()
    print(res)
    print("Connection Successful!!")
except mysql.connector.Error as e:
    print(e)
