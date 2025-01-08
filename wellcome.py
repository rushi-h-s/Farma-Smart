import tkinter as tk
from tkinter import *

from AboutUs import AboutUsPage
from ContactUs import ContactUsPage
from Login import loginClass


class PharmaSmartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to PharmaSmart")
        self.root.geometry("1400x700+50+50")
        self.root.configure(bg="#f0f4f8")  # Light background for a clean look

        # Frame for Buttons at the Top
        self.button_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.button_frame.pack(pady=70)

        # Create hover effect buttons
        self.create_hover_button("Login", self.open_login, 0)
        self.create_hover_button("About Us", self.open_about, 1)
        self.create_hover_button("Contact Us", self.open_contact, 2)

        # Main Frame for Centered Title and Subtitle
        self.center_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.center_frame.pack(expand=True)

        # Title Label in the Center
        self.title_label = tk.Label(self.center_frame, text="Welcome to PharmaSmart", font=("Helvetica", 70, "bold"), fg="#008CBA", bg="#f0f4f8")
        self.title_label.pack(pady=(0,90))

        # Subtitle Label in the Center
        self.subtitle_label = tk.Label(self.center_frame, text="", font=("Times New Roman", 25), fg="#4b4b4b",
                                       bg="#f0f4f8")
        self.subtitle_label.pack(pady=(0,70))

        # Start the animation for the subtitle
        self.subtitle_text = "Your One-Stop Solution for Pharmacy Management"
        self.display_subtitle()

        # Footer
        self.footer_label = tk.Label(self.root, text="© 2024 PharmaSmart, All Rights Reserved", font=("Helvetica", 14), fg="#8a8a8a", bg="#f0f4f8")
        self.footer_label.pack(side="bottom", pady=10)

    def display_subtitle(self, index=0):
        # Display one letter at a time
        if index < len(self.subtitle_text):
            self.subtitle_label.config(text=self.subtitle_label.cget("text") + self.subtitle_text[index])
            self.root.after(100, self.display_subtitle, index + 1)  # Adjust the delay (in ms) as needed

    def create_hover_button(self, text, command, column):
        # Create a text-only button with hover effect
        button = tk.Label(self.button_frame, text=text, font=("Helvetica", 18, "bold"), fg="#008CBA", bg="#f0f4f8", cursor="hand2")
        button.grid(row=0, column=column, padx=50, pady=5)

        # Bind hover effects
        button.bind("<Enter>", lambda e: button.config(fg="black"))  # Hover color
        button.bind("<Leave>", lambda e: button.config(fg="#008CBA"))  # Original color
        button.bind("<Button-1>", lambda e: command())  # Click action

    def open_login(self):
        login_root = tk.Toplevel(self.root)  # New window from the main one
        login_screen = loginClass(login_root)  # Assuming loginClass is your Login screen
        login_root.mainloop()

    def open_about(self):
        print("About Us screen opened")
        about_window = AboutUsPage()  # Create an instance of AboutUsPage
        # No need to call about_window.mainloop() if using Toplevel

    def open_contact(self):
        print("Contact Us screen opened")  # Replace with actual function
        contact_page = ContactUsPage(self.root)  # Pass the main window to ContactUsPage




# Run the app
root = tk.Tk()
app = PharmaSmartApp(root)
root.mainloop()
