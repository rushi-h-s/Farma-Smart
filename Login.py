from tkinter import *
from tkinter import messagebox, ttk
import os
import smtplib
import time
from PIL import Image, ImageTk
from connector.ConnectionProvider import ConnectionProvider
from BackgroundPage import BackgroundPage

class BackgroundPage:
    def __init__(self, root):
        self.root = root
        self.raw_image = Image.open("login.png")
        self.raw_image = self.raw_image.resize((1350, 700))
        self.img = ImageTk.PhotoImage(self.raw_image)

        # Assign the image to the label and keep a reference to it
        self.panel = Label(root, image=self.img)
        self.panel.image = self.img  # Explicitly keep a reference to avoid garbage collection
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)


class loginClass:
    cursor=None
    email_ = 'divesh.patil@ssvpsengg.ac.in'
    pass_ = 'smnp ukhw lmfs anov'
    def __init__(self, root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#d8f9ff")
        self.root.focus_force()
        self.root.resizable(False, False)
        self.otp=''
        BackgroundPage(root)
        #login_frame

        self.password=StringVar()
        self.user_name=StringVar()
        self.master=StringVar()
        self.txt_pass = None
        self.ch_pass = None
        login_frame = Frame(self.root, bd=2, bg="#FFFFFF", highlightthickness=3, highlightbackground="#E0E0E0")
        login_frame.place(x=720, y=120, width=400, height=500)
        title = Label(login_frame, text="Login", font=("Helvetica Neue", 30, "bold"), bg="white", fg="#333333")
        title.place(x=135, y=30)

        lbl_user=Label(login_frame,text="User Name",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.user_name,font=("times new roman",15),bg="#ebf3fb" ,fg="black").place(x=50,y=140,width=250)

        title = Label(self.root, text="PharmaSmart", font=("times new roman", 40, "bold"), bg="lightsteelblue1", fg="steelblue3").place(x=90,y=220)
       # title = Label(self.root, text="System", font=("times new roman", 40, "bold"), bg="lightsteelblue1", fg="steelblue3").place(x=280,y=287)



        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50,
                                                                                                             y=200)
        self.txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15),bg="#ebf3fb" ,fg="black")
        self.txt_pass.place(x=50, y=240, width=250)
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#4585f4",activebackground="#00B0F0",fg="black",activeforeground="white",cursor="hand2").place(x=50,y=315,width=250,height=35)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_= Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150, y=355)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_win,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=110,y=398)
        self.ch_pass = ttk.Checkbutton(login_frame, text="Show Password", command=self.toggle_password,style='TCheckbutton')
        self.ch_pass.place(x=50, y=280, width=250)



    #ALL FUNCTIONS

    def login(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()

            if self.user_name.get() == "" or self.password.get() == "":
                messagebox.showerror('Error', "All fields are required", parent=self.root)
            else:
                self.cursor.execute("SELECT password, userRole FROM appuser WHERE username=%s", (self.user_name.get(),))
                user = self.cursor.fetchone()
                self.userrole=user[0]
                if user is None:
                    messagebox.showerror('Error', "Invalid Username/Password", parent=self.root)
                else:
                    if user[0] == self.password.get():
                        if user[1] == "Admin":
                            self.root.destroy()
                            os.system("python Admin.py")
                        elif user[1] == "Employee":
                            self.root.destroy()
                            os.system("python Empdash.py")
                        else:
                            messagebox.showerror('Error', "Invalid User Role", parent=self.root)
                    else:
                        messagebox.showerror('Error', "Invalid Username/Password", parent=self.root)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def toggle_password(self):
        if self.ch_pass.instate(['selected']):
            self.txt_pass.configure(show="")
        else:
            self.txt_pass.configure(show="*")

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def forget_win(self):
        connection_provider = ConnectionProvider()
        con = connection_provider.get_con()
        self.cursor = con.cursor()
        try:
                #FORGET WINDOW
                self.var_otp=StringVar()
                self.newpas=StringVar()
                self.conpas=StringVar()
                self.var_id=StringVar()
                self.master=StringVar()

                self.forget_win=Toplevel(self.root)
                self.forget_win.title('FORGET PASSWORD')
                self.forget_win.geometry('400x350+500+100')
                self.forget_win.focus_force()

                self.forget_win.resizable(False, False)

                title=Label(self.forget_win,text='Reset Password',font=('houdy old style ',15,'bold'),bg="#4285f4",fg="white").pack(side=TOP,fill=X)
                lbl_fid = Label(self.forget_win, text="User Name",font=("times new roman", 15)).place(x=20, y=40)

                txt_master = Entry(self.forget_win, textvariable=self.master, font=("times new roman", 15),bg='#ebf3fb' , fg="black").place(x=20, y=70, width=250, height=30)
                self.btn_send = Button(self.forget_win, text="SEND", command=self.chk,font=("times new roman", 15), bg='lightblue')
                self.btn_send.place(x=280, y=70, width=100, height=30)


                lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("times new roman",15)).place(x=20,y=105)
                txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg='#ebf3fb' , fg="black").place(x=20,y=135,width=250,height=30)
                self.btn_reset = Button(self.forget_win, text="SUBMIT",command=self.validate_otp, font=("times new roman", 15), bg='lightblue')
                self.btn_reset.place(x=280, y=135, width=100, height=30)
                lbl_newpas = Label(self.forget_win, text='New Password',font=("times new roman",15)).place(x=20,y=170)
                txt_newpas = Entry(self.forget_win,show="*",textvariable=self.newpas,font=("times new roman", 15),bg='#ebf3fb', fg="black").place(x=20, y=200,width=250,height=30)
                lbl_conpas= Label(self.forget_win, text='Confirm Password',font=("times new roman",15)).place(x=20,y=235)
                txt_conpas = Entry(self.forget_win,show="*",textvariable=self.conpas,font=("times new roman", 15),bg='#ebf3fb' , fg="black").place(x=20, y=265,width=250,height=30)

                self.btn_update = Button(self.forget_win, text="Update",command=self.update_password,state=DISABLED, font=("times new roman", 15), bg='lightblue')
                self.btn_update.place(x=150, y=310, width=100, height=30)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def chk(self):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()
            if self.master.get() == "":
                messagebox.showerror('Error', "User Name must be required", parent=self.root)
            else:
                self.cursor.execute("SELECT emailid FROM appuser WHERE username=%s", (self.master.get(),))
                email = self.cursor.fetchone()
                if email is None:
                    messagebox.showerror('Error', "Invalid User Name, try again", parent=self.root)
                else:
                    chk = self.send_email(email[0])
                    if chk == 'f':
                        messagebox.showerror("Error", "Connection Error, try again", parent=self.root)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def update_password(self):
        if self.newpas.get() == "" or self.conpas.get() == "":
            messagebox.showerror("Error", "Password is required", parent=self.root)
        elif self.newpas.get() != self.conpas.get():
            messagebox.showerror("Error", "Password & confirm password should be same", parent=self.root)
        else:
            try:
                if int(self.otp) == int(self.var_otp.get()):

                    self.btn_update.config(state=NORMAL)
                    self.btn_reset.config(state=DISABLED)
                else:
                    messagebox.showerror("Error", "Invalid OTP, Try again", parent=self.forget_win)
                connection_provider = ConnectionProvider()
                con = connection_provider.get_con()
                self.cursor = con.cursor()
                self.cursor.execute("UPDATE appuser SET password=%s WHERE username=%s", (self.conpas.get(), self.master.get()))
                con.commit()
                messagebox.showinfo("Success", "Password updated successfully", parent=self.root)
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):

            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try again",parent=self.forget_win)

    def send_email(self, to_):
        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            self.cursor = con.cursor()

            self.cursor.execute("SELECT emailid FROM appuser WHERE username=%s", (self.master.get(),))
            email_result = self.cursor.fetchone()
            if email_result is None:
                messagebox.showerror('Error', "Invalid User Name, try again", parent=self.root)
                return 'f'

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(self.email_, self.pass_)
            self.otp = int(time.strftime("%H%S%M")) + int(time.strftime("%S"))
            subj = 'Reset Password OTP'
            msg = f'Dear Sir/Madam, \n\n Your Reset OTP is {str(self.otp)}.\n\n Best Regards,\n Pharmacy Management System'
            msg = "Subject:{}\n\n{}".format(subj, msg)
            s.sendmail(self.email_, email_result[0], msg)
            chk = s.ehlo()
            if chk[0] == 250:
                return 's'
            else:
                return 'f'
        except Exception as ex:
            messagebox.showerror("Error", f"Error sending email: {str(ex)}", parent=self.root)
            return 'f'

if __name__ == "__main__":
    root = Tk()
    obj = loginClass(root)
    root.mainloop()
