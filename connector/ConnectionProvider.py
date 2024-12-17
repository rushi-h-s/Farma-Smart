import mysql.connector

class ConnectionProvider:
    def get_con(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Raj@9104",
                database="pharmacy",
                port=3306
                # UseSSL=false
            )
            print("Connection Successful!!")
            return con
        except mysql.connector.Error as e:
            print(e)
            return None
