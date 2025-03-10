import os
import tkinter as tk
from tkinter import ttk, messagebox
from email.message import EmailMessage
import ssl
import smtplib
from  Ademp import  AdEmp
from sales import sales
from stock import stock
from inventory import InventoryApp
from connector.ConnectionProvider import ConnectionProvider
from PIL import Image, ImageTk
from BackgroundPage import BackgroundPage


class BackgroundPage:
    def __init__(self, root):
        self.root = root
        self.raw_image = Image.open("lb.jpg")
        self.raw_image = self.raw_image.resize((1400, 700))
        self.img = ImageTk.PhotoImage(self.raw_image)
        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)
        self.panel.image = self.img

class Admin:
    def __init__(self, root):

        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1400x700+50+50")
        BackgroundPage(root)

        # Create a frame for better organization
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=100)

        # Create buttons with better styling

        self.btn_admin_employee = tk.Button(self.frame, text="Admin & Employee", command=self.open_admin_employee, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_admin_employee.grid(row=0, column=2, pady=10)

        self.btn_supplier= tk.Button(self.frame, text="Supplier",command=self.open_supp,width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_supplier.grid(row=1, column=2, pady=10)

        self.btn_stocks = tk.Button(self.frame, text="Stocks", command=self.open_stocks, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_stocks.grid(row=2, column=2, pady=10)

        self.btn_inventory = tk.Button(self.frame, text="Inventory", command=self.open_inventory, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_inventory.grid(row=3, column=2, pady=10)

        self.btn_sales = tk.Button(self.frame, text="Sales", command=self.open_sales, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_sales.grid(row=4, column=2, pady=10)

        self.btn_bt = tk.Button(self.frame, text="Bill Records", command=self.open_bt, width=20, height=2, bg="#008CBA",
                                   fg="black", font=("Arial", 12, "bold"))
        self.btn_bt.grid(row=5, column=2, pady=10)

        self.btn_logout = tk.Button(self.frame, text="Logout", command=self.logout,width=20, height=2, bg="red", fg="black", font=("Arial", 12, "bold"))
        self.btn_logout.grid(row=6, column=2, pady=10)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Create the Treeview
        self.expiry_alert = ttk.Treeview(self.root)
        self.expiry_alert["columns"] = ("name", "doe", "quantity")
        self.expiry_alert.column("#0", width=0, stretch="NO")
        self.expiry_alert.column("name", anchor="center", width=150)
        self.expiry_alert.column("doe", anchor="center", width=150)
        self.expiry_alert.column("quantity", anchor="center", width=150)
        self.expiry_alert.heading("#0", text="index")
        self.expiry_alert.heading("name", text="Name")
        self.expiry_alert.heading("doe", text="Expiry date")
        self.expiry_alert.heading("quantity", text="Quantity")
        self.expiry_alert.place(x="60", y="100",height="550")

        # Set an attractive heading for the table
        self.heading_label = ttk.Label(self.root, text="Expiration Alert", font=("Helvetica", 14, "bold"))
        self.heading_label.place(x=210, y=50)

        self.low_stock = ttk.Treeview(self.root)
        self.low_stock["columns"] = (
            "name", "quantity")
        self.low_stock.column("#0", width=0, stretch="NO")
        self.low_stock.column("name", anchor="center", width=200)
        self.low_stock.column("quantity", anchor="center", width=200)
        self.low_stock.heading("#0", text="index")
        self.low_stock.heading("name", text="Name")
        self.low_stock.heading("quantity", text="Quantity")
        self.low_stock.place(x="900", y="100",height="550")

        self.heading_label = ttk.Label(self.root, text="Low Stock Alert", font=("Helvetica", 14, "bold"))
        self.heading_label.place(x="1090", y="50")
        self.expdata()
        self.lowdata()

    def logout(self):
        from Login import loginClass
        self.root.destroy()
        root=tk.Tk()
        loginClass(root)
        root.mainloop()

    def expdata(self):
        try:

            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            cursor.execute("SELECT medicineName,doe,quantity FROM stock WHERE doe BETWEEN CURRENT_DATE() AND DATE_ADD(CURRENT_DATE(), INTERVAL 30 DAY)")
            self.upexp = cursor.fetchall()
            for row in self.upexp:
                self.expiry_alert.insert("", tk.END, values=row)
            cursor.execute("SELECT medicineName,doe,quantity FROM stock WHERE doe <= CURRENT_DATE")
            self.expr=cursor.fetchall()
            self.expiry_alert.tag_configure('highlighted_row', background='red',foreground='white')
            for row in self.expr:
                id=self.expiry_alert.insert("",tk.END,values=row)
                self.expiry_alert.item(id,tags=("highlighted_row",))

            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def lowdata(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT medicineName,quantity FROM stock WHERE quantity<=100")
            self.lowStock = cursor.fetchall()
            for row in self.lowStock:
                self.low_stock.insert("", tk.END, values=row)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT emailid FROM appuser WHERE userRole='Admin'")
            email=cursor.fetchall()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",f"An error occurred: {str(e)}")
        print("hello")

        for em in email:
            receiver=em[0]
            try:
                # Email configuration
                sender_email = "divesh.patil@ssvpsengg.ac.in"
                receiver_email =receiver
                password = "smnp ukhw lmfs anov"
                subject = "Alerts"
                body = "Upcomming expirations :\n"
                for entry in self.upexp:
                    body += f"Medicine Name: {entry[0]}, Date of Expiry: {entry[1]}, Quantity: {entry[2]}\n"

                body += "\nExpired Medicines:\n"
                for entry in self.expr:
                    body += f"Medicine Name: {entry[0]}, Date of Expiry: {entry[1]}, Quantity: {entry[2]}\n"

                body += "\nLow Stocks:\n"
                for entry in self.lowStock:
                    body += f"Medicine Name: {entry[0]}, Quantity: {entry[1]}\n"

                # Create a multipart message
                em = EmailMessage()
                em["From"] = sender_email
                em["To"] = receiver_email
                em["Subject"] = subject

                # Add body to email
                em.set_content(body)

                # Establish a connection to the SMTP server
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                    smtp.login(sender_email, password)

                    # Send the email
                    smtp.sendmail(sender_email, receiver_email, em.as_string())

                # Quit the SMTP server

                print("Email sent successfully")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    def open_admin_employee(self):
        # Define functionality for opening admin and employee window
        self.root.destroy()
        root=tk.Tk()
        app=AdEmp(root)
        root.mainloop()

    def open_stocks(self):
        # Define functionality for opening stocks window
        self.root.destroy()
        root=tk.Tk()
        stock(root)
        root.mainloop()

    def open_inventory(self):
        # Define functionality for opening inventory window
        self.root.destroy()
        root=tk.Tk()
        InventoryApp(root)
        root.mainloop()

    def open_sales(self):
        # Define functionality for opening sales window
        self.root.destroy()
        root=tk.Tk()
        sales(root)
        root.mainloop()

    def open_bt(self):
        self.root.destroy()
        os.system("python Billing.py")

    def open_supp(self):
        self.root.destroy()
        os.system("python supplier.py")

def main():
    root = tk.Tk()
    app = Admin(root)
    root.mainloop()

if __name__ == "__main__":
    main()
