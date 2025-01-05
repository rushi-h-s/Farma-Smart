import os
import tkinter as tk
from tkinter import messagebox, ttk

import Login

from connector.ConnectionProvider import ConnectionProvider
from PIL import Image, ImageTk
from BackgroundPage import BackgroundPage

class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("add image.png")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1200, 600))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img
class BillApp:
    def __init__(self, root):
        self.add_stock = None
        BackgroundPage(root)
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1200x600")

        # UI Elements
        self.lbl_title = tk.Label(root, text="Customer/Blling Records", font=("Tahoma", 36, "bold"))
        self.lbl_title.place(x=270, y=20)


        self.btn_back = tk.Button(root, text="BACK", font=("Tahoma", 18),bg='darkblue',fg='black', command=self.go_back, width=8, height=1)
        self.btn_back.place(x=30, y=200)

        self.tbl_employee = tk.Label(root, text="Bill ID" ,font=("Tahoma",12 ))
        self.tbl_employee.place(x=190, y=100)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search)  # Triggers search on any modification to the variable

        self.entry_search = tk.Entry(root, textvariable=self.search_var, font=("Tahoma", 14))
        self.entry_search.place(x=300, y=100)

        self.entry_search.bind("<KeyRelease>", self.search)

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("billid", "bill_date", "cname", "mobile", "mname", "qty", "pr","tamt", "dct")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("billid", anchor="center", width=100)
        self.tree.column("bill_date", anchor="center", width=100)
        self.tree.column("cname", anchor="center", width=100)
        self.tree.column("mobile", anchor="center", width=100)
        self.tree.column("mname", anchor="center", width=100)
        self.tree.column("qty", anchor="center", width=100)
        self.tree.column("pr", anchor="center", width=100)
        self.tree.column("tamt", anchor="center", width=100)
        self.tree.column("dct", anchor="center", width=100)
        self.tree.heading("#0", text="index")
        self.tree.heading("billid", text="Bill ID")
        self.tree.heading("bill_date", text="Bill Date")
        self.tree.heading("cname", text="Customer")
        self.tree.heading("mobile", text="Mobile")
        self.tree.heading("mname", text="Medicine")
        self.tree.heading("qty", text="Quantity")
        self.tree.heading("pr", text="Price")
        self.tree.heading("tamt", text="Total Price")
        self.tree.heading("dct", text="Discount")
        self.tree.place(x=200,y=150)
        self.scrollbar_y = tk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_y.place(x=1110, y=160, height=200)

        self.tree.configure(yscrollcommand=self.scrollbar_y.set)
        self.load_data()

    def load_data(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def go_back(self):
        self.root.destroy()
        os.system("python Admin.py")

    def search(self,event=None):
        search_term = self.entry_search.get().strip().lower()
        self.tree.delete(*self.tree.get_children())  # Clear existing rows
        if search_term:
            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("SELECT * FROM customer WHERE LOWER(billid) LIKE %s", ('%' + search_term + '%',))

                rows = cursor.fetchall()
                for row in rows:
                    self.tree.insert("", tk.END, values=row)
                con.close()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            self.load_data()  # Reload all data if search term is empty


if __name__ == "__main__":
    root = tk.Tk()
    app = BillApp(root)
    root.mainloop()
