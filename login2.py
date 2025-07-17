import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.geometry('500x500')
root.resizable(1, 1)

# database 
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

# for register window
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
            # Fixed order to match table schema (username, password, address, email, phone)
            cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", (username, password, address, email, phone_no))
            conn.commit()
            messagebox.showinfo("success", "Registration Successful!")
            reg_win.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

    reg_win = tk.Toplevel(root)
    reg_win.title("Register")
    reg_win.geometry("300x300")

    lbl_username = tk.Label(reg_win, text="username")
    lbl_username.pack()
    entry_username = tk.Entry(reg_win, width=35, font=("Arial", 11))
    entry_username.pack()

    lbl_password = tk.Label(reg_win, text="Password")
    lbl_password.pack()
    entry_password = tk.Entry(reg_win, width=35, font=("Arial", 11), show="*")  # added show="*"
    entry_password.pack()

    lbl_email = tk.Label(reg_win, text="Email")
    lbl_email.pack()
    entry_email = tk.Entry(reg_win, width=35, font=("Arial", 11))
    entry_email.pack()

    lbl_address = tk.Label(reg_win, text="Address")
    lbl_address.pack()
    entry_address = tk.Entry(reg_win, width=35, font=("Arial", 11))
    entry_address.pack()

    lbl_phone_no = tk.Label(reg_win, text="phone_no")
    lbl_phone_no.pack()
    entry_phone_no = tk.Entry(reg_win, width=35, font=("Arial", 11))
    entry_phone_no.pack()

    btn_register = tk.Button(reg_win, text="register", command=register_user)
    btn_register.pack(pady=10)


# password change window 
def open_change_password(username):
    change_password_win = tk.Toplevel(root)
    change_password_win.title("Change Password")
    change_password_win.geometry("300x180")

    tk.Label(change_password_win, text=f"Change Password for {username}").pack(pady=5)

    tk.Label(change_password_win, text="Old Password").pack()
    entry_old_password = tk.Entry(change_password_win, show="*")
    entry_old_password.pack()

    tk.Label(change_password_win, text="New Password").pack()
    entry_new_password = tk.Entry(change_password_win, show="*")
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

    tk.Button(change_password_win, text="Change Password", command=change_password).pack(pady=10)


# Login window with Update Password button enabled only after login
def open_login():
    logged_in_user = {"username": None}  # To store logged-in username in closure

    login_win = tk.Toplevel(root)
    login_win.title("Login")
    login_win.geometry("300x250")

    tk.Label(login_win, text="Username").pack()
    entry_user = tk.Entry(login_win)
    entry_user.pack()

    tk.Label(login_win, text="Password").pack()
    entry_pwd = tk.Entry(login_win, show="*")
    entry_pwd.pack()

    show_password_var = tk.BooleanVar()

    def toggle_password():
        if show_password_var.get():
            entry_pwd.config(show="")
        else:
            entry_pwd.config(show="*")

    show_password_check = tk.Checkbutton(login_win, text="Show Password", variable=show_password_var, command=toggle_password)
    show_password_check.pack()

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
            # Do NOT destroy root here; otherwise app closes
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.\nIf new user, please register first.")
            logged_in_user["username"] = None
            btn_update_password.config(state="disabled")

    def open_update_password():
        user = logged_in_user["username"]
        if not user:
            messagebox.showwarning("Not Logged In", "Please login first to update your password.")
            return
        open_change_password(user)

    btn_update_password = tk.Button(login_win, text="Update Password", command=open_update_password, state="disabled")
    btn_update_password.pack()

    tk.Button(login_win, text="Login", command=login_user).pack(pady=10)


# Main window with side-by-side Login and Register buttons at top center

root.title("Login / Register")

root.geometry("350x150")

frame = tk.Frame(root)
frame.pack(side="top", pady=20)

btn_login = tk.Button(frame, text="Login", width=12, command=open_login)
btn_login.pack(side="left", padx=10)

btn_register = tk.Button(frame, text="Register", width=12, command=open_register)
btn_register.pack(side="left", padx=10)

root.mainloop()
