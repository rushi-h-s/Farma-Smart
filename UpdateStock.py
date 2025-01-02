import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector import Error
import re
import datetime
from connector.ConnectionProvider import ConnectionProvider
from PIL import Image, ImageTk


class BackgroundPage:
    def __init__(self,root):
        self.root = root
        # Ensure that size of image is same as/greater than size of frame
        self.raw_image = Image.open("update.jpg")
        # Define the size of the image, which will also determine the size of the frame
        self.raw_image = self.raw_image.resize((1012, 680))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img

class UpdateStock():
    def __init__(self, root):
        self.root = root
        self.txtcat = None
        self.root.title("Update Stock")
        self.root.geometry("1012x680")
        BackgroundPage(root)

        self.lable = tk.Label(root, text="No Stock Found", font=("Segoe UI", 14), foreground="red")

        self.label_title = tk.Label(root, text="Update Stock", font=("Tahoma", 36))
        self.label_title.pack()

        self.labelcat = tk.Label(root, text="Category", font=("Tahoma", 18, "bold"))
        self.labelcat.place(x=130, y=160)

        self.category = ttk.Combobox(root, font=("Segoe UI", 18), state="readonly")
        self.category["values"] = ("Generic Medications", "Medical Devices", "Herbal and Dietary Supplements")
        self.category.place(x=130, y=190)

        self.label2 = tk.Label(root,text="Medicine Id ",  font=("Tahoma", 14, "bold"))
        self.label2.place(x=400, y=70)

        self.label3 = tk.Label(root,text="Medicine Name",  font=("Tahoma", 14, "bold"))
        self.label3.place(x=130, y=240)

        self.label4 = tk.Label(root,text="Supplier Name",  font=("Tahoma", 14, "bold"))
        self.label4.place(x=130, y=320)

        self.label5 = tk.Label(root,text="Quantity", font=("Tahoma", 14, "bold"))
        self.label5.place(x=130, y=420)

        self.label6 = tk.Label(root,text="DOM", font=("Tahoma", 14, "bold"))
        self.label6.place(x=580, y=160)

        self.label7 = tk.Label(root,text="DOE",font=("Tahoma", 14, "bold"))
        self.label7.place(x=580, y=240)

        self.label8 = tk.Label(root,text="Purchase date",  font=("Tahoma", 14, "bold"))
        self.label8.place(x=580, y=320)

        self.label9 = tk.Label(root,text="Price", font=("Tahoma", 14, "bold"))
        self.label9.place(x=580, y=410)

        self.txtmedid = tk.Entry(root, font=("Tahoma", 12))
        self.txtmedid.place(x=360, y=100, width=320, height=30)

        self.txtmedname = tk.Entry(root, font=("Tahoma", 12))
        self.txtmedname.place(x=130, y=280, width=320, height=30)

        self.txtsuppname = tk.Entry(root, font=("Tahoma", 12))
        self.txtsuppname.place(x=130, y=360, width=320, height=30)

        self.txtquan = tk.Entry(root, font=("Tahoma", 12))
        self.txtquan.place(x=130, y=460, width=320, height=30)

        self.txtdom = tk.Entry(root, font=("Tahoma", 12))
        self.txtdom.place(x=580, y=190, width=320, height=30)

        self.txtdoe = tk.Entry(root, font=("Tahoma", 12))
        self.txtdoe.place(x=580, y=270, width=320, height=30)

        self.txtpur = tk.Entry(root, font=("Tahoma", 12))
        self.txtpur.place(x=580, y=350, width=320, height=30)

        self.txtprice = tk.Entry(root, font=("Tahoma", 12))
        self.txtprice.place(x=580, y=450, width=320, height=30)

        self.btn_search = tk.Button(root, text="Search", command=self.search, font=("Tahoma", 18))
        self.btn_search.place(x=700, y=90)

        self.btn_save = tk.Button(root, text="Save", command=self.save, font=("Tahoma", 18))
        self.btn_save.place(x=200, y=580)

        self.btn_back = tk.Button(root, text="Back", command=self.go_back, font=("Tahoma", 18))
        self.btn_back.place(x=380, y=580)

    def search(self):
        id = self.txtmedid.get()  # Retrieve text from Text widget
        if id == "":
            messagebox.showinfo("Error", "Medicine Id field is required.")
        else:

            try:
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                cursor = con.cursor()
                cursor.execute("SELECT * FROM stock WHERE Id=%s", (id,))
                result = cursor.fetchone()
                con.close()
                if result:

                    self.lable.destroy()



                    self.txtmedname.delete(0, tk.END)
                    self.txtmedname.insert(tk.END, result[2])

                    self.txtsuppname.delete(0, tk.END)
                    self.txtsuppname.insert(tk.END, result[3])

                    # Convert DOM (Date of Manufacture)
                    if isinstance(result[4], datetime.date):
                        dom = result[4].strftime("%d/%m/%Y")
                    else:
                        dom = datetime.datetime.strptime(result[4], "%Y-%m-%d").strftime("%d/%m/%Y")

                    # Convert DOE (Date of Expiry)
                    if isinstance(result[5], datetime.date):
                        doe = result[5].strftime("%d/%m/%Y")
                    else:
                        doe = datetime.datetime.strptime(result[5], "%Y-%m-%d").strftime("%d/%m/%Y")

                    # Convert Purchase Date
                    if isinstance(result[6], datetime.date):
                        purchasedate = result[6].strftime("%d/%m/%Y")
                    else:
                        purchasedate = datetime.datetime.strptime(result[6], "%Y-%m-%d").strftime("%d/%m/%Y")

                    self.txtdom.delete(0, tk.END)
                    self.txtdom.insert(tk.END, dom)

                    self.txtdoe.delete(0, tk.END)
                    self.txtdoe.insert(tk.END, doe)

                    self.txtpur.delete(0, tk.END)
                    self.txtpur.insert(tk.END, purchasedate)


                    self.txtquan.delete(0, tk.END)
                    self.txtquan.insert(tk.END, result[8])

                    self.txtprice.delete(0, tk.END)
                    self.txtprice.insert(tk.END, result[9])

                    self.category.set(result[7])  # Assuming category is at index 8 in result tuple



                else:

                    self.lable.place(x=340, y=120)
                    self.txtprice.delete(0, tk.END)
                    self.txtdoe.delete(0, tk.END)
                    self.txtdom.delete(0, tk.END)
                    self.txtpur.delete(0, tk.END)
                    self.txtquan.delete(0, tk.END)
                    self.txtsuppname.delete(0, tk.END)
                    self.txtmedname.delete(0, tk.END)
                    self.txtmedid.delete(0,tk.END)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def save(self):
        import re
        from datetime import datetime
        from tkinter import messagebox
        pattern = r'^\d{2}/\d{2}/\d{4}$'

        medicineId = self.txtmedid.get()
        medicineName = self.txtmedname.get()
        supplierName = self.txtsuppname.get()
        quantity = self.txtquan.get()
        dom = self.txtdom.get()
        doe = self.txtdoe.get()
        purchasedate = self.txtpur.get()
        category = self.category.get()
        priceperunit = self.txtprice.get()

        if medicineId == "":
            messagebox.showinfo("Invalid Info", "Please Enter an Integer")
        elif medicineName == "":
            messagebox.showinfo("Invalid Info", "Please Enter Medicine Name")
        elif doe == "":
            messagebox.showinfo("Invalid Info", "Please Enter DOE")
        elif dom == "":
            messagebox.showinfo("Invalid Info", "Please Enter DOM")
        elif purchasedate == "":
            messagebox.showinfo("Invalid Info", "Please Enter purchase date")
        elif quantity == "":
            messagebox.showinfo("Invalid Info", "Please Enter Quantity")
        elif category == "":
            messagebox.showinfo("Invalid Info", "Please Enter Category of Medicine")
        elif priceperunit == "":
            messagebox.showinfo("Invalid Info", "Please Enter price per unit")
        else:
            if re.match(pattern, doe):
                datee = datetime.strptime(doe, '%d/%m/%Y').strftime('%Y-%m-%d')
            else:
                messagebox.showinfo("Invalid Info", "Invalid DOE format. Please use DD/MM/YYYY.")

            if re.match(pattern, purchasedate):
                datep = datetime.strptime(purchasedate, '%d/%m/%Y').strftime('%Y-%m-%d')
            else:
                messagebox.showinfo("Invalid Info", "Invalid Purchase Date format. Please use DD/MM/YYYY.")

            if re.match(pattern, dom):
                datem = datetime.strptime(dom, '%d/%m/%Y').strftime('%Y-%m-%d')
            else:
                messagebox.showinfo("Invalid Info", "Invalid DOM format. Please use DD/MM/YYYY.")


        qty = int(quantity)
        prc = float(priceperunit)
        total=qty*prc

        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            # Assuming you have a database named 'medical_store.db' with a table named 'stock'
            cursor = con.cursor()

            cursor.execute("UPDATE stock SET medicineName=%s,supplierName=%s,dom=%s,doe=%s,purchasedate=%s,quantity=%s,price=%s,category=%s WHERE Id=%s",
                         ( medicineName, supplierName, datem, datee, datep, quantity, priceperunit,category,medicineId))

            con.commit()
            self.stock_id = cursor.lastrowid
            con.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))
        try:
            Price = 2 * prc
            total = qty * Price
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("UPDATE inventory SET medicineName=%s,dom=%s,doe=%s,quantity=%s,price=%s,category=%s,totalPrice=%s WHERE Id=%s",
                             ( medicineName, datem, datee, quantity, Price,category,total,medicineId))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Updated Successfully.")
            self.root.destroy()
            root = tk.Tk()
            app = UpdateStock(root)
            root.mainloop()

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def go_back(self):
        self.root.destroy()
        os.system("python stock.py")


if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateStock(root)
    root.mainloop()

