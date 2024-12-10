import re
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from connector.ConnectionProvider import ConnectionProvider
from datetime import datetime
import time
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


class AddStock():
    def __init__(self,root):
        self.root=root
        self.root.title("Add Stock")
        self.root.geometry("1030x610")
        BackgroundPage(root)
        
        self.label1 = tk.Label(root, text="Add Stock", font=("Tahoma", 18, "bold"))
        self.label1.place(x=440, y=20)

        self.labelcat = tk.Label(root, text="Category", font=("Tahoma", 18, "bold"))
        self.labelcat.place(x=400, y=70)

        self.category = ttk.Combobox(root, font=("Segoe UI", 18), state="readonly")
        self.category["values"] = ("Generic Medications", "Medical Devices","Herbal and Dietary Supplements")
        self.category.place(x=400, y=100)

        self.label2 = tk.Label(root, text="Medicine ID", font=("Tahoma", 14, "bold"))
        self.label2.place(x=130, y=160)

        self.label3 = tk.Label(root, text="Medicine Name", font=("Tahoma", 14, "bold"))
        self.label3.place(x=130, y=240)

        self.label4 = tk.Label(root, text="Supplier Name", font=("Tahoma", 14, "bold"))
        self.label4.place(x=130, y=320)

        self.label5 = tk.Label(root, text="Quantity", font=("Tahoma", 14, "bold"))
        self.label5.place(x=130, y=420)

        self.label6 = tk.Label(root, text="Date of Manufacture", font=("Tahoma", 14, "bold"))
        self.label6.place(x=580, y=160)

        self.label7 = tk.Label(root, text="Date of Expiry", font=("Tahoma", 14, "bold"))
        self.label7.place(x=580, y=240)

        self.label8 = tk.Label(root, text="Purchase Date", font=("Tahoma", 14, "bold"))
        self.label8.place(x=580, y=320)

        self.label9 = tk.Label(root, text="Price Per Unit", font=("Tahoma", 14, "bold"))
        self.label9.place(x=580, y=410)

        self.txtmedid = tk.Entry(root, font=("Tahoma", 12))
        self.txtmedid.place(x=130, y=190, width=320, height=30)


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

        self.button1 = tk.Button(root, text="ADD", font=("Tahoma", 14, "bold"), bg='darkblue', fg='black', command=self.add_stock)
        self.button1.place(x=380, y=560, width=106, height=41)

        self.button2 = tk.Button(root, text="Back", font=("Tahoma", 14, "bold"), bg='#22D43B', fg='black', command=self.go_back)
        self.button2.place(x=570, y=560, width=106, height=41)


    def go_back(self):
        from stock import stock
        self.root.destroy()
        root=tk.Tk()
        stock_purchased = stock(root)
        root.mainloop()

    def add_stock(self):
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

        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO stock(Id,medicineName,supplierName,dom,doe,purchaseDate,quantity,price,category) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (medicineId, medicineName, supplierName, datem, datee, datep, quantity, priceperunit, category))

            con.commit()
            self.stock_id = cursor.lastrowid  # Ensure stock_id is set after inserting
            cursor.close()
            con.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Second try block for inventory insertion
        try:
            Price = 2 * prc
            total = qty * Price
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO inventory(Id,medicineName,dom,doe,quantity,price,totalPrice,stock_id,category) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (medicineId, medicineName, datem, datee, quantity, Price, total, self.stock_id, category))

            con.commit()
            messagebox.showinfo("Success", "Stock Added Successfully.")

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            con.close()
            self.root.destroy()
            root = tk.Tk()
            AddStock(root)
            root.mainloop()






if __name__ == "__main__":
    root=tk.Tk()
    AddStock(root)
    root.mainloop()
