from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from admin import admin_interface
from available_dog import available_dog

# Main window setup
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
cursor.execute("""
CREATE TABLE IF NOT EXISTS doginformation (    
    dogname TEXT,
    dogid TEXT,
    dogage TEXT              
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin_interface (    
    username1 TEXT,
    password1 TEXT                
)
""")
cursor.execute("SELECT * FROM admin_interface WHERE username1 = ?", ("pragati",))
if not cursor.fetchone():
    cursor.execute("INSERT INTO admin_interface (username1, password1) VALUES (?, ?)", ("pragati", "1234"))
conn.commit()

# Background image
bg_image = Image.open("images/golden.jpg")
bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

# Navigation bar
nav_bar = Frame(root, bg="#ffffff", height=50)
nav_bar.pack(fill=X)
nav_items = ["Available Dogs", "About Us"]

Button(nav_bar, text="Available dogs", font=("Helvetica", 10, "bold"), bg="#F4F4F4", bd=0,command=available_dog).pack(side=LEFT, padx=15)
Button(nav_bar, text="About Us", font=("Helvetica", 10, "bold"), bg="#ffffff", bd=0).pack(side=LEFT, padx=15)

# Logo
try:
    paw_img = Image.open("images/paw.png").resize((60, 60))
    paw_photo = ImageTk.PhotoImage(paw_img)
    logo_label = Label(root, image=paw_photo, bg="#ffffff")
    logo_label.image = paw_photo
    logo_label.place(x=10, y=22)
except:
    Label(root, text="[Paw Image Missing]", bg="#ffffff").place(x=10, y=5)

# Title
title_label = Label(root, text="Heaven of Happy Hooves", font=("Helvetica", 20, "bold"), bg="#ffffff")
title_label.place(relx=0.5, y=10, anchor="n")

# Login/Register buttons
btn_frame = Frame(root, bg="#ffffff")
btn_frame.place(relx=0.99, y=10, anchor="ne")
Button(btn_frame, text="Login", command=lambda: open_login(), font=("Arial", 11, "bold"),
       bg="#1e88e5", fg="white", width=10).pack(side=LEFT, padx=10)
Button(btn_frame, text="Register", command=lambda: open_register(), font=("Arial", 11, "bold"),
       bg="#43a047", fg="white", width=10).pack(side=LEFT, padx=10)

# description
desc_label = Label(root, text="🐶 Meet our adorable rescue dogs waiting for a loving home.\nEach one has a story, a heart, and a wagging tail ready to greet you!",
                   justify=CENTER, font=("Helvetica", 12), bg="#fdf6e3")
desc_label.place(relx=0.5, rely=0.75, anchor="center")

# Footer
footer = Frame(root, bg="#f5f5f5", height=120)
footer.place(relx=0.5, rely=1.0, anchor="s", relwidth=1)
Label(footer, text="⭐ ⭐ ⭐ ⭐ ⭐", bg="#f5f5f5", font=("Helvetica", 12)).pack()
Label(footer, text="Rated 4.9/5 by our happy adopters!", bg="#f5f5f5", font=("Helvetica", 10)).pack(pady=4)
Label(footer, text="Follow us: Facebook | Twitter | Instagram", bg="#f5f5f5", fg="blue", font=("Helvetica", 10)).pack(pady=4)
Label(footer, text="© 2025 Heaven of Happy Hooves. All rights reserved.", bg="#f5f5f5", font=("Helvetica", 9)).pack()

# Register window
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
    reg_win.geometry("800x600") 
    reg_win.resizable(0,0) 

    bg_img = Image.open("images/brown.jpeg")
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(reg_win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(relwidth=1, relheight=1)

    form_frame = Frame(reg_win, bg="#ffffff", padx=20, pady=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(form_frame, text="Username", font=("Arial", 10, "bold")).pack(pady=5)
    entry_username = Entry(form_frame, width=35, font=("Arial", 10))
    entry_username.pack()

    Label(form_frame, text="Password", font=("Arial", 10, "bold")).pack(pady=5)
    entry_password = Entry(form_frame, width=35, font=("Arial", 10), show="*")
    entry_password.pack()

    Label(form_frame, text="Email", font=("Arial", 10, "bold")).pack(pady=5)
    entry_email = Entry(form_frame, width=35, font=("Arial", 10))
    entry_email.pack()

    Label(form_frame, text="Address", font=("Arial", 10, "bold")).pack(pady=5)
    entry_address = Entry(form_frame, width=35, font=("Arial", 10))
    entry_address.pack()

    Label(form_frame, text="Phone", font=("Arial", 10, "bold")).pack(pady=5)
    entry_phone_no = Entry(form_frame, width=35, font=("Arial", 10))
    entry_phone_no.pack()

    Button(form_frame, text="Register", command=register_user, bg="#43a047", fg="white",
           font=("Arial", 11, "bold")).pack(pady=10, ipadx=10, ipady=5)

# password changing window
def open_change_password(username):
    change_password_win = Toplevel(root)
    change_password_win.title("Change Password")
    change_password_win.geometry("300x180")
    change_password_win.config(bg="#fff3e0")

    Label(change_password_win, text=f"Change Password for {username}", bg="#fff3e0", font=("Arial", 11, "bold")).pack(pady=5)
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

    Button(change_password_win, text="Change Password", bg="#ef6c00", fg="white",
           font=("Arial", 11, "bold"), command=change_password).pack(pady=10)

def open_login(): # Login window
    logged_in_user = {"username": None}

    login_win = Toplevel(root)
    login_win.title("Login")
    login_win.geometry("800x600")
    login_win.resizable(0,0) 

    bg_img = Image.open("images/brown.jpeg")
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(login_win, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(relwidth=1, relheight=1)

    form_frame = Frame(login_win, bg="#ffffff", padx=20, pady=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(form_frame, text="Username", font=("Arial", 10, "bold")).pack(pady=5)
    entry_user = Entry(form_frame, width=35, font=("Arial", 10))
    entry_user.pack()
    Label(form_frame, text="Password", font=("Arial", 10, "bold")).pack(pady=5)
    entry_pwd = Entry(form_frame, width=35, font=("Arial", 10), show="*")
    entry_pwd.pack()

    show_password_var = BooleanVar()

    def toggle_password():
        entry_pwd.config(show="" if show_password_var.get() else "*")

    Checkbutton(form_frame, text="Show Password", variable=show_password_var,
                command=toggle_password, bg="#ffffff").pack(pady=5)
    
    def login_user():
        user = entry_user.get()
        pwd = entry_pwd.get()

        if not user or not pwd:
            messagebox.showerror("Login Failed", "Enter both phone number and password")
            return 
    
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Check if admin
        cursor.execute("SELECT * FROM admin_interface WHERE username1 = ? AND password1 = ?", (user, pwd)) 
        admin_result = cursor.fetchone()

        # Check if user
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pwd)) 
        user_result = cursor.fetchone()

        conn.close()

        if admin_result:
            admin_interface()
        elif user_result:
            messagebox.showinfo("Login Success", f"Welcome {user}!")
            btn_update_password.config(state="normal")  # Enable password update for users
            logged_in_user["username"] = user
            login_win.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


    def open_update_password():
        user = logged_in_user["username"]
        if not user:
            messagebox.showwarning("Not Logged In", "Please login first to update your password.")
            return
        open_change_password(user)

    btn_update_password = Button(form_frame, text="Update Password", bg="#43a047", fg="white",
                                 font=("Arial", 11, "bold"), command=open_update_password, state="disabled")
    btn_update_password.pack(pady=(10, 5), ipadx=10, ipady=5)

    Button(form_frame, text="Login", bg="#1e88e5", fg="white",
           font=("Arial", 11, "bold"), command=login_user).pack(pady=10, ipadx=10, ipady=5)

# Starts the main loop
root.mainloop()