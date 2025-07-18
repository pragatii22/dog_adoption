from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Heaven of Happy Hooves")
root.state("zoomed")

# Database setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    address TEXT,
    email TEXT,
    phone TEXT
)
""")
conn.commit()

# Background image full screen
bg_image = Image.open("images/golden.jpg")
bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

# Paw logo at top-left
try:
    paw_img = Image.open("images/paw.png").resize((80, 80))
    paw_photo = ImageTk.PhotoImage(paw_img)
    logo_label = Label(root, image=paw_photo)
    logo_label.image = paw_photo
    logo_label.place(x=20, y=20)
except:
    Label(root, text="[Paw Image Missing]", fg="white", font=("Arial", 16)).place(x=20, y=20)

# Title above background
title_label = Label(root, text="Heaven of Happy Hooves", font=("Helvetica", 36, "bold"), fg="white")
title_label.place(relx=0.5, y=30, anchor="n")

# Header Navigation Buttons
nav_frame = Frame(root)
nav_frame.place(relx=0.5, rely=0.15, anchor="n")

nav_buttons = [
    ("Homepage", lambda: messagebox.showinfo("Homepage", "Welcome to Heaven of Happy Hooves!")),
    ("About Us", lambda: messagebox.showinfo("About Us", "We rescue and rehome dogs with love.")),
    ("Available Dogs", lambda: messagebox.showinfo("Available Dogs", "Here are the dogs ready for adoption."))
]

for text, cmd in nav_buttons:
    Button(nav_frame, text=text, command=cmd, font=("Arial", 14), bg="#212121", fg="white",
           activebackground="#424242", activeforeground="white", padx=20, pady=5).pack(side=LEFT, padx=10)

# Description about dogs
desc_label = Label(root, text="🐶 Meet our adorable rescue dogs waiting for a loving home.\nEach one has a story, a heart, and a wagging tail ready to greet you!",
                   font=("Arial", 14), fg="white", justify=CENTER)
desc_label.place(relx=0.5, rely=0.22, anchor="n")

# Login/Register/Ratings buttons at top-right
btn_frame = Frame(root)
btn_frame.place(relx=0.99, y=20, anchor="ne")

def open_register():
    def register_user():
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.get()
        address = entry_address.get()
        phone_no = entry_phone_no.get()
        if not (username and password and address and email and phone_no):
            messagebox.showwarning("Input Error", "All fields are required")
            return
        try:
            cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", (username, password, address, email, phone_no))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
            reg_win.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

    reg_win = Toplevel(root)
    reg_win.title("Register")
    reg_win.geometry("300x300")
    reg_win.config(bg="#e1f5fe")

    Label(reg_win, text="Username", bg="#e1f5fe").pack(pady=(15, 2))
    entry_username = Entry(reg_win, width=35)
    entry_username.pack()

    Label(reg_win, text="Password", bg="#e1f5fe").pack(pady=(10, 2))
    entry_password = Entry(reg_win, width=35)
    entry_password.pack()

    Label(reg_win, text="Email", bg="#e1f5fe").pack(pady=(10, 2))
    entry_email = Entry(reg_win, width=35)
    entry_email.pack()

    Label(reg_win, text="Address", bg="#e1f5fe").pack(pady=(10, 2))
    entry_address = Entry(reg_win, width=35)
    entry_address.pack()

    Label(reg_win, text="Phone", bg="#e1f5fe").pack(pady=(10, 2))
    entry_phone_no = Entry(reg_win, width=35)
    entry_phone_no.pack()

    Button(reg_win, text="Register", bg="#0277bd", fg="white", command=register_user).pack(pady=20)

def open_change_password(username):
    change_password_win = Toplevel(root)
    change_password_win.title("Change Password")
    change_password_win.geometry("300x180")
    change_password_win.config(bg="#fff3e0")

    Label(change_password_win, text=f"Change Password for {username}", bg="#fff3e0").pack(pady=5)
    Label(change_password_win, text="Old Password", bg="#fff3e0").pack()
    entry_old_password = Entry(change_password_win, show="*")
    entry_old_password.pack()

    Label(change_password_win, text="New Password", bg="#fff3e0").pack()
    entry_new_password = Entry(change_password_win, show="*")
    entry_new_password.pack()

    def change_password():
        old_password = entry_old_password.get()
        new_password = entry_new_password.get()
        if not (old_password and new_password):
            messagebox.showwarning("Input Error", "All fields are required")
            return
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, old_password))
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
            conn.commit()
            messagebox.showinfo("Success", "Password changed successfully!")
            change_password_win.destroy()
        else:
            messagebox.showerror("Error", "Old password incorrect")

    Button(change_password_win, text="Change Password", command=change_password, bg="#ef6c00", fg="white").pack(pady=10)

def open_login():
    logged_in_user = {"username": None}
    login_win = Toplevel(root)
    login_win.title("Login")
    login_win.geometry("300x250")
    login_win.config(bg="#e8f5e9")

    Label(login_win, text="Username", bg="#e8f5e9").pack(pady=(15, 2))
    entry_user = Entry(login_win)
    entry_user.pack()

    Label(login_win, text="Password", bg="#e8f5e9").pack(pady=(10, 2))
    entry_pwd = Entry(login_win, show="*")
    entry_pwd.pack()

    show_password_var = BooleanVar()
    def toggle_password():
        entry_pwd.config(show="" if show_password_var.get() else "*")
    Checkbutton(login_win, text="Show Password", variable=show_password_var, command=toggle_password, bg="#e8f5e9").pack(pady=5)

    def login_user():
        user = entry_user.get()
        pwd = entry_pwd.get()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Login", f"Welcome, {user}!")
            logged_in_user["username"] = user
            btn_update_password.config(state="normal")
            login_win.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            logged_in_user["username"] = None
            btn_update_password.config(state="disabled")

    def open_update_password():
        user = logged_in_user["username"]
        if not user:
            messagebox.showwarning("Not Logged In", "Please login first.")
            return
        open_change_password(user)

    btn_update_password = Button(login_win, text="Update Password", state="disabled", bg="#43a047", fg="white", command=open_update_password)
    btn_update_password.pack(pady=(10, 5))

    Button(login_win, text="Login", command=login_user, bg="#1e88e5", fg="white").pack(pady=10)

# Buttons at top-right
Button(btn_frame, text="Login", font=("Arial", 14), bg="#1e88e5", fg="white", padx=20, pady=5, command=open_login).pack(side=LEFT, padx=10)
Button(btn_frame, text="Register", font=("Arial", 14), bg="#43a047", fg="white", padx=20, pady=5, command=open_register).pack(side=LEFT, padx=10)
Button(btn_frame, text="Ratings", font=("Arial", 14), bg="#fbc02d", fg="black", padx=20, pady=5,
       command=lambda: messagebox.showinfo("Ratings", "Rated 4.9/5 by our happy adopters!")).pack(side=LEFT, padx=10)

# Fixed Footer with Ratings
footer = Frame(root, bg="#f5f5f5", height=120)
footer.place(relx=0.5, rely=1.0, anchor="s", relwidth=1)

Label(footer, text="⭐ ⭐ ⭐ ⭐ ⭐", font=("Arial", 18), bg="#f5f5f5").pack()
Label(footer, text="Rated 4.9/5 by our happy adopters!", bg="#f5f5f5", font=("Arial", 12)).pack(pady=4)
Label(footer, text="Follow us: Facebook | Twitter | Instagram", bg="#f5f5f5", fg="blue", font=("Arial", 11)).pack(pady=4)
Label(footer, text="© 2025 Heaven of Happy Hooves. All rights reserved.", bg="#f5f5f5", font=("Arial", 10)).pack()

root.mainloop()