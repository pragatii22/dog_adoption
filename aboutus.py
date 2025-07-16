import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

# -------------------- Initialize Combined DB --------------------
def init_db():
    conn = sqlite3.connect("happy_hooves.db")
    c = conn.cursor()

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    """)

    # Dogs table
    c.execute("""
        CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            breed TEXT,
            image TEXT
        )
    """)

    # Adoptions table
    c.execute("""
        CREATE TABLE IF NOT EXISTS adoptions (
            adoption_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            dog_id INTEGER,
            address TEXT,
            notes TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(dog_id) REFERENCES dogs(id)
        )
    """)

    # Insert sample dogs if empty
    c.execute("SELECT COUNT(*) FROM dogs")
    if c.fetchone()[0] == 0:
        sample_dogs = [
            ("Black Labrador", "Labrador", "image/lab.jpeg"),
            ("Golden Retriever", "Retriever", "image/golden.jpeg"),
            ("Pug", "Pug", "image/pug.jpeg")
        ]
        c.executemany("INSERT INTO dogs (name, breed, image) VALUES (?, ?, ?)", sample_dogs)

    conn.commit()
    conn.close()

# -------------------- Adoption Application Form --------------------
def open_adoption_form(user_id, dog_id, dog_name, breed):
    form_win = Toplevel()
    form_win.geometry("400x400")
    form_win.title("Adoption Application Form")

    Label(form_win, text=f"Adopt {dog_name} ({breed})", font=("Arial", 14, "bold")).pack(pady=10)

    Label(form_win, text="Your Address").pack(anchor="w", padx=20)
    address_entry = Text(form_win, height=4, width=40)
    address_entry.pack(padx=20, pady=5)

    Label(form_win, text="Additional Notes").pack(anchor="w", padx=20)
    notes_entry = Text(form_win, height=4, width=40)
    notes_entry.pack(padx=20, pady=5)

    def submit_application():
        address = address_entry.get("1.0", END).strip()
        notes = notes_entry.get("1.0", END).strip()

        if not address:
            messagebox.showerror("Error", "Address cannot be empty")
            return

        conn = sqlite3.connect("happy_hooves.db")
        c = conn.cursor()
        c.execute("SELECT * FROM adoptions WHERE user_id = ? AND dog_id = ?", (user_id, dog_id))
        if c.fetchone():
            messagebox.showinfo("Already Applied", "You have already applied for this dog.")
        else:
            c.execute(
                "INSERT INTO adoptions (user_id, dog_id, address, notes) VALUES (?, ?, ?, ?)",
                (user_id, dog_id, address, notes)
            )
            conn.commit()
            messagebox.showinfo("Success", f"Your application for {dog_name} is submitted!")
        conn.close()
        form_win.destroy()

    Button(form_win, text="Submit Application", bg="green", fg="white", command=submit_application).pack(pady=20)

# -------------------- Dog Listings --------------------
def open_dog_listings(user_id):
    list_win = Toplevel()
    list_win.geometry("800x900")
    list_win.title("Available Dogs for Adoption")

    # GUI setup merged here
    root = list_win
    root.configure(bg="white")

    header = Frame(root, bg="#f7f7f7", pady=10)
    header.pack(fill=X)

    try:
        logo_img = Image.open("image/paw.jpeg").resize((60, 60))
        logo = ImageTk.PhotoImage(logo_img)
        logo_frame = Frame(header, bg="#f7f7f7")
        logo_frame.pack(side=LEFT, padx=10)
        Label(logo_frame, image=logo, bg="#f7f7f7").pack()
        Label(logo_frame, text="Logo", font=("Arial", 10, "italic"), bg="#f7f7f7").pack()
    except Exception:
        Label(header, text="Logo not found", font=("Arial", 12), bg="#f7f7f7").pack(side=LEFT, padx=10)

    Label(header, text="Heaven of Happy Hooves", font=("Helvetica", 20, "bold"), bg="#f7f7f7").pack(side=LEFT)

    navbar = Frame(root, bg="#dcdcdc")
    navbar.pack(fill=X)
    for name in ["Home", "About Us", "Accessories", "Available Dogs", "Contact Us"]:
        Button(navbar, text=name, relief=FLAT, bg="#dcdcdc", padx=15).pack(side=LEFT, padx=5)

    hero = Frame(root, bg="white", pady=20)
    hero.pack()
    hero_img = ImageTk.PhotoImage(Image.open("image/brown.jpeg").resize((600, 250)))
    Label(hero, image=hero_img, bg="white").pack()
    Label(hero, text='"In every act of giving, there\'s a touch of love."', font=("Arial", 14, "italic"), bg="white", pady=10).pack()

    about = Frame(root, bg="white", padx=20, pady=20)
    about.pack(fill=X)
    Label(about, text='About "Heaven of Happy Hooves"', font=("Helvetica", 16, "bold"), bg="white").pack(anchor=W)
    Label(about, text=(
        "Heaven of Happy Hooves started with six golden retriever stray puppies.\n"
        "It was very sad to see those dogs hoping for food, a home, and a loving human.\n"
        "Slowly starting with six puppies, today this shelter has given happy homes to\n"
        "78 dogs and puppies and yet has a lot more to save and give them a new life."
    ), bg="white", justify=LEFT).pack(anchor=W)

    friends = Frame(root, bg="white", pady=20)
    friends.pack()
    Label(friends, text="Our Friends Who Are Looking for a Home", font=("Helvetica", 16, "bold"), bg="white").pack()
    gallery = Frame(friends, bg="white")
    gallery.pack(pady=10)

    conn = sqlite3.connect("happy_hooves.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, breed, image FROM dogs")
    dogs = cursor.fetchall()
    conn.close()

    dog_images = []

    for dog in dogs:
        dog_id, name, breed, img_path = dog
        if not img_path.startswith("image/"):
            img_path = "image/" + img_path
        card = Frame(gallery, bd=1, relief=SOLID, padx=10, pady=10, bg="white")
        card.pack(side=LEFT, padx=10)

        try:
            img = Image.open(img_path).resize((150, 150))
            photo = ImageTk.PhotoImage(img)
            dog_images.append(photo)
            Label(card, image=photo, bg="white").pack()
        except:
            Label(card, text="Image not found", bg="white").pack()

        Label(card, text=name, font=("Arial", 12), bg="white").pack()
        Button(card, text="Adopt", bg="blue", fg="white",
               command=lambda d_id=dog_id, d_name=name, br=breed: open_adoption_form(user_id, d_id, d_name, br)
        ).pack(pady=5)

    footer = Frame(root, bg="#e6e6e6", pady=10)
    footer.pack(side=BOTTOM, fill=X)
    Label(footer, text="© 2025 Heaven of Happy Hooves. All rights reserved.", bg="#e6e6e6").pack()

# -------------------- Registration Window --------------------
def main_window():
    root = Tk()
    root.geometry("500x400")
    root.title("Dog Adoption App - Register")

    Label(root, text="User Registration", font=("Arial", 16, "bold"), fg="blue").place(x=130, y=30)

    Label(root, text="Full Name").place(x=50, y=100)
    name_entry = Entry(root, width=35)
    name_entry.place(x=180, y=100)

    Label(root, text="Contact Number").place(x=50, y=150)
    contact_entry = Entry(root, width=35)
    contact_entry.place(x=180, y=150)

    def register_user():
        name = name_entry.get().strip()
        contact = contact_entry.get().strip()

        if not name or not contact:
            messagebox.showerror("Error", "Please fill all fields")
            return
        if not contact.isdigit():
            messagebox.showerror("Error", "Contact must be numbers only")
            return

        conn = sqlite3.connect("happy_hooves.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, contact) VALUES (?, ?)", (name, contact))
        user_id = c.lastrowid
        conn.commit()
        conn.close()

        messagebox.showinfo("Registered", f"Welcome {name}! Browse dogs to adopt.")
        root.withdraw()
        open_dog_listings(user_id)

    Button(root, text="Register", bg="green", fg="white", font=("Arial", 11), command=register_user).place(x=200, y=220)
    root.mainloop()




# -------------------- Start App --------------------
init_db()
main_window()



