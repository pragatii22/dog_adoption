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

    # Adoptions table — includes questions now
    c.execute("""
        CREATE TABLE IF NOT EXISTS adoptions (
            adoption_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            dog_id INTEGER,
            address TEXT,
            reason TEXT,
            experience TEXT,
            agree TEXT,
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


    

from tkinter import *
from tkinter import messagebox

def open_payment_window(user_id, dog_name):
    payment_win = Toplevel()
    payment_win.geometry("400x350")
    payment_win.title("Payment Process")

    Label(payment_win, text="Payment Page", font=("Arial", 16, "bold")).pack(pady=20)
    Label(payment_win, text=f"You are paying for adopting: {dog_name}", font=("Arial", 12)).pack(pady=10)

    Label(payment_win, text="Select Payment Method:").pack(anchor="w", padx=20)
    method_var = StringVar()
    method_var.set("Credit Card")

    Radiobutton(payment_win, text="Credit Card", variable=method_var, value="Credit Card").pack(anchor="w", padx=40)
    Radiobutton(payment_win, text="PayPal", variable=method_var, value="PayPal").pack(anchor="w", padx=40)
    Radiobutton(payment_win, text="Debit Card", variable=method_var, value="Debit Card").pack(anchor="w", padx=40)

    Label(payment_win, text="Enter Card/Account Number:").pack(anchor="w", padx=20)
    payment_entry = Entry(payment_win, width=30)
    payment_entry.pack(padx=20, pady=5)

    Label(payment_win, text="Amount (USD):").pack(anchor="w", padx=20)
    amount_entry = Entry(payment_win, width=30)
    amount_entry.insert(0, "50")  # Example fixed fee
    amount_entry.pack(padx=20, pady=5)

    def process_payment():
        payment_info = payment_entry.get().strip()
        amount = amount_entry.get().strip()
        method = method_var.get()

        if not payment_info or not amount:
            messagebox.showerror("Error", "Please enter all payment details.")
            return

        if not amount.isdigit():
            messagebox.showerror("Error", "Amount must be a number.")
            return

        messagebox.showinfo(
            "Payment Successful",
            f"Payment of ${amount} for {dog_name} via {method} completed.\nThank you!"
        )
        payment_win.destroy()

    Button(payment_win, text="Pay Now", bg="green", fg="white", command=process_payment).pack(pady=20)

import sqlite3
from tkinter import *
from tkinter import messagebox






# -------------------- Adoption Application Form --------------------
def open_adoption_form(user_id, dog_id, dog_name, breed):
    form_win = Toplevel()
    form_win.geometry("500x600")
    form_win.title("Adoption Application Form")

    Label(form_win, text=f"Adopt {dog_name} ({breed})", font=("Arial", 14, "bold")).pack(pady=10)

    Label(form_win, text=f"User ID: {user_id} | Dog ID: {dog_id}", font=("Arial", 10)).pack(pady=5)

    Label(form_win, text="Guardian Name").pack(anchor="w", padx=10)
    guardian_entry = Text(form_win, height=3, width=50)
    guardian_entry.pack(padx=20, pady=5)

    Label(form_win, text="Guardian Id").pack(anchor="w", padx=10)
    id_entry = Text(form_win, height=3, width=50)
    id_entry.pack(padx=20, pady=5)


    Label(form_win, text="Your Address").pack(anchor="w", padx=20)
    address_entry = Text(form_win, height=3, width=50)
    address_entry.pack(padx=20, pady=5)



    Label(form_win, text="Why do you want to adopt this dog?").pack(anchor="w", padx=20)
    reason_entry = Text(form_win, height=3, width=50)
    reason_entry.pack(padx=20, pady=5)

    Label(form_win, text="Do you have prior pet experience?").pack(anchor="w", padx=20)
    experience_entry = Text(form_win, height=3, width=50)
    experience_entry.pack(padx=20, pady=5)

    Label(form_win, text="Do you agree to provide proper care?").pack(anchor="w", padx=20)
    agree_var = StringVar()
    agree_var.set("Yes")
    Radiobutton(form_win, text="Yes", variable=agree_var, value="Yes").pack(anchor="w", padx=40)
    Radiobutton(form_win, text="No", variable=agree_var, value="No").pack(anchor="w", padx=40)

    def submit_application():
        guardian = guardian_entry.get("1.0", END).strip()
        id=id_entry.get("1.0",END).strip()

        address = address_entry.get("1.0", END).strip()
        reason = reason_entry.get("1.0", END).strip()
        experience = experience_entry.get("1.0", END).strip()
        agree = agree_var.get()

        if not guardian or not id or not  address or not reason or not experience:
            messagebox.showerror("Error", "Please answer all questions and provide your address.")
            return

        conn = sqlite3.connect("dog_adoption_app.db")
        c = conn.cursor()

        # Check for duplicate
        c.execute("SELECT * FROM adoptions WHERE user_id = ? AND dog_id = ?", (user_id, dog_id))
        if c.fetchone():
            messagebox.showinfo("Already Applied", "You have already applied for this dog.")
        else:
            c.execute("""
                INSERT INTO adoptions (user_id, dog_id, address, reason, experience, agree)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, dog_id, address, reason, experience, agree))
            conn.commit()
            messagebox.showinfo("Success", f"Your application for {dog_name} is submitted!")

        conn.close()
        form_win.destroy()

    Button(form_win, text="Submit Application", bg="green", fg="white", command=submit_application).pack(pady=20)


    

def open_submission_view(adoption_id, dog_name, breed, user_id):
    view_win = Toplevel()
    view_win.geometry("500x400")
    view_win.title("Your Application Submitted")

    # Get adoption record from DB
    conn = sqlite3.connect("dog_adoption_app.db")
    c = conn.cursor()
    c.execute("SELECT * FROM adoptions WHERE adoption_id = ?", (adoption_id,))
    record = c.fetchone()
    conn.close()

    if not record:
        messagebox.showerror("Error", "Could not find your adoption application.")
        view_win.destroy()
        return

    _, _, _, address, reason, experience, agree = record

    Label(view_win, text="Application Submitted Successfully!", font=("Arial", 16, "bold"), fg="green").pack(pady=10)

    Label(view_win, text=f"Dog: {dog_name} ({breed})").pack(anchor="w", padx=20)
    Label(view_win, text=f"User ID: {user_id}").pack(anchor="w", padx=20)
    Label(view_win, text=f"Address: {address}").pack(anchor="w", padx=20)
    Label(view_win, text=f"Reason: {reason}").pack(anchor="w", padx=20)
    Label(view_win, text=f"Experience: {experience}").pack(anchor="w", padx=20)
    Label(view_win, text=f"Agreed to Care: {agree}").pack(anchor="w", padx=20)

    
    Button(
        view_win,
        text="Proceed to Payment",
        bg="blue", fg="white",
        command=lambda: open_payment_window(user_id, dog_name)  # Make sure you have open_payment_window!
    ).pack(pady=20)



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

