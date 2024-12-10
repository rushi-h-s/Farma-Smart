from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import re
import time
from datetime import datetime
from PIL import Image, ImageTk

import Ademp
from connector.ConnectionProvider import ConnectionProvider
from BackgroundPage import BackgroundPage

class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("add image.png")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1030, 610))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img
        
class addemp:
    cursor = None
    def __init__(self,root):
        self.root = root
        self.root.title("Add Employee")
        self.root.geometry("1030x610+200+100")
        BackgroundPage(root)
        self.EmailPattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.MobileNumberPattern = "^[0-9]*$"
        self.checkUsername = 0

        # UI Elements
        self.lbl_title = Label(root, text="ADD USER", font=("Serif", 32, "bold"), padx=10)
        self.lbl_title.place(x=360, y=20)

        self.lbl_role = Label(root, text="Role", font=("Tahoma", 18))
        self.lbl_role.place(x=60, y=80)

        self.lbl_username = Label(root, text="Username", font=("Tahoma", 18))
        self.lbl_username.place(x=540, y=90)

        self.lbl_name = Label(root, text="Name", font=("Tahoma", 18))
        self.lbl_name.place(x=60, y=180)

        self.lbl_doj = Label(root, text="Date of Joining", font=("Tahoma", 18))
        self.lbl_doj.place(x=59, y=282)

        self.lbl_mobile = Label(root, text="Mobile Number", font=("Tahoma", 18))
        self.lbl_mobile.place(x=60, y=390)

        self.lbl_password = Label(root, text="Password", font=("Tahoma", 18))
        self.lbl_password.place(x=540, y=190)

        self.lbl_address = Label(root, text="Email", font=("Tahoma", 18))
        self.lbl_address.place(x=540, y=280)

        self.lbl_salary = Label(root, text="Salary", font=("Tahoma", 18))
        self.lbl_salary.place(x=540, y=380)

        self.txt_username = Entry(root, font=("Segoe UI", 18))
        self.txt_username.place(x=540, y=120)

        self.txt_name = Entry(root, font=("Segoe UI", 18))
        self.txt_name.place(x=59, y=221)

        self.txt_password = Entry(root, font=("Segoe UI", 18), show="*")
        self.txt_password.place(x=540, y=220)

        self.txt_doj = Entry(root, font=("Segoe UI", 18))
        self.txt_doj.place(x=59, y=319)

        self.txt_mobile = Entry(root, font=("Segoe UI", 18))
        self.txt_mobile.place(x=59, y=422)

        self.txt_email = Entry(root, font=("Segoe UI", 18))
        self.txt_email.place(x=540, y=310)

        self.txt_salary = Entry(root, font=("Segoe UI", 18))
        self.txt_salary.place(x=540, y=410)

        self.btn_save = Button(root, text="Save", font=("Tahoma", 18, "bold"), bd=2,bg='darkblue', fg='black', command=self.save_data)
        self.btn_save.place(x=320, y=490)

        self.btn_back = Button(root, text="Back", font=("Tahoma", 18, "bold"), bd=2,bg='#22D43B', fg='black', command=self.back)
        self.btn_back.place(x=461, y=490)

        self.combo_user_role = ttk.Combobox(root, font=("Segoe UI", 18), state="readonly")
        self.combo_user_role["values"] = ("Admin", "Employee")
        self.combo_user_role.place(x=59, y=112)

        self.lbl_label = Label(root, text="", font=("Tahoma", 12), fg="red")
        self.lbl_label.place(x=550, y=160)

    def back(self):
        self.root.destroy()
        root = tk.Tk()
        app = Ademp.AdEmp(root)
        root.mainloop()

        # Add code to go back to the previous window

    def save_data(self):
        user_role = self.combo_user_role.get()
        name = self.txt_name.get()
        doj = datetime.strptime(self.txt_doj.get(), '%d/%m/%Y').strftime('%Y-%m-%d')
        mobile_number = self.txt_mobile.get()
        username = self.txt_username.get()
        password = self.txt_password.get()
        email = self.txt_email.get()
        salary = self.txt_salary.get()

        # Validation
        if name == "":
            messagebox.showerror("Error", "Name field is required.")
            return
        elif doj == "":
            messagebox.showerror("Error", "Date of joining field is required.")
            return
        elif user_role == "":
            messagebox.showerror("Error", "Role field is required.")
            return
        elif mobile_number == "":
            messagebox.showerror("Error", "Mobile number field is required.")
            return
        elif not re.match(self.MobileNumberPattern, mobile_number) or len(mobile_number) != 10:
            messagebox.showerror("Error", "Mobile Number field is invalid.")
            return
        elif username == "":
            messagebox.showerror("Error", "Username field is required.")
            return
        elif self.checkUsername == 1:
            messagebox.showerror("Error", "This username already exists.")
            return
        elif password == "":
            messagebox.showerror("Error", "Password field is required.")
            return
        elif email == "":
            messagebox.showerror("Error", "Email field is required.")
            return
        elif not re.match(self.EmailPattern, email):
            messagebox.showerror("Error", "Email field is invalid.")
            return

        # Save to database
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()
            self.cursor.execute("SELECT COUNT(*) FROM appuser WHERE username = %s", (username,))
            count = self.cursor.fetchone()[0]
            con.close()

            if count > 0:
                messagebox.showerror("Error", "This username already exists.")
                return
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()
            self.cursor.execute("INSERT INTO appuser (userRole, name, doj, mobileNumber,emailid, username, password, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (user_role, name, doj, mobile_number,email, username, password, salary))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "User added successfully.")
            # Clear the form
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_form(self):
        self.combo_user_role.set('')
        self.txt_name.delete(0, 'end')
        self.txt_doj.delete(0, 'end')
        self.txt_mobile.delete(0, 'end')
        self.txt_username.delete(0, 'end')
        self.txt_password.delete(0, 'end')
        self.txt_email.delete(0, 'end')
        self.txt_salary.delete(0, 'end')

if __name__ == "__main__":
    root = Tk()
    app2 = addemp(root)
    root.mainloop()
