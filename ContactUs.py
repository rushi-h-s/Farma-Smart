import smtplib
import ssl
from email.message import EmailMessage
from tkinter import messagebox

from connector.ConnectionProvider import ConnectionProvider
import tkinter as tk

class ContactUsPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Contact Us")
        self.geometry("900x650")
        self.configure(bg="#f0f4f8")  # Light background color

        # Left Panel - Contact Information
        left_frame = tk.Frame(self, bg="#f0f4f8")
        left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        tk.Label(left_frame, text="Contact Us", font=("Times New Roman", 28, "bold"), bg="#f0f4f8", fg="#008CBA").pack(
            anchor="w", pady=(10, 10))
        tk.Label(left_frame, text="Email, call, or complete the form to learn how we can help.\n", font=("Oswald", 14),
                 bg="#f0f4f8", fg="black").pack(anchor="w")
        tk.Label(left_frame, text=" divesh.patil@ssvpsengg.ac.in", font=("Oswald", 14, "bold"), bg="#f0f4f8",
                 fg="black").pack(anchor="w", pady=(10, 0))
        tk.Label(left_frame, text="+91  750-744-1435", font=("Oswald", 14, "bold"), bg="#f0f4f8", fg="black").pack(
            anchor="w", pady=(10, 0))

        # Support Sections
        sections = [
            ("Customer Support", "Our support team is available around the clock to address any concerns, providing quick responses and expert assistance to ensure your needs are met."),
            ("Feedback and Suggestions", "We value your feedback and suggestions work to improve our services."),
            ("Media Inquiries", "For media-related questions, please contact us at divesh.patil@ssvpsengg.ac.in. Our team is ready to assist you with press releases, interviews, and any promotional inquiries.")
        ]

        for title, desc in sections:
            tk.Label(left_frame, text=title, font=("Times New Roman", 18, "bold"), bg="#f0f4f8", fg="#008CBA").pack(
                anchor="center", pady=(30, 10))
            tk.Label(left_frame, text=desc, font=("Oswald", 14), bg="#f0f4f8", fg="black", wraplength=400).pack(
                anchor="w")

        # Right Panel - Contact Form
        right_frame = tk.Frame(self, bg="white", relief="groove", bd=2)
        right_frame.pack(side="right", fill="y", padx=20, pady=20, ipadx=20, ipady=20)

        tk.Label(right_frame, text="\t         Get in Touch", font=("Times New Roman", 24, "bold"), bg="white",
                 fg="#008CBA").pack(anchor="w", pady=(10, 10))

        # Form Fields with Underlines Only
        fields = [
            ("   First name", 20),
            ("   Last name", 20),
            ("   Your email", 40),
            ("   Phone number", 20),
            ("   How can we help?", 120)
        ]
        self.form_data = {}  # To store entry and text widget references

        for label, limit in fields:
            tk.Label(right_frame, text=label, font=("Oswald", 14), bg="white", fg="#8a8a8a").pack(anchor="w",
                                                                                                  pady=(10, 0))

            if label.strip() == "How can we help?":
                text_field = tk.Text(right_frame, height=5, wrap="word", bd=0, highlightthickness=0,
                                     bg="white", fg="black", insertbackground="black" ,font = ("Times New Roman",16) )
                text_field.pack(fill="x", padx=15)
                #underline for how we help
                tk.Frame(right_frame, height=2, bg="#D3D3D3").pack(fill="x", padx=17, pady=(0, 0))
                self.form_data[label.strip()] = text_field  # Store the reference
            else:
                entry = tk.Entry(right_frame, width=40, bd=0, highlightthickness=0, relief="flat", bg="white",
                                 fg="black", insertbackground="black", font=("Times New Roman", 16))
                entry.pack(fill="x", padx=15, pady=(10, 5))
                self.form_data[label.strip()] = entry  # Store the reference

                # Set a fixed width for the underline
                tk.Frame(right_frame, width=375, height=2, bg="#D3D3D3").pack(padx=5, pady=(0, 10))

        # Submit Button using Canvas
        self.submit_canvas = tk.Canvas(right_frame, width=120, height=40, bg="white", highlightthickness=0)
        self.submit_canvas.pack(padx=5, pady=(10, 10))

        # Draw the rectangle outline and the text inside the canvas
        self.submit_canvas.create_rectangle(5, 5, 115, 35, outline="#008CBA", width=2)
        self.submit_canvas.create_text(60, 20, text="Submit", fill="#008CBA", font=("Oswald", 14, "bold"))

        # Bind the canvas to act like a button when clicked
        self.submit_canvas.bind("<Button-1>", lambda e: self.submit_action())

        # Change color on hover
        self.submit_canvas.bind("<Enter>", self.on_hover)
        self.submit_canvas.bind("<Leave>", self.on_leave)

        # Terms and Privacy Text
        terms_text = "By contacting us, you agree to our Terms of Service and Privacy Policy."
        tk.Label(right_frame, text=terms_text, font=("Oswald", 12), bg="white", fg="black", wraplength=300).pack(
            anchor="center", padx=5)

    def on_hover(self, event):
        self.submit_canvas.itemconfig(1, outline="black")  # Change outline color to black
        self.submit_canvas.itemconfig(2, fill="black")  # Change text color to black

    def on_leave(self, event):
        self.submit_canvas.itemconfig(1, outline="#008CBA")  # Change outline color back to original
        self.submit_canvas.itemconfig(2, fill="#008CBA")  # Change text color back to original

    def submit_action(self):
        # Collect user data from form
        user_data = {
            "first_name": self.form_data["First name"].get(),
            "last_name": self.form_data["Last name"].get(),
            "email": self.form_data["Your email"].get(),
            "phone": self.form_data["Phone number"].get(),
            "message": self.form_data["How can we help?"].get("1.0", tk.END).strip()
        }

        # Input validation
        if not user_data["first_name"] or not user_data["last_name"] or not user_data["email"] or not user_data[
            "phone"] or not user_data["message"]:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return
        if "@" not in user_data["email"]:
            self.show_temp_message("Please enter a valid email address.")
            return
        try:
            phone_number = int(user_data["phone"])
            if len(user_data["phone"]) > 12:
                self.show_temp_message("Phone number should not exceed 12 digits.")
                return
        except ValueError:
            self.show_temp_message("Please enter a valid phone number.")
            return

        try:
            connection_provider = ConnectionProvider()
            con = connection_provider.get_con()
            cursor = con.cursor()

            # Insert the contact submission into the database
            insert_query = """
            INSERT INTO contact_submissions(first_name, last_name, email, phone, message)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (user_data["first_name"], user_data["last_name"], user_data["email"],
                                          user_data["phone"], user_data["message"]))
            con.commit()

            # Fetch all admin emails
            cursor.execute("SELECT emailid FROM appuser WHERE userRole = 'Admin'")
            admin_emails = [row[0] for row in cursor.fetchall()]

            # Send email to each admin email
            for admin_email in admin_emails:
                self.send_email(user_data, admin_email)

            self.show_temp_message("Data submitted and emailed to admin successfully!")
            self.clear_form_fields()
            cursor.close()
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            if con and con.is_connected():
                con.close()



    def show_temp_message(self, message):
        # Create a label to display the message
        message_label = tk.Label(self, text=message, bg="#f0f4f8", fg="green", font=("Oswald", 14))
        message_label.place(x=250, y=600)
       # message_label.pack(pady=(50, 60))  # Add padding for aesthetics

        # After 2 seconds, destroy the label
        self.after(2000, message_label.destroy)  # 2000 milliseconds = 2 seconds

    def clear_form_fields(self):
        # Clear each form field
        for field in self.form_data:
            if isinstance(self.form_data[field], tk.Entry):  # For entry widgets
                self.form_data[field].delete(0, tk.END)
            elif isinstance(self.form_data[field], tk.Text):  # For text widgets
                self.form_data[field].delete("1.0", tk.END)

    def send_email(self, user_data, admin_email):
        try:
            sender_email = "divesh.patil@ssvpsengg.ac.in"  # Your email address
            password = "smnp ukhw lmfs anov"  # Your email password
            subject = "New Contact Us Form Submission"
            body = f"""
            New Contact Us Submission:

            First Name: {user_data["first_name"]}
            Last Name: {user_data["last_name"]}
            Email: {user_data["email"]}
            Phone: {user_data["phone"]}
            Message: {user_data["message"]}
            """

            # Set up email message
            em = EmailMessage()
            em["From"] = sender_email
            em["To"] = admin_email
            em["Subject"] = subject
            em.set_content(body)

            # Send email using SMTP_SSL
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(sender_email, password)
                smtp.sendmail(sender_email, admin_email, em.as_string())

            print(f"Email sent successfully to {admin_email}")
        except Exception as e:
            print(f"Failed to send email to {admin_email}: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    contact_us_page = ContactUsPage(root)
    contact_us_page.mainloop()
