import os
import tkinter as tk
from tkinter import messagebox, ttk


from connector.ConnectionProvider import ConnectionProvider
from BackgroundPage import BackgroundPage
from PIL import Image, ImageTk





class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("001.jpg")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1000, 710))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img

class Supplier:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Employee")

        self.root.geometry("1000x710")
        BackgroundPage(root)


        # UI Elements
        self.lbl_title = tk.Label(root, text="SUPPLIER DETAILS", font=("Tahoma", 36, "bold"))
        self.lbl_title.place(x=200, y=20)

        self.btn_add = tk.Button(root, text="ADD", font=("Tahoma", 18), command=self.add_supp)
        self.btn_add.place(x=30, y=120)

        self.btn_update = tk.Button(root, text="UPDATE", font=("Tahoma", 18), command=self.update_supp)
        self.btn_update.place(x=30, y=170)

        self.btn_delete = tk.Button(root, text="DELETE", font=("Tahoma", 18), command=self.delete_supp)
        self.btn_delete.place(x=30, y=220)

        self.btn_back = tk.Button(root, text="BACK", font=("Tahoma", 18), command=self.go_back)
        self.btn_back.place(x=30, y=270)

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("Id", "supplierName", "Mobile", "Address")
        self.tree.column("#0",width=0,stretch="NO")
        self.tree.column("Id",anchor="center", width=100)
        self.tree.column("supplierName",anchor="center", width=100)
        self.tree.column("Mobile",anchor="center", width=100)
        self.tree.column("Address",anchor="center", width=100)

        self.tree.heading("#0", text="index")
        self.tree.heading("Id", text="Id")
        self.tree.heading("supplierName", text="SupplierName")
        self.tree.heading("Mobile", text="Mobile")
        self.tree.heading("Address", text="Address")

        self.tree.place(x=300,y=150,height=500)
        self.scrollbar_y = tk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_y.place(x=705, y=150, height=500)

        self.tree.configure(yscrollcommand=self.scrollbar_y.set)
        self.load_data()

    def load_data(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM supplier")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def add_supp(self):
        # Add code to open a window for adding a new employee
        self.root.destroy()
        os.system("python addsup.py")


    def update_supp(self):
        # Add code to open a window for updating an existing employee
        self.root.destroy()
        os.system("python Updatesup.py")


    def delete_supp(self):
        # Add code to delete a selected employee from the table
        selected_item = self.tree.focus()
        data=self.tree.item(selected_item,'values')
        Id = data[0]
        try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("DELETE FROM supplier WHERE Id=%s", (Id,))
                con.commit()
                con.close()
                messagebox.showerror("","Supplier deleted successfully..")
                self.root.destroy()
                os.system("python supplier.py")

        except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def go_back(self):
        from Admin import Admin
        self.root.destroy()
        root = tk.Tk()
        app = Admin(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Supplier(root)
    root.mainloop()
