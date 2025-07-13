# import sqlite3
# from tkinter import *
# from tkinter import messagebox

# # Connect and create database tables
# def init_db():
#     conn = sqlite3.connect("dog_adoption_app.db")
#     c = conn.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             contact TEXT NOT NULL
#         )
#     """)
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS adoptions (
#             adoption_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             dog_name TEXT NOT NULL,
#             breed TEXT NOT NULL,
#             FOREIGN KEY(user_id) REFERENCES users(user_id)
#         )
#     """)
#     conn.commit()
#     conn.close()

# # Function to open adoption window after registration
# def open_adoption_window(user_id):
#     adoption_win = Toplevel()
#     adoption_win.geometry("500x400")
#     adoption_win.title("Choose a Dog to Adopt")

#     Label(adoption_win, text="Dog Name").place(x=50, y=50)
#     dog_name = Entry(adoption_win, width=30)
#     dog_name.place(x=180, y=50)

#     Label(adoption_win, text="Breed").place(x=50, y=100)
#     breed = Entry(adoption_win, width=30)
#     breed.place(x=180, y=100)

#     def adopt_dog():
#         dname = dog_name.get()
#         br = breed.get()

#         if not dname or not br:
#             messagebox.showerror("Error", "Please fill all fields")
#             return

#         conn = sqlite3.connect("dog_adoption_app.db")
#         c = conn.cursor()
#         c.execute("INSERT INTO adoptions (user_id, dog_name, breed) VALUES (?, ?, ?)", (user_id, dname, br))
#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Success", f"You adopted {dname}!")
#         adoption_win.destroy()

#     Button(adoption_win, text="Adopt", bg="green", fg="white", command=adopt_dog).place(x=200, y=150)

# # # Main registration window
# # def main_window():
# #     root = Tk()
# #     root.geometry("500x400")
# #     root.title("Dog Adoption App - Register")

# #     Label(root, text="User Registration", font=("Arial", 16, "bold"), fg="blue").place(x=130, y=30)

# #     Label(root, text="Full Name").place(x=50, y=100)
# #     name_entry = Entry(root, width=35)
# #     name_entry.place(x=180, y=100)

# #     Label(root, text="Contact Number").place(x=50, y=150)
# #     contact_entry = Entry(root, width=35)
# #     contact_entry.place(x=180, y=150)

# #     def register_user():
# #         name = name_entry.get()
# #         contact = contact_entry.get()

# #         if not name or not contact:
# #             messagebox.showerror("Error", "Please fill all fields")
# #             return

# #         conn = sqlite3.connect("dog_adoption_app.db")
# #         c = conn.cursor()
# #         c.execute("INSERT INTO users (name, contact) VALUES (?, ?)", (name, contact))
# #         user_id = c.lastrowid  # get the ID of the inserted user
# #         conn.commit()
# #         conn.close()

# #         messagebox.showinfo("Registered", f"Welcome {name}!\nNow choose a dog.")
# #         root.withdraw()  # hide registration window
# #         open_adoption_window(user_id)

# #     Button(root, text="Register", bg="green", fg="white", font=("Arial", 11), command=register_user).place(x=200, y=220)

# #     root.mainloop()

# # # Run everything
# # init_db()
# # main_window()

# import sqlite3
# from tkinter import *
# from tkinter import messagebox

# # -------------------- Initialize DB --------------------
# def init_db():
#     conn = sqlite3.connect("dog_adoption_app.db")
#     c = conn.cursor()

#     # Users table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             contact TEXT NOT NULL
#         )
#     """)

#     # Dogs table (list of available dogs)
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS dogs (
#             dog_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             dog_name TEXT NOT NULL,
#             breed TEXT NOT NULL
#         )
#     """)

#     # Adoptions table (records adoption)
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS adoptions (
#             adoption_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             dog_id INTEGER,
#             FOREIGN KEY(user_id) REFERENCES users(user_id),
#             FOREIGN KEY(dog_id) REFERENCES dogs(dog_id)
#         )
#     """)

#     # Insert sample dogs if not already present
#     c.execute("SELECT COUNT(*) FROM dogs")
#     count = c.fetchone()[0]
#     if count == 0:
#         sample_dogs = [
#             ('Buddy', 'Golden Retriever'),
#             ('Max', 'German Shepherd'),
#             ('Bella', 'Labrador'),
#             ('Lucy', 'Beagle'),
#             ('Charlie', 'Pug'),
#             ('Rocky', 'Bulldog')
#         ]
#         c.executemany("INSERT INTO dogs (dog_name, breed) VALUES (?, ?)", sample_dogs)

#     conn.commit()
#     conn.close()

# # -------------------- Adoption Window --------------------
# def open_adoption_window(user_id):
#     adoption_win = Toplevel()
#     adoption_win.geometry("600x500")
#     adoption_win.title("Available Dogs for Adoption")

#     Label(adoption_win, text="Search Dogs", font=("Arial", 12, "bold")).place(x=20, y=20)
#     search_entry = Entry(adoption_win, width=30)
#     search_entry.place(x=150, y=20)

#     def load_dogs(filter_text=""):
#         for widget in dogs_frame.winfo_children():
#             widget.destroy()

#         conn = sqlite3.connect("dog_adoption_app.db")
#         c = conn.cursor()
#         if filter_text:
#             c.execute("SELECT * FROM dogs WHERE dog_name LIKE ? OR breed LIKE ?", (f'%{filter_text}%', f'%{filter_text}%'))
#         else:
#             c.execute("SELECT * FROM dogs")
#         dogs = c.fetchall()
#         conn.close()

#         if not dogs:
#             Label(dogs_frame, text="No dogs found.").pack()
#             return

#         for dog in dogs:
#             dog_id, dog_name, breed = dog
#             frame = Frame(dogs_frame, pady=5, padx=5, relief="solid", borderwidth=1)
#             Label(frame, text=f"Name: {dog_name}").pack(anchor="w")
#             Label(frame, text=f"Breed: {breed}").pack(anchor="w")
#             Button(frame, text="Adopt", bg="green", fg="white",
#                    command=lambda d_id=dog_id, d_name=dog_name: adopt_dog(user_id, d_id, d_name, adoption_win)
#             ).pack(anchor="e")
#             frame.pack(fill="x", padx=10, pady=5)

#     def search_dogs():
#         filter_text = search_entry.get().strip()
#         load_dogs(filter_text)

#     Button(adoption_win, text="Search", command=search_dogs).place(x=400, y=17)

#     dogs_frame = Frame(adoption_win)
#     dogs_frame.place(x=20, y=60, width=560, height=400)

#     load_dogs()

# def adopt_dog(user_id, dog_id, dog_name, window):
#     conn = sqlite3.connect("dog_adoption_app.db")
#     c = conn.cursor()

#     # Check if this user has already adopted this dog
#     c.execute("SELECT * FROM adoptions WHERE user_id = ? AND dog_id = ?", (user_id, dog_id))
#     if c.fetchone():
#         messagebox.showinfo("Already Adopted", f"You have already adopted {dog_name}.")
#     else:
#         c.execute("INSERT INTO adoptions (user_id, dog_id) VALUES (?, ?)", (user_id, dog_id))
#         conn.commit()
#         messagebox.showinfo("Success", f"You adopted {dog_name}!")
#     conn.close()
#     window.destroy()

# # -------------------- Registration Window --------------------
# def main_window():
#     root = Tk()
#     root.geometry("500x400")
#     root.title("Dog Adoption App - Register")

#     Label(root, text="User Registration", font=("Arial", 16, "bold"), fg="blue").place(x=130, y=30)

#     Label(root, text="Full Name").place(x=50, y=100)
#     name_entry = Entry(root, width=35)
#     name_entry.place(x=180, y=100)

#     Label(root, text="Contact Number").place(x=50, y=150)
#     contact_entry = Entry(root, width=35)
#     contact_entry.place(x=180, y=150)

#     def register_user():
#         name = name_entry.get().strip()
#         contact = contact_entry.get().strip()

#         if not name or not contact:
#             messagebox.showerror("Error", "Please fill all fields")
#             return

#         if not contact.isdigit():
#             messagebox.showerror("Error", "Contact must be numbers only")
#             return

#         conn = sqlite3.connect("dog_adoption_app.db")
#         c = conn.cursor()
#         c.execute("INSERT INTO users (name, contact) VALUES (?, ?)", (name, contact))
#         user_id = c.lastrowid
#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Registered", f"Welcome {name}! Choose a dog to adopt.")
#         root.withdraw()
#         open_adoption_window(user_id)

#     Button(root, text="Register", bg="green", fg="white", font=("Arial", 11), command=register_user).place(x=200, y=220)

#     root.mainloop()

# # -------------------- Run the App --------------------
# init_db()
# main_window()


import sqlite3
from tkinter import *
from tkinter import messagebox

# -------------------- Initialize DB --------------------
def init_db():
    conn = sqlite3.connect("dog_adoption_app.db")
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
            dog_id INTEGER PRIMARY KEY AUTOINCREMENT,
            dog_name TEXT NOT NULL,
            breed TEXT NOT NULL
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
            FOREIGN KEY(dog_id) REFERENCES dogs(dog_id)
        )
    """)

    # Insert sample dogs if not already present
    c.execute("SELECT COUNT(*) FROM dogs")
    count = c.fetchone()[0]
    if count == 0:
        sample_dogs = [
            ('Buddy', 'Golden Retriever'),
            ('Max', 'German Shepherd'),
            ('Bella', 'Labrador'),
            ('Lucy', 'Beagle'),
            ('Charlie', 'Pug')
        ]
        c.executemany("INSERT INTO dogs (dog_name, breed) VALUES (?, ?)", sample_dogs)

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

        conn = sqlite3.connect("dog_adoption_app.db")
        c = conn.cursor()

        # Prevent duplicate adoption
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
    list_win.geometry("500x500")
    list_win.title("Available Dogs for Adoption")

    Label(list_win, text="Available Dogs", font=("Arial", 16, "bold")).pack(pady=10)

    search_entry = Entry(list_win, width=30)
    search_entry.pack(pady=5)

    def load_dogs(filter_text=""):
        for widget in dogs_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect("dog_adoption_app.db")
        c = conn.cursor()
        if filter_text:
            c.execute("SELECT * FROM dogs WHERE dog_name LIKE ? OR breed LIKE ?", (f'%{filter_text}%', f'%{filter_text}%'))
        else:
            c.execute("SELECT * FROM dogs")
        dogs = c.fetchall()
        conn.close()

        if not dogs:
            Label(dogs_frame, text="No dogs found.").pack()
            return

        for dog in dogs:
            dog_id, dog_name, breed = dog
            frame = Frame(dogs_frame, pady=5, padx=5, relief="ridge", borderwidth=1)
            Label(frame, text=f"Name: {dog_name}", font=("Arial", 12)).pack(anchor="w")
            Label(frame, text=f"Breed: {breed}", font=("Arial", 12)).pack(anchor="w")
            Button(
                frame,
                text="Adopt This Dog",
                bg="blue", fg="white",
                command=lambda d_id=dog_id, d_name=dog_name, br=breed: open_adoption_form(user_id, d_id, d_name, br)
            ).pack(anchor="e", pady=5)
            frame.pack(fill="x", padx=20, pady=5)

    def search_dogs():
        filter_text = search_entry.get().strip()
        load_dogs(filter_text)

    Button(list_win, text="Search", command=search_dogs).pack()

    dogs_frame = Frame(list_win)
    dogs_frame.pack(fill="both", expand=True)

    load_dogs()

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

        conn = sqlite3.connect("dog_adoption_app.db")
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

# -------------------- Run the App --------------------
init_db()
main_window()

    
