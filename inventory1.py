import os
import tkinter as tk
from tkinter import messagebox, ttk

import Login
import addemp
from Login import loginClass
import SetImage as  si


from connector.ConnectionProvider import ConnectionProvider


from BackgroundPage import BackgroundPage
from PIL import Image, ImageTk





class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("001.jpg")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1200, 600))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img

class InventoryApp:
    def __init__(self, root):
        self.add_stock = None
        self.root = root
        self.root.title("Inventory ")
        self.root.geometry("1200x600")
        BackgroundPage(root)
        # UI Elements
        self.lbl_title = tk.Label(root, text="Inventory DETAILS", font=("Tahoma", 36, "bold"))
        self.lbl_title.place(x=270, y=20)


        self.btn_back = tk.Button(root, text="BACK ", font=("Tahoma", 18), bg='#22D43B', command=self.go_back, width=8, height=1)
        self.btn_back.place(x=30, y=200)

        self.btn_delete = tk.Button(root, text="DELETE", font=("Tahoma", 18), bg='#22D43B', command=self.delete, width=8, height=1)
        self.btn_delete.place(x=30, y=300)

        self.tbl_employee = tk.Label(root, text="Search",font=("Tahoma", 18))
        self.tbl_employee.place(x=160, y=100)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search)  # Triggers search on any modification to the variable

        self.entry_search = tk.Entry(root, textvariable=self.search_var, font=("Tahoma", 14))
        self.entry_search.place(x=250, y=100)

        self.entry_search.bind("<KeyRelease>", self.search)

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("stock_id", "Id", "medicineName", "dom", "doe", "quantity", "price","totalPrice", "Category")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("stock_id", anchor="center", width=100)
        self.tree.column("Id", anchor="center", width=100)
        self.tree.column("medicineName", anchor="center", width=100)
        self.tree.column("dom", anchor="center", width=100)
        self.tree.column("doe", anchor="center", width=100)
        self.tree.column("quantity", anchor="center", width=100)
        self.tree.column("price", anchor="center", width=100)
        self.tree.column("totalPrice", anchor="center", width=100)
        self.tree.column("Category", anchor="center", width=100)
        self.tree.heading("#0", text="index")
        self.tree.heading("stock_id", text="stock_id")
        self.tree.heading("Id", text="Id")
        self.tree.heading("medicineName", text="medicineName")
        self.tree.heading("dom", text="Dom")
        self.tree.heading("doe", text="Doe")
        self.tree.heading("quantity", text="quantity")
        self.tree.heading("price", text="price")
        self.tree.heading("totalPrice", text="totalPrice")
        self.tree.heading("Category", text="Category")
        self.tree.place(x=200,y=150)
        self.scrollbar_y = tk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_y.place(x=1110, y=160, height=200)

        self.tree.configure(yscrollcommand=self.scrollbar_y.set)
        self.load_data()

    def delete(self):
        selected_item = self.tree.focus()
        data = self.tree.item(selected_item, 'values')
        Id = data[0]
        name=data[2]
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("DELETE FROM inventory WHERE stock_id=%s", (Id,))
            cursor.execute("DELETE FROM stock WHERE stock_id=%s", (Id,))
            cursor.execute("DELETE FROM selling WHERE name=%s",(name,))
            con.commit()
            con.close()
            messagebox.showerror("", "Stock deleted successfully..")
            self.root.destroy()
            root = tk.Tk()
            app = InventoryApp(root)
            root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def load_data(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            cursor.execute(" SELECT name,SUM(quantity) AS totalqty from selling GROUP BY name ORDER BY totalqty DESC LIMIT 1;")
            highest_row = cursor.fetchone()
            if highest_row:
                highest_name = highest_row[0]
                # Compare the fetched name with the existing names in the Treeview
                for child in self.tree.get_children():
                    item = self.tree.item(child)
                    if item['values'][2] == highest_name:
                        # Move the existing row in the Treeview
                        self.tree.move(child, '', 0)
                        self.tree.tag_configure('high_sales', background='lightgreen')
                        self.tree.tag_configure('highlighted_row', background='lightgreen')
                        self.tree.item(child, tags=('highlighted_row',))
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def go_back(self):
        self.root.destroy()
        os.system("python Empdash.py")

    def search(self,event=None):
        search_term = self.entry_search.get().strip().lower()
        self.tree.delete(*self.tree.get_children())  # Clear existing rows
        if search_term:
            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("SELECT * FROM inventory WHERE LOWER(medicineName) LIKE %s", ('%' + search_term + '%',))

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

    app = InventoryApp(root)
    root.mainloop()
