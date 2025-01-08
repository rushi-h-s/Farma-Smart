import tkinter as tk
from tkinter import messagebox, ttk
import addemp
from tkinter import Canvas, PhotoImage, Label
from PIL import Image,ImageTk
from UpdateEmp import Update
from connector.ConnectionProvider import ConnectionProvider
import SetImage as si

from BackgroundPage import BackgroundPage
from PIL import Image, ImageTk





class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("003.jpg")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1200, 710))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img
class AdEmp:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Employee")
        self.root.geometry("1200x710")
        BackgroundPage(root)
        # UI Elements
        self.lbl_title = tk.Label(root, text="ADMIN & EMPLOYEE DETAILS", font=("Tahoma", 36, "bold"))
        self.lbl_title.place(x=270, y=20)

        self.btn_add = tk.Button(root, text="ADD", font=("Tahoma", 18),bg='#89CFF0', command=self.add_employee)
        self.btn_add.place(x=30, y=130)

        self.btn_update = tk.Button(root, text="UPDATE", font=("Tahoma", 18),bg='#89CFF0' ,command=self.update_employee)
        self.btn_update.place(x=30, y=190)

        self.btn_delete = tk.Button(root, text="DELETE", font=("Tahoma", 18),bg='#89CFF0' , command=self.delete_employee)
        self.btn_delete.place(x=30, y=250)

        self.btn_back = tk.Button(root, text="BACK", font=("Tahoma", 18),bg='#89CFF0' , command=self.go_back)
        self.btn_back.place(x=30, y=310)

        self.tbl_employee = tk.Label(root, text="Employee Table")
        self.tbl_employee.place(x=160, y=80)

        self.tree = ttk.Treeview(root,height=23)
        self.tree["columns"] = ("Id", "UserRole", "Name", "Doj", "Mobile", "emailid", "username", "password", "salary")
        self.tree.column("#0",width=0,stretch="NO")
        self.tree.column("UserRole",anchor="center", width=100)
        self.tree.column("Id",anchor="center", width=100)
        self.tree.column("Name",anchor="center", width=100)
        self.tree.column("Doj",anchor="center", width=100)
        self.tree.column("Mobile",anchor="center", width=100)
        self.tree.column("emailid",anchor="center", width=100)
        self.tree.column("username",anchor="center", width=100)
        self.tree.column("password",anchor="center", width=100)
        self.tree.column("salary",anchor="center", width=100)
        self.tree.heading("#0", text="index")
        self.tree.heading("Id", text="Id")
        self.tree.heading("UserRole", text="UserRole")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Doj", text="Doj")
        self.tree.heading("Mobile", text="Mobile")
        self.tree.heading("emailid", text="eamilid")
        self.tree.heading("username", text="username")
        self.tree.heading("password", text="password")
        self.tree.heading("salary", text="salary")
        self.tree.place(x=200,y=150)
        self.tree
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
            cursor.execute("SELECT * FROM appuser")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")



    def add_employee(self):
        # Add code to open a window for adding a new employee

        self.root.destroy()
        root = tk.Tk()
        app = addemp.addemp(root)
        root.mainloop()

    def update_employee(self):
        # Add code to open a window for updating an existing employee
        self.root.destroy()
        root = tk.Tk()
        app=Update(root)
        root.mainloop()

    def delete_employee(self):
        # Add code to delete a selected employee from the table
        selected_item = self.tree.focus()
        data=self.tree.item(selected_item,'values')
        Id = data[0]
        userRole = data[1]
        if userRole=="Admin":
            messagebox.showinfo("Warning","you can't delete your own account")
        else:
            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("DELETE FROM appuser WHERE appuser_pk=%s", (Id,))
                con.commit()
                con.close()
                messagebox.showerror("","User deleted successfully..")
                self.root.destroy()
                root = tk.Tk()
                app=AdEmp(root)
                root.mainloop()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def set_background(window, image_path):
        # Load the image file
        bg_image = PhotoImage(file=image_path)
        # Create a label with the image
        bg_label = ttk.Label(window, image=bg_image)
        # Set the label as the background
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Keep a reference to the image
        bg_label.image = bg_image
        bg_label.pack
    def go_back(self):
        from Admin import Admin
        self.root.destroy()
        root = tk.Tk()
        app = Admin(root)
        root.mainloop()
        # Close the current window




if __name__ == "__main__":

    root = tk.Tk()

    app = AdEmp(root)
    # imagelbl.pack()
    root.mainloop()

