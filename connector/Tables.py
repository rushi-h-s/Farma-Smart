from mysql.connector import Error
from tkinter import messagebox
from ConnectionProvider import ConnectionProvider

class Tables:
    def __init__(self):
        self.create_tables()

    def create_tables(self):
        try:
            # Initialize connection provider and establish connection
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            # Create appuser table
            #cursor.execute("CREATE TABLE IF NOT EXISTS appuser (appuser_pk INT AUTO_INCREMENT PRIMARY KEY, userRole VARCHAR(200), name VARCHAR(200), doj DATE, mobileNumber VARCHAR(50), emailid VARCHAR(100), username VARCHAR(200), password VARCHAR(50), salary VARCHAR(50))")

            # Insert a sample user
            #cursor.execute("INSERT INTO appuser (userRole, name, doj, mobileNumber, emailid, username, password, salary) VALUES ('Admin', 'Divesh', '2020-06-06', '7507441435', 'diveshpatil9104@gmail.com', 'divesh', '123456', '15000')")

            # Create supplier table
            #cursor.execute("CREATE TABLE IF NOT EXISTS supplier (Id INT PRIMARY KEY, supplierName VARCHAR(100), mobileNumber VARCHAR(15), address VARCHAR(100))")

            # Create stock table
            #cursor.execute("CREATE TABLE IF NOT EXISTS stock (stock_id INT AUTO_INCREMENT PRIMARY KEY, Id INT, medicineName VARCHAR(50), supplierName VARCHAR(50), dom DATE, doe DATE, purchaseDate DATE, category VARCHAR(100), quantity INT, price FLOAT, totalPrice FLOAT GENERATED ALWAYS AS (quantity * price) STORED)")

            # Create inventory table
            #cursor.execute("CREATE TABLE IF NOT EXISTS inventory (stock_id INT, Id INT, medicineName VARCHAR(100), dom DATE, doe DATE, quantity INT, price FLOAT, totalPrice FLOAT, category VARCHAR(100), FOREIGN KEY (stock_id) REFERENCES stock(stock_id))")

            # Create bill table
            #cursor.execute("CREATE TABLE IF NOT EXISTS bill (bill INT AUTO_INCREMENT PRIMARY KEY, bill_id VARCHAR(200), billdate DATE, totalamount FLOAT)")

            # Create customer table
            #cursor.execute("CREATE TABLE IF NOT EXISTS customer (billid VARCHAR(200), bill_date DATE, cname VARCHAR(100), mobile VARCHAR(50), mname VARCHAR(100), qty INT, pr FLOAT, tamt FLOAT, dct FLOAT)")

            # Create selling table with a check constraint
            #cursor.execute("CREATE TABLE IF NOT EXISTS selling (name VARCHAR(50), quantity INT, saledate DATE)")
            # Create trigger for enforcing the month and year restriction on saledate
            # cursor.execute("""
            #                CREATE TRIGGER check_saledate BEFORE INSERT ON selling
            #                FOR EACH ROW
            #                BEGIN
            #                    DECLARE cur_month INT;
            #                    DECLARE cur_year INT;
            #                    SET cur_month = MONTH(CURRENT_DATE());
            #                    SET cur_year = YEAR(CURRENT_DATE());
            #                    IF MONTH(NEW.saledate) != cur_month OR YEAR(NEW.saledate) != cur_year THEN
            #                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Sale date must be within the current month and year';
            #                    END IF;
            #                END
            #            """)
            # Create an event to delete old sales data monthly
            #cursor.execute("CREATE EVENT IF NOT EXISTS delete_old_data ON SCHEDULE EVERY 1 MONTH DO DELETE FROM selling WHERE MONTH(saledate) != MONTH(CURRENT_DATE()) OR YEAR(saledate) != YEAR(CURRENT_DATE())")
            # Create sales table
            #cursor.execute("CREATE TABLE IF NOT EXISTS sales (id INT AUTO_INCREMENT PRIMARY KEY, month INT, year INT, revenue FLOAT DEFAULT 0, expense FLOAT DEFAULT 0, profit FLOAT DEFAULT 0)")
            #cursor.execute("CREATE TABLE IF NOT EXISTS contact_submissions (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, phone VARCHAR(20) NOT NULL, message TEXT NOT NULL)")

            # Commit the changes
            con.commit()

            # Show success message
            messagebox.showinfo("Success", "Tables Created Successfully")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            # Close cursor and connection
            if cursor:
                cursor.close()
            if con and con.is_connected():
                con.close()

if __name__ == "__main__":
    Tables()
