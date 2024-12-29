import os
import tkinter as tk
from tkinter import messagebox,ttk
from tkinter import *
import mysql.connector
from connector.ConnectionProvider import ConnectionProvider
from PIL import Image, ImageTk


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

class AddSupp(tk.Tk):
    def __init__(self,root):
        super().__init__()
        self.root=root
        self.root.title("Add Supplier")
        self.root.geometry("1030x610")
        BackgroundPage(root)

        self.MobileNumberPattern = "^[0-9]*$"
        self.checkSupplier_ID = 0
        self.lable = tk.Label(root, text="No Stock Found", font=("Segoe UI", 14), foreground="red")

        self.lbl_title = tk.Label(root, text="ADD SUPPLIER", font=("Serif", 32, "bold"))
        self.lbl_title.place(x=340, y=20)

        self.btn_search = tk.Button(root, text="search", font=("Tahoma", 18, "bold"), command=self.search)
        self.btn_search.place(x=400, y=110)

        self.lbl_supplier_id = tk.Label(root, text="Supplier ID", font=("Tahoma", 18))
        self.lbl_supplier_id.place(x=83, y=90)

        self.lbl_supplier_name = tk.Label(root, text="Supplier Name", font=("Tahoma", 18))
        self.lbl_supplier_name.place(x=710, y=300)

        self.lbl_mobile = tk.Label(root, text="Mobile Number", font=("Tahoma", 18))
        self.lbl_mobile.place(x=90, y=300)

        self.lbl_address = tk.Label(root, text="Address", font=("Tahoma", 18))
        self.lbl_address.place(x=400, y=300)

        self.txtsuppid = tk.Entry(root, font=("Segoe UI", 18))
        self.txtsuppid.place(x=83, y=120)

        self.txtsuppname = tk.Entry(root, font=("Segoe UI", 18))
        self.txtsuppname.place(x=710, y=340)

        self.txtmobile = tk.Entry(root, font=("Segoe UI", 18))
        self.txtmobile.place(x=83, y=336)

        self.txtaddress = tk.Entry(root, font=("Segoe UI", 18))
        self.txtaddress.place(x=400, y=340)

        self.btn_save = tk.Button(root, text="Save", font=("Tahoma", 18, "bold"), command=self.save_supplier)
        self.btn_save.place(x=310, y=430)

        self.btn_back = tk.Button(root, text="Back", font=("Tahoma", 18, "bold"), command=self.go_back)
        self.btn_back.place(x=480, y=430)

    def search(self):
        id = self.txtsuppid.get()  # Retrieve text from Text widget
        if id == "":
            messagebox.showinfo("Error", "Supplier Id field is required.")
        else:

            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("SELECT * FROM supplier WHERE Id=%s", (id,))
                result = cursor.fetchone()
                con.close()
                if result:

                    self.lable.destroy()

                    self.txtsuppname.delete(0, tk.END)
                    self.txtsuppname.insert(tk.END, result[1])

                    self.txtmobile.delete(0, tk.END)
                    self.txtmobile.insert(tk.END, result[2])


                    self.txtaddress.delete(0, tk.END)
                    self.txtaddress.insert(tk.END, result[3])




                else:

                    self.lable.place(x=340, y=120)
                    self.txtmobile.delete(0, tk.END)
                    self.txtaddress.delete(0, tk.END)
                    self.txtsuppid.delete(0, tk.END)
                    self.txtsuppname.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def save_supplier(self):

        Id = self.txtsuppid.get()
        supplierName = self.txtsuppname.get()
        mobileNumber = self.txtmobile.get()
        address = self.txtaddress.get()

        if Id == "":
            messagebox.showerror("Error", "Supplier ID field is required.")
        elif supplierName == "":
            messagebox.showerror("Error", "Supplier Name field is required.")
        elif mobileNumber == "":
            messagebox.showerror("Error", "Mobile number field is required.")
        elif not mobileNumber.isdigit() or len(mobileNumber) != 10:
            messagebox.showerror("Error", "Mobile Number field is invalid.")
        elif address == "":
            messagebox.showerror("Error", "Address field is required.")
        else:
            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()

                cursor = con.cursor()
                query = "UPDATE supplier SET  supplierName=%s, mobileNumber=%s, address=%s WHERE Id=%s"
                cursor.execute(query, ( supplierName, mobileNumber, address,Id))
                con.commit()
                messagebox.showinfo("Success", "Supplier Updated Successfully.")
                self.txtsuppid.delete(0, tk.END)
                self.txtsuppname.delete(0, tk.END)
                self.txtmobile.delete(0, tk.END)
                self.txtaddress.delete(0, tk.END)
                self.checkSupplier_ID = 0
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                con.close()

    def go_back(self):
        self.root.destroy()
        os.system("python supplier.py")

    def txtsuppid_keyreleased(self, event):
        Id = self.txtsuppid.get()
        if Id != "":
            self.checkSupplier_ID = 0
            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                query = "SELECT * FROM supplier WHERE Id = %s"
                cursor.execute(query, (Id,))
                result = cursor.fetchone()
                if result:
                    self.checkSupplier_ID = 1
                    messagebox.showerror("Error", "This supplier ID already exists.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                con.close()


if __name__ == "__main__":
    root = tk.Tk()  # Instantiate the Tkinter root object
    app = AddSupp(root)  # Pass the root object to the AddSupp class
    root.mainloop()

