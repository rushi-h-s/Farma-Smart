import         tkinter as tk
from              tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

class AboutUsPage(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("About Us - PharmaSmart")
        self.geometry("1100x700+50+50")
        self.configure(bg="#f0f4f8")

        # Scrollable Canvas
        canvas = tk.Canvas(self, bg="#f0f4f8", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame inside Canvas
        scrollable_frame = tk.Frame(canvas, bg="#f0f4f8")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Placing Canvas and Scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Mouse Scroll Bindings for Windows and MacOS/Linux
        canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        canvas.bind_all("<Button-4>", self.on_mouse_wheel)  # For Linux scroll up
        canvas.bind_all("<Button-5>", self.on_mouse_wheel)  # For Linux scroll down

        # Title Section
        # Title Section
        # title_label = tk.Label(scrollable_frame, text="About Us", font=("Helvetica", 36, "bold"), fg="#008CBA",
        #                        bg="#f0f4f8")
        # title_label.pack(fill="x",pady=(50, 10))  # Adjusted padding for spacing above and below
        #
        # underline_canvas = tk.Canvas(scrollable_frame, width=250, height=2.5, bg="#f0f4f8", highlightthickness=0)
        # underline_canvas.create_line(0, 2, 250, 2, fill="#008CBA", width=2)
        # underline_canvas.pack(pady=(0, 30))  # Reduced padding for closer positioning below the title

        # Project Overview Section
        self.create_section(scrollable_frame, "Project Overview",
                            "\n\tPharmaSmart is an innovative pharmacy management system dedicated to transforming the way pharmacies operate and serve their. "
                            "This platform is designed to modernize pharmacy operations, placing emphasis on efficiency, accuracy, and patient-centeredcare. \t\tOur vision is to create an environment where pharmacists and healthcare providers can focus more on personalized patient interactions while administrative tasks are simplified and optimized. \n\n"
                            "\tBy integrating smart management practices,PharmaSmart aims to ensure that every aspect of a pharmacy's workflow from medication tracking \t\tto patient support—runs smoothly and reliably. "
                            "PharmaSmart aspires to be a trusted partner for pharmacies, helping them adapt to the evolving needs of the healthcare industry and elevate their standards of service."
                            )

        # Meet the Team Section
        self.create_team_section(scrollable_frame)

        # Meet Our Guide Section
        self.create_guide_section(scrollable_frame)

        # Our College Section
        self.create_section(scrollable_frame, "About Our College",
            "\n\t\tThis project was developed as part of our coursework at SSVPS College Dhule. "
            "We aimed to address real-world challenges in \t\tpharmacy management through technology and teamwork.\n")

        # Footer
        footer_label = tk.Label(scrollable_frame, text="\t© 2024 PharmaSmart. All rights reserved.", font=("Helvetica", 14), fg="#8a8a8a", bg="#f0f4f8")
        footer_label.pack(pady=(30, 20))

        self.canvas = canvas

    def on_mouse_wheel(self, event):
        """Scroll canvas using mouse wheel."""
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")

    def create_section(self, parent, title, content):
        """Creates a section in the about page with title, underline, and content centered."""
        # project overview and clg title
        title_label = tk.Label(parent, text=title, font=("Times New Roman", 30, "bold"), fg="#008CBA", bg="#f0f4f8")
        title_label.pack(anchor="center", pady=(30, 0))

        # theirs underlines
        underline_canvas = tk.Canvas(parent, width=200, height=2, bg="#f0f4f8", highlightthickness=0)
        underline_canvas.create_line(0, 1, 200, 1, fill="#008CBA", width=2)
        underline_canvas.pack(anchor="center", pady=(15, 10))

        # for content in it
        content_label = tk.Label(parent, text=content, wraplength=1000, justify="center", bg="#f0f4f8",
                                 font=("Oswald", 14), fg="black")
        content_label.pack(anchor="center", pady=(0, 20))

    def create_team_section(self, parent):
        #title for meet the team
        title_label = tk.Label(parent, text="\t\t\tMeet the Team", font=("Times New Roman", 30, "bold"), fg="#008CBA", bg="#f0f4f8")
        title_label.pack(anchor="w", padx=65, pady=(30, 0))

        # underline for meet the team
        underline_canvas = tk.Canvas(parent, width=200, height=2, bg="#f0f4f8", highlightthickness=0)
        underline_canvas.create_line(0, 1, 155, 1, fill="#008CBA", width=2)
        underline_canvas.pack(anchor="center", pady=(15, 10) , padx=(55, 10))

        team_frame = tk.Frame(parent, bg="#f0f4f8")
        team_frame.pack(anchor="center", padx=65, pady=(10, 20))

        team_members = [
            ("shantanu.png", "Shantanu Shelake"),
            ("rushikesh1.png", "Rushikesh Salunke"),
            ("harshal1.png", "Harshal Baviskar"),
            ("kuldip.png", "Kuldip Girase"),
            ("divesh1.png", "Divesh Patil"),
        ]

        for image_path, name in team_members:
            self.add_team_member(team_frame, image_path, name)

    def add_team_member(self, parent, image_path, name):
        """Adds a team member's circular photo and name to the team section."""
        try:
            image = Image.open(image_path)
            image = image.resize((120, 120), Image.LANCZOS)
            circle_image = ImageTk.PhotoImage(self.create_circle_image(image))
        except Exception as e:
            print(f"Error loading image for {name}: {e}")
            return

        member_frame = tk.Frame(parent, bg="#f0f4f8")
        member_frame.pack(side="left", padx=30, pady=10)

        photo_label = tk.Label(member_frame, image=circle_image, bg="#f0f4f8")
        photo_label.image = circle_image
        photo_label.pack()

        name_label = tk.Label(member_frame, text=name, font=("Oswald", 14), fg="black", bg="#f0f4f8")
        name_label.pack(pady=(5, 0))

    def create_circle_image(self, image):
        """Creates a circular mask for an image."""
        size = (120, 120)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)
        circular_image = Image.new("RGBA", size)
        circular_image.paste(image, (0, 0), mask=mask)
        return circular_image

    def create_guide_section(self, parent):
        """Creates a section to meet the guide, with a photo on the left and description next to it."""
        title_label = tk.Label(parent, text="  Meet Our Guide", font=("Times New Roman", 30, "bold"), fg="#008CBA",
                               bg="#f0f4f8")
        title_label.pack(anchor="center", padx=50, pady=(30, 0))

        # Guide section underline
        underline_canvas = tk.Canvas(parent, width=200, height=2, bg="#f0f4f8", highlightthickness=0)
        underline_canvas.create_line(0, 1, 200, 1, fill="#008CBA", width=2)
        underline_canvas.pack(anchor="center", pady=(15, 10), padx=(10, 0))

        # Frame for guide's image and text
        guide_frame = tk.Frame(parent, bg="#f0f4f8")
        guide_frame.pack(anchor="center", padx=50, pady=(10, 20))

        # Guide details (image path and description only, no name)
        guide_image_path = "BRM.png"  # Replace with your guide's image path
        guide_description = """Name : Prof. Dr. Bhalchandra. R. Mandre\n\nProf. Dr. Bhalchandra. R. Mandre is the Project Guide and Head of the Computer Science Department at SSVPS's Bapusaheb Shivajirao Deore College of Engineering, Dhule. He provided valuable guidance throughout the development process of PharmaSmart, offering constructive feedback, helping refine our ideas, and ensuring we remained focused on our objectives."""

        self.add_guide_member(guide_frame, guide_image_path, guide_description)

    def add_guide_member(self, parent, image_path, description):
        """Adds the guide's image and description to the guide section with the description next to the photo."""
        try:
            # Load and resize the image to fit within the layout
            image = Image.open(image_path)
            image = image.resize((120, 120), Image.LANCZOS)
            circle_image = ImageTk.PhotoImage(self.create_circle_image(image))
        except Exception as e:
            print(f"Error loading guide image: {e}")
            return

        # Create a frame to hold both the image and the description
        guide_frame = tk.Frame(parent, bg="#f0f4f8")
        guide_frame.pack(anchor="center", padx=10, pady=0)

        # Display the guide's image on the left side
        photo_label = tk.Label(guide_frame, image=circle_image, bg="#f0f4f8")
        photo_label.image = circle_image
        photo_label.grid(row=0, column=0, padx=20)

        # Display the guide's description on the right side (no name)
        description_label = tk.Label(guide_frame, text=description, wraplength=700, justify="left", bg="#f0f4f8",
                                     font=("Oswald", 14), fg="black")
        description_label.grid(row=0, column=1, pady=(10, 0), padx=10)


# Run the About Us page
if __name__ == "__main__":
    app = AboutUsPage()
    app.mainloop()
