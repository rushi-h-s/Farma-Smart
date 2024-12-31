import os
import tkinter as tk
from tkinter import ttk, messagebox

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

class Empdash:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1400x700+70+60")
        BackgroundPage(root)

        # Create a frame for better organization
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=100)

        # Create buttons with better styling
        self.btn_inventory = tk.Button(self.frame, text="Inventory", command=self.open_inventory, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_inventory.grid(row=4, column=1, pady=10)

        self.btn_cart = tk.Button(self.frame, text="Cart", command=self.open_cart, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_cart.grid(row=5, column=1, pady=10)

        self.btn_return= tk.Button(self.frame, text="Return", command=self.open_return, width=20, height=2, bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_return.grid(row=6, column=1, pady=10)

        self.btn_bt= tk.Button(self.frame, text="Bill Records", command=self.open_bt, width=20, height=2,bg="#008CBA", fg="black", font=("Arial", 12, "bold"))
        self.btn_bt.grid(row=8, column=1, pady=10)

        self.btn_log = tk.Button(self.frame, text="Logout", command=self.logout,width=20, height=2, bg="red", fg="black", font=("Arial", 12, "bold"))
        self.btn_log.grid(row=9, column=1, pady=10)


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
        self.lowdata()
        self.expdata()

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


    def open_inventory(self):
        # Define functionality for opening admin and employee window
        from inventory1 import InventoryApp
        self.root.destroy()
        root=tk.Tk()
        app=InventoryApp(root)
        root.mainloop()

    def open_cart(self):
        # Define functionality for opening stocks window
        from Cart import Cartapp
        self.root.destroy()
        root=tk.Tk()
        Cartapp(root)
        root.mainloop()

    def open_return(self):
        # Define functionality for opening inventory window
        from Return import ReturnClass
        self.root.destroy()
        root=tk.Tk()
        ReturnClass(root)
        root.mainloop()

    def open_bt(self):
        self.root.destroy()
        os.system("python Billing1.py")

def main():
    root = tk.Tk()
    app = Empdash(root)
    root.mainloop()

if __name__ == "__main__":
    main()
