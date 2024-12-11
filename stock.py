import os
import tkinter as tk
from tkinter import messagebox, ttk

#from PIL import ImageTk,Image

from connector.ConnectionProvider import ConnectionProvider
import SetImage as si

from BackgroundPage import BackgroundPage
from PIL import Image, ImageTk





class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("001.jpg")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1350, 710))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img



class stock:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock")
        self.root.geometry("1350x710")
        # Create a canvas
        BackgroundPage(root)

        # UI Elements
        self.lbl_title = tk.Label(root, text="STOCK DETAILS",bg='white',font=("Tahoma", 36, "bold"))
        self.lbl_title.place(x=500, y=20)


        self.btn_add = tk.Button(root, text="ADD", font=("Tahoma", 18),bg='skyblue', command=self.add_stock, width=8, height=1)
        self.btn_add.place(x=30, y=170)

        self.btn_update = tk.Button(root, text="UPDATE", font=("Tahoma", 18),bg='#89CFF0' ,command=self.update_stock, width=8, height=1)
        self.btn_update.place(x=30, y=250)

        self.btn_delete = tk.Button(root, text="DELETE", font=("Tahoma", 18),bg='#89CFF0', command=self.delete_stock, width=8, height=1)
        self.btn_delete.place(x=30, y=330)

        self.btn_back = tk.Button(root, text="BACK", font=("Tahoma", 18), bg='#89CFF0',command=self.go_back, width=8, height=1)
        self.btn_back.place(x=30, y=410)

        self.tbl_employee = tk.Label(root, text="Stock Table")
        self.tbl_employee.place(x=160, y=80)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search)  # Triggers search on any modification to the variable

        self.entry_search = tk.Entry(root, textvariable=self.search_var, font=("Tahoma", 14))
        self.entry_search.place(x=200, y=100)

        self.entry_search.bind("<KeyRelease>", self.search)

        self.tree = ttk.Treeview(root,height=23)
        self.tree["columns"] = (
        "stock_id", "Id", "medicineName", "supplierName", "dom", "doe", "purchaseDate", "Category", "quantity",
        "price", "totalPrice")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("stock_id", anchor="center", width=100)
        self.tree.column("Id", anchor="center", width=100)
        self.tree.column("medicineName", anchor="center", width=100)
        self.tree.column("supplierName", anchor="center", width=100)
        self.tree.column("dom", anchor="center", width=100)
        self.tree.column("doe", anchor="center", width=100)
        self.tree.column("purchaseDate", anchor="center", width=100)
        self.tree.column("quantity", anchor="center", width=100)
        self.tree.column("price", anchor="center", width=100)
        self.tree.column("totalPrice", anchor="center", width=100)
        self.tree.column("Category", anchor="center", width=100)
        self.tree.heading("#0", text="index")
        self.tree.heading("stock_id", text="stock_id")
        self.tree.heading("Id", text="Id")
        self.tree.heading("medicineName", text="medicineName")
        self.tree.heading("supplierName", text="supplierName")
        self.tree.heading("dom", text="Dom")
        self.tree.heading("doe", text="Doe")
        self.tree.heading("purchaseDate", text="purchaseDate")
        self.tree.heading("quantity", text="quantity")
        self.tree.heading("price", text="price")
        self.tree.heading("totalPrice", text="totalPrice")
        self.tree.heading("Category", text="Category")
        self.tree.place(x=200,y=150)
        self.scrollbar_y = tk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_y.place(x=1310, y=160, height=200)

        self.tree.configure(yscrollcommand=self.scrollbar_y.set)
        self.load_data()

    def load_data(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM stock")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def add_stock(self):
            from AddStock import AddStock
            print("hello")
            self.root.destroy()
            os.system("python AddStock.py")



    def update_stock(self):
        from UpdateStock import UpdateStock
        self.root.destroy()
        root=tk.Tk()
        app=UpdateStock(root)
        root.mainloop()

    def delete_stock(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No item selected for deletion.")
            return

        data = self.tree.item(selected_item, 'values')
        stock_id = data[0]  # Assuming stock_id is the first value

        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            # First, attempt to delete from inventory
            cursor.execute("DELETE FROM inventory WHERE stock_id=%s", (stock_id,))
            # Then, delete from stock
            cursor.execute("DELETE FROM stock WHERE stock_id=%s", (stock_id,))

            con.commit()
            con.close()

            messagebox.showinfo("Success", "Stock item deleted successfully.")
            self.load_data()  # Reload data to refresh the tree view

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def search(self, event=None):
        search_term = self.entry_search.get().strip().lower()
        self.tree.delete(*self.tree.get_children())  # Clear existing rows
        if search_term:
            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("SELECT * FROM stock WHERE LOWER(medicineName) LIKE %s", ('%' + search_term + '%',))

                rows = cursor.fetchall()
                for row in rows:
                    self.tree.insert("", tk.END, values=row)
                con.close()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            self.load_data()  # Reload all data if search term is empty

    def go_back(self):
        from Admin import Admin
        self.root.destroy()  # Close the current window
        root = tk.Tk()
        app = Admin(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = stock(root)
    root.mainloop()
