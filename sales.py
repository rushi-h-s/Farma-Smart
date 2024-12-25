import datetime
import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        self.raw_image = self.raw_image.resize((1000, 780))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = tk.Label(root, image=self.img)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)  # Fill entire window
        self.panel.image = self.img
class sales:
    def __init__(self, root):
        self.profit = 0
        self.expenses = 0
        self.turnover = 0
        self.root = root
        self.root.title("Store Profit, Expenses, and Turnover")
        self.root.geometry("1000x780")
        BackgroundPage(root)

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=20)


        self.month=ttk.Combobox(self.frame,font=("Helventica",12),state="readonly")
        self.month["values"]=("1","2","3","4","5","6","7","8","9","10","11","12")
        self.month.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        self.year = ttk.Combobox(self.frame, font=("Helventica", 12), state="readonly")
        self.year["values"] = ("2019", "2020", "2021", "2022", "2023", "2024")
        self.year.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.profit_label = tk.Label(self.frame, text="Profit: 0.00", bg="lightgreen",fg="black", font=("Helvetica", 12))
        self.profit_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.expenses_label = tk.Label(self.frame, text="Expenses: 0.00", bg="yellow", fg="black", font=("Helvetica", 12))
        self.expenses_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.turnover_label = tk.Label(self.frame, text="Turnover: 0.00", bg="lightblue",fg="black", font=("Helvetica", 12))
        self.turnover_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.calculate_button = tk.Button(self.frame, text="Calculate", command=self.calculate_profit_turnover,
                                          bg="#4CAF50", fg="black", font=("Helvetica", 12))
        self.calculate_button.grid(row=4, column=0, pady=10)
        self.chart_button = tk.Button(self.frame, text="Show Chart", command=self.loaddata,
                                      bg="#4CAF50", fg="black", font=("Helvetica", 12))

        self.go_back = tk.Button(self.frame, text="Back", command=self.back,
                                          bg="#4CAF50", fg="black", font=("Helvetica", 12))
        self.go_back.grid(row=4, column=2, pady=10)
        self.chart_button.grid(row=4, column=1, pady=10 )
        self.chart_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.chart_frame.pack(pady=20)

        self.backbtn=tk.Button(self.frame,text="Back",command=self.back)

    def back(self):
        from Admin import Admin
        self.root.destroy()
        root = tk.Tk()
        app = Admin(root)
        root.mainloop()

    def calculate_profit_turnover(self):
        # Here you can add your logic to calculate profit, expenses, and turnover
        # For demonstration, let's assume profit, expenses, and turnover are calculated based on some data
        # You can replace this with your actual calculation logic
        month=self.month.get()
        year=self.year.get()
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()
            cursor.execute("select revenue,profit,expense from sales where month=%s and year=%s",(month,year))
            result=cursor.fetchone()
            if result:
                self.turnover = result[0]
                self.profit = result[1]
                self.expenses = result[2]
            else:
                tk.messagebox.showinfo("","No record")
            con.commit()
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        self.profit_label.config(text=f"Profit: {self.profit}Rs")
        self.expenses_label.config(text=f"Expenses: {self.expenses}Rs")
        self.turnover_label.config(text=f"Turnover: {self.turnover}Rs")

    def loaddata(self):

        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            # Your SQL query to fetch data for the chart
            # Calculate the start and end dates for the last 6 months
            current_year = datetime.date.today().year
            current_month = datetime.date.today().month
            start_year = current_year
            start_month = current_month - 5
            if start_month <= 0:
                start_month += 12
                start_year -= 1

            # Fetch data for the last 6 months from the database
            cursor.execute("""
                         SELECT profit, month, year 
                         FROM sales 
                         WHERE (year * 12 + month) BETWEEN %s AND %s
                     """, ((start_year * 12 + start_month), (current_year * 12 + current_month)))

            # Fetch all rows from the query result
            rows = cursor.fetchall()

            # Initialize lists to store profit and month-year strings
            profit_data = []
            month_data = []

            # Update profit and month lists with fetched data
            for row in rows:
                profit_data.append(row[0])
                month_year_string = f"{row[1]}-{row[2]}"
                month_data.append(month_year_string)

            con.commit()
            con.close()

            for widget in self.chart_frame.winfo_children():
                widget.destroy()

            # Plot the bar chart
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(month_data, profit_data, color='skyblue')
            ax.set_xlabel('Months')
            ax.set_ylabel('Profit')
            ax.set_title('Profit for Last 6 Months')
            plt.xticks( ha='center')
            plt.tight_layout()

            # Embed the chart in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            # Embed the chart in the Tkinter window
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()

    app = sales(root)
    root.mainloop()
