from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk, messagebox
import os
import mysql
from connector.ConnectionProvider import ConnectionProvider
class ReturnClass:
    cursor = None
    def __init__(self, root):

        self.root = root
        self.root.geometry("1300x750+130+0")
        self.root.title("Pharmacy  Management System ")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        self.bill_list = []
        self.var_invoice = StringVar()

        lbl_title = Label(self.root, text="Return Products", font=("goudy old style", 20, "bold"), bg="#add8e6",fg="#333333",bd=0, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        lbl_invoice = Label(self.root, text="       Bill no :", font=("times new roman", 15), bg="white" , fg= "black").place(x=50, y=80)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15),bg="#ebf3fb" , fg= "black").place(x=140, y=80, width=200, height=28)

        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"),bg="#2196f3", fg="black", cursor="hand2").place(x=360, y=80, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"),bg="lightgray", fg="black", cursor="hand2").place(x=490, y=80, width=120, height=28)
        btn_back = Button(self.root, text="Back", command=self.back, font=("times new roman", 15, "bold"),bg="#90ee90", fg="black", cursor="hand2").place(x=1130, y=80, width=120, height=28)

        # BILL LIST
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=35, y=120, width=200, height=600)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)

        self.sales_list = Listbox(sales_Frame, font=("goudy old style", 15), bg="black",fg= "white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)

        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        #widgets
        Add_WidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_WidgetsFrame.place(x=750, y=280, width=500, height=440)

        self.var_medname = StringVar()
        self.var_qty = StringVar()
        self.var_price = StringVar()
        self.var_amt = StringVar()
        self.var_gst = StringVar()
        self.var_blamt = StringVar()
        self.var_dct = StringVar()
        self.var_npay = StringVar()
        self.var_amtret = StringVar()

        lbl_med_name = Label(Add_WidgetsFrame, text="Product Name", font=("times new roman", 15), bg="white" , fg= "black").place(x=5,y=20)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_medname, font=("times new roman", 15),bg="#ebf3fb",fg= "white",state='readonly').place(x=5, y=55, width=120, height=22)
        lbl_p_qty = Label(Add_WidgetsFrame, text="Quantity", font=("times new roman", 15), bg="white" , fg= "black").place(x=155,y=20)
        txt_p_qty = Entry(Add_WidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15),bg="#ebf3fb", fg= "black" ).place(x=155, y=55, width=120, height=22)
        btn_update = Button(Add_WidgetsFrame, text="Update Quantity", command=self.update_qty,font=("times new roman",15, "bold"), bg="#2196f3", fg="black", cursor="hand2").place(x=320,y=50,width=150,height=25)
        separator = ttk.Separator(Add_WidgetsFrame, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=100)
        lbl_med_name = Label(Add_WidgetsFrame, text="P_Price", font=("times new roman", 15), bg="white" , fg= "black").place(x=5,y=115)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_price, font=("times new roman", 15),bg="#ebf3fb", state='readonly').place(x=5, y=145, width=120, height=22)
        lbl_med_name = Label(Add_WidgetsFrame, text="Amount", font=("times new roman", 15), bg="white" , fg= "black").place(x=155,y=115)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_amt, font=("times new roman", 15), bg="#ebf3fb", state='readonly').place(x=155, y=145, width=120, height=22)
        lbl_med_name = Label(Add_WidgetsFrame, text="GST", font=("times new roman", 15), bg="white", fg= "black").place(x=305,y=115)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_gst, font=("times new roman", 15),bg="#ebf3fb", state='readonly').place(x=305, y=145, width=120, height=22)
        lbl_med_name = Label(Add_WidgetsFrame, text="Bill Amount", font=("times new roman", 15), bg="white" , fg= "black").place(x=5,y=220)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_blamt, font=("times new roman", 15), bg="#ebf3fb", state='readonly').place(x=5, y=250, width=120, height=22)
        lbl_med_name = Label(Add_WidgetsFrame, text="Discount", font=("times new roman", 15), bg="white" , fg= "black").place(x=155,y=220)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_dct, font=("times new roman", 15), bg="#ebf3fb", state='readonly').place(x=155, y=250, width=120, height=22)
        lbl_med_name = Label(Add_WidgetsFrame, text="Net Pay", font=("times new roman", 15), bg="white" , fg= "black").place(x=305,y=220)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_npay, font=("times new roman", 15),bg="#ebf3fb", state='readonly').place(x=305, y=250, width=120, height=22)
        separator = ttk.Separator(Add_WidgetsFrame, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=100)
        lbl_med_name = Label(Add_WidgetsFrame, text="   Amount To Be Return :", font=("times new roman", 15, "bold"), bg="white",fg="green").place(x=5,y=345)
        txt_med_name = Entry(Add_WidgetsFrame, textvariable=self.var_amtret, font=("times new roman", 15), bg="#90EE90", state='readonly' , fg= "white").place(x=190, y=348, width=120, height=22)

        #return
        ProductFrame = Frame(self.root, bd=3, relief=RIDGE)
        ProductFrame.place(x=750, y=120, width=500, height=150)

        scrolly = Scrollbar(ProductFrame, orient=VERTICAL)

        self.product_Table = ttk.Treeview(ProductFrame, columns=("name", "qty", "price","tamount"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("name", text=" Product Name")
        self.product_Table.heading("qty", text="Quantity")
        self.product_Table.heading("price", text="Price Per Unit")
        self.product_Table.heading("tamount", text="Total amount")
        self.product_Table["show"] = "headings"
        self.product_Table.column("name", width=100)
        self.product_Table.column("qty", width=40)
        self.product_Table.column("price", width=100)
        self.product_Table.column("tamount", width=100)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data1)
        # BILL AREA
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=240, y=120, width=500, height=600)

        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("goudy old style", 20, "bold"),bg="#add8e6").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)

        self.bill_area = Text(bill_Frame, font=("goudy old style", 15), bg="black", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        self.show()

    def fetch_product_data(self, bill_number):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()

            # Fetch all products related to the bill
            query = f"SELECT mname, qty, pr, bill_date FROM customer WHERE billid = %s"
            self.cursor.execute(query, (bill_number,))
            rows = self.cursor.fetchall()

            # If rows are found
            if rows:
                self.product_Table.delete(*self.product_Table.get_children())  # Clear the table
                for row in rows:
                    mname, qty, pr, bill_date = row

                    # Validate the bill date
                    if (datetime.now().date() - bill_date).days > 5:
                        messagebox.showerror("Error", "This bill is too old (more than 5 days).", parent=self.root)
                        return

                    # Calculate the total amount for the current medicine
                    total_amount = qty * pr

                    # Insert product data into the table
                    self.product_Table.insert("", "end", values=(mname, qty, pr, total_amount))
            else:
                messagebox.showerror("Error", "No matching records found for this bill number.", parent=self.root)
        except mysql.connector.Error as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bills'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):

        index_ = self.sales_list.curselection()
        if index_:
            file_name = self.sales_list.get(index_[0])
            bill_number = file_name.split('.')[0]
            self.var_invoice.set(bill_number)
            self.fetch_product_data(bill_number)
            with open(f'bills/{file_name}', 'r') as file:
                bill_contents = file.read()
                self.bill_area.delete("1.0", END)
                self.bill_area.insert(END, bill_contents)

    def get_data1(self,ev):
        f = self.product_Table.focus()
        content = (self.product_Table.item(f))
        row = content['values']
        self.var_medname.set(row[0])
        self.var_qty.set(row[1])

    def update_qty(self):
        try:
            quantity = int(self.var_qty.get())
            name = str(self.var_medname.get())
            price_per_unit = float(self.product_Table.item(self.product_Table.focus())['values'][2])
            current_quantity = int(self.product_Table.item(self.product_Table.focus())['values'][1])

            # Check if entered quantity is valid
            if quantity > current_quantity:
                messagebox.showerror("Error", "Entered quantity is greater than purchase quantity", parent=self.root)
                return

            # Calculate new price after return (correct for the return scenario)
            new_price = (current_quantity - quantity) * price_per_unit
            self.var_price.set(new_price)

            # Initialize bill amount to 0
            bill_amount = 0
            items = self.product_Table.get_children()

            # Calculate total bill amount for all products, considering returned quantity
            for item in items:
                values = self.product_Table.item(item, 'values')
                qty = int(values[1])
                price_per_unit = float(values[2])
                if values[0] == self.var_medname.get():
                    bill_amount += (current_quantity - quantity) * price_per_unit
                else:
                    bill_amount += qty * price_per_unit

            self.var_blamt.set(bill_amount)

            # Calculate GST and total amount after applying GST
            gst = bill_amount * 0.12
            self.var_gst.set(gst)
            amount = bill_amount - gst
            self.var_amt.set(amount)

            # Fetch customer discount and total amount from the database
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()
            self.cursor.execute(f"SELECT tamt, dct FROM customer WHERE billid = {self.var_invoice.get()}")
            row = self.cursor.fetchone()

            if row:
                tamount, discount = row
                # Apply discount if it's non-zero (10% of bill_amount)
                if discount != 0:
                    discount = bill_amount * 0.1
                self.var_dct.set(discount)
                self.var_npay.set(bill_amount - discount)
                self.var_amtret.set(tamount - (bill_amount - discount))
            else:
                messagebox.showerror("Error", "No data found for the selected bill", parent=self.root)
                return

            # Update customer quantity, total amount, and discount in the database
            try:
                self.cursor.execute(
                    f"UPDATE customer SET qty = CASE WHEN billid = {self.var_invoice.get()} AND mname = '{self.var_medname.get()}' "
                    f"THEN {current_quantity - quantity} ELSE qty END, tamt = CASE WHEN billid = {self.var_invoice.get()} "
                    f"THEN {bill_amount - discount} ELSE tamt END, dct = CASE WHEN billid = {self.var_invoice.get()} "
                    f"THEN {discount} ELSE dct END WHERE billid = {self.var_invoice.get()}"
                )
                con.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update customer data: {str(e)}", parent=self.root)
                return

            # Update inventory quantity
            try:
                self.cursor.execute(
                    f"UPDATE inventory SET quantity = quantity + {quantity} WHERE medicineName = '{name}'"
                )
                con.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update inventory: {str(e)}", parent=self.root)
                return

            # Update stock quantity
            try:
                self.cursor.execute(
                    f"UPDATE stock SET quantity = quantity + {quantity} WHERE medicineName = '{name}'"
                )
                con.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update stock: {str(e)}", parent=self.root)
                return

            # Update bill total amount after return
            try:
                self.cursor.execute(
                    f"UPDATE bill SET totalamount = {bill_amount - discount} WHERE bill_id = {self.var_invoice.get()}"
                )
                con.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update bill total amount: {str(e)}", parent=self.root)
                return

            # Refresh product data after all updates are completed
            self.fetch_product_data(self.var_invoice.get())

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Bill number should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'bills/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
                self.fetch_product_data(self.var_invoice.get())
            else:
                messagebox.showerror("Error", "Invalid Bill Number", parent=self.root)

    def clear(self):
        self.var_invoice.set("")
        self.var_medname.set("")
        self.var_qty.set("")
        self.var_price.set("")
        self.var_amt.set("")
        self.var_gst.set("")
        self.var_blamt.set("")
        self.var_dct.set("")
        self.var_npay.set("")
        self.var_amtret.set("")
        self.bill_area.delete('1.0', END)
        self.product_Table.delete(*self.product_Table.get_children())
        self.show()

    def back(self):
        self.root.destroy()
        os.system("python EmpDash.py")

if __name__ == "__main__":
    root = Tk()
    obj = ReturnClass(root)
    root.mainloop()
