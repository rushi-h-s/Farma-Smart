from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import re
from PIL import Image, ImageTk
import Ademp
from connector.ConnectionProvider import ConnectionProvider

class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("update.jpg")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1030, 610))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img
class Update:
    def __init__(self, root):

        self.root = root
        self.mobileNumberPattern = "^[0-9]*$"
        self.EmailPattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        self.root.title("Update Employee")
        self.root.geometry("1030x630+150+100")
        BackgroundPage(root)
        self.lable=tk.Label(root,text="r")

        self.label_title = tk.Label(root, background="#ADD8E6",text="UPDATE EMPLOYEE", font=("Serif", 32))
        self.label_title.place(x=275,y=20)

        self.label_username = tk.Label(root, background="#ADD8E6",text="Username", font=("SansSerif", 18))
        self.label_username.place(x=200, y=90)

        self.txtUsername = tk.Entry(root, font=("Segoe UI", 14))
        self.txtUsername.place(x=340, y=90, width=250)

        self.btn_search = tk.Button(root, text="Search", font=("SansSerif", 14),bg ='#E14F27', command=self.search_employee)
        self.btn_search.place(x=610, y=90, width=70, height=30)

        self.label_username = tk.Label(root, background="#ADD8E6", text="Username", font=("SansSerif", 14))
        self.label_username.place(x=150, y=170)

        self.txtusername = tk.Entry(root, font=("Segoe UI", 14))
        self.txtusername.place(x=150, y=200, width=200)

        self.label_userrole = tk.Label(root, background="#ADD8E6",text="UserRole", font=("SansSerif", 14))
        self.label_userrole.place(x=650, y=170)

        self.combo_user_role = ttk.Combobox(root, font=("Segoe UI", 18), state="readonly")
        self.combo_user_role["values"] = ("Admin", "Employee")
        self.combo_user_role.place(x=650,y=200,width=200,height=30)

        self.label_password = tk.Label(root,background="#ADD8E6", text="Password", font=("SansSerif", 14))
        self.label_password.place(x=150, y=260)

        self.txtpassword = tk.Entry(root, font=("Segoe UI", 14))
        self.txtpassword.place(x=150, y=290, width=200)

        self.label_name = tk.Label(root,background="#ADD8E6", text="Name", font=("SansSerif", 14))
        self.label_name.place(x=650, y=260)

        self.txtname = tk.Entry(root, font=("Segoe UI", 14))
        self.txtname.place(x=650, y=290, width=200)

        self.label_mobile = tk.Label(root,background="#ADD8E6", text="Mobile", font=("SansSerif", 14))
        self.label_mobile.place(x=150, y=350)

        self.txtmobile = tk.Entry(root, font=("Segoe UI", 14))
        self.txtmobile.place(x=150, y=380, width=200)

        self.label_doj = tk.Label(root,background="#ADD8E6", text="Date Of Joining", font=("SansSerif", 14))
        self.label_doj.place(x=650, y=350)

        self.txtdoj = tk.Entry(root, font=("Segoe UI", 14))
        self.txtdoj.place(x=650, y=380, width=200)

        self.label_email = tk.Label(root,background="#ADD8E6", text="Email", font=("SansSerif", 14))
        self.label_email.place(x=150, y=440)

        self.txtemail = tk.Entry(root, font=("Segoe UI", 14))
        self.txtemail.place(x=150, y=470, width=200)

        self.label_salary = tk.Label(root,background="#ADD8E6", text="Salary", font=("SansSerif", 14))
        self.label_salary.place(x=650, y=440)

        self.txtsalary = tk.Entry(root, font=("Segoe UI", 14))
        self.txtsalary.place(x=650, y=470, width=200)

        self.updatebtn=tk.Button(root,text="Update",font=("SansSerif",18),background="#B6A5F1",command=self.update_employee)
        self.updatebtn.place(x=480,y=550)

        self.backbtn = tk.Button(root, text="Back", font=("SansSerif", 18),background="#B6A5F1", command=self.back_to_ademp)
        self.backbtn.place(x=400, y=550)



        # Add other widgets and layout as per your Java code...

    def search_employee(self):
        # Implement the search functionality similar to your Java code...
        txtUsername=self.txtUsername.get()
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM appuser WHERE username=%s",(txtUsername,))
            result=cursor.fetchone()
            con.close()
            if result:

                self.lable.destroy()
                self.txtusername.delete(0,tk.END)
                self.txtusername.insert(0,result[6])

                self.combo_user_role.delete(0, tk.END)
                self.combo_user_role.set(result[1])

                self.txtpassword.delete(0, tk.END)
                self.txtpassword.insert(0, result[7])

                self.txtname.delete(0, tk.END)
                self.txtname.insert(0, result[2])

                self.txtmobile.delete(0, tk.END)
                self.txtmobile.insert(0, result[4])

                self.txtdoj.delete(0, tk.END)
                self.txtdoj.insert(0, result[3])

                self.txtemail.delete(0, tk.END)
                self.txtemail.insert(0, result[5])

                self.txtsalary.delete(0, tk.END)
                self.txtsalary.insert(0, result[8])
            else:

                self.lable = tk.Label(self.root, text="No User Found", font=("Segoe UI", 14), foreground="red")
                self.lable.place(x=340, y=120)
                self.txtusername.delete(0,tk.END)
                self.txtpassword.delete(0, tk.END)
                self.txtname.delete(0, tk.END)
                self.txtmobile.delete(0, tk.END)
                self.txtdoj.delete(0, tk.END)
                self.txtemail.delete(0, tk.END)
                self.txtsalary.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_employee(self):

        username=self.txtUsername.get()
        userrole=self.combo_user_role.get()
        password=self.txtpassword.get()
        name=self.txtname.get()
        mobile=self.txtmobile.get()
        doj=self.txtdoj.get()
        emailid=self.txtemail.get()
        salary=self.txtsalary.get()
        print(username)
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("UPDATE appuser SET userRole=%s, name=%s, doj=%s, mobileNumber=%s,emailid=%s, password=%s, salary=%s WHERE username=%s" , (userrole,name,doj,mobile,emailid,password,salary,username))
            con.commit()
            con.close()
            if username:
                messagebox.showinfo("","Updated User Successfully.")
            else:
                messagebox.showinfo("","No User Selected")

            self.txtusername.delete(0, tk.END)
            self.txtpassword.delete(0, tk.END)
            self.txtname.delete(0, tk.END)
            self.txtmobile.delete(0, tk.END)
            self.txtdoj.delete(0, tk.END)
            self.txtemail.delete(0, tk.END)
            self.txtsalary.delete(0, tk.END)
            self.txtUsername.delete(0,tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def back_to_ademp(self):
        self.root.destroy()
        root=tk.Tk()
        Ademp.AdEmp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    Update(root)
    root.mainloop()