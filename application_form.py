from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

root = Tk()
root.title("📝 Dog Adoption Application Form")
root.geometry("870x700")
root.configure(bg="#E8F4FD")  # Light blue background instead of skyblue

# Variables
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar() 
city_var = StringVar()
state_var = StringVar()
dog_name_var = StringVar()
dog_breed_var = StringVar()
agreed_var = BooleanVar()

# create database connection
conn = sqlite3.connect("dog_adoption.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT, city TEXT, state TEXT,
        dog_name TEXT, dog_breed TEXT, experience TEXT, reason TEXT,
        agreement TEXT, submission_date TEXT)"""
)
conn.commit()
conn.close()

# Remove scrollable area - use direct frame
main_container = Frame(root, bg="#E8F4FD")  # Match root background
main_container.pack(fill="both", expand=True, padx=0, pady=0)

# Header
header_frame = Frame(main_container, bg="#E8F4FD")  # Changed from white
header_frame.pack(fill="x", padx=0, pady=0)
Label(header_frame, text="🐾 Dog Adoption Application Form 🐾", font=("Arial", 15, "bold"),
        bg="#E8F4FD", fg="#272A2B").pack(pady=10)  # Changed bg

# Personal Information Section
personal_frame = LabelFrame(main_container, text="1. Personal Information", 
                           font=("Arial", 12, "bold"), bg="#E8F4FD", fg="#272A2B", 
                           relief="flat", bd=0, padx=8, pady=5)  # Changed bg
personal_frame.pack(fill="x", padx=0, pady=5)

Label(personal_frame, text="Full Name", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(personal_frame, text="Email Address", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=email_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

Label(personal_frame, text="Phone Number", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=phone_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=1, column=1, padx=10, pady=5)

# Address Information Section
address_frame = LabelFrame(main_container, text="2. Address Information", 
                          font=("Arial", 12, "bold"), bg="#E8F4FD", fg="#181A1A", 
                          relief="flat", bd=0, padx=15, pady=10)  # Changed bg
address_frame.pack(fill="x", padx=0, pady=5)

Label(address_frame, text="City", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(address_frame, textvariable=city_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(address_frame, text="State", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(address_frame, textvariable=state_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Dog Information Section
dog_frame = LabelFrame(main_container, text="3. Dog Information", 
                      font=("Arial", 12, "bold"), bg="#E8F4FD", fg="#101111", 
                      relief="flat", bd=0, padx=15, pady=10)  # Changed bg
dog_frame.pack(fill="x", padx=0, pady=5)

Label(dog_frame, text="Dog Name", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(dog_frame, text="Dog Breed", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_breed_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Experience and Motivation Section
experience_frame = LabelFrame(main_container, text="4. Experience & Motivation", 
                             font=("Arial", 12, "bold"), bg="#E8F4FD", fg="#101111", 
                             relief="flat", bd=0, padx=10, pady=5)  # Changed bg
experience_frame.pack(fill="x", padx=0, pady=5)

Label(experience_frame, text="Previous Pet Experience", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=0, sticky="nw", padx=10, pady=5)
experience_text = Text(experience_frame, width=30, height=3, font=("Arial", 10), relief="solid", bd=1)
experience_text.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

Label(experience_frame, text="Why do you want to adopt?", font=("Arial", 10, "bold"), bg="#E8F4FD").grid(row=0, column=2, sticky="nw", padx=10, pady=5)
reason_text = Text(experience_frame, width=30, height=3, font=("Arial", 10), relief="solid", bd=1)
reason_text.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

# Agreement Section
agreement_frame = LabelFrame(main_container, text="5. Terms and Conditions", 
                            font=("Arial", 12, "bold"), bg="#E8F4FD", fg="#0B0C0C", 
                            relief="flat", bd=0, padx=5, pady=3)  # Changed bg
agreement_frame.pack(fill="x", padx=0, pady=5)

agreement_inner_frame = Frame(agreement_frame, bg="#E8F4FD")  # Changed bg
agreement_inner_frame.pack(fill="x", padx=5, pady=5)  # Reduced padding

agreement_text = """ADOPTION AGREEMENT:
By checking the box below, I agree to:
• Provide proper care, food, water, shelter and veterinary care.
• Never abandon, abuse or neglect the dog. 
• You must be 18 over to able a adopt dog.
• Return the dog to the shelter if unable to provide care.
• Allow home visits for welfare checks if requested.
• Follow all local licensing and vaccination requirements.
• Provide a permanent, loving home for the dog's lifetime."""

agreement_display = Text(agreement_inner_frame, height=4, width=80, font=("Arial", 9),  # Reduced height from 6 to 4, width from 90 to 80, font from 10 to 9
                           wrap="word", bg="#F7EBEB", relief="solid", bd=1)  # Reduced border from 2 to 1
agreement_display.pack(fill="x", pady=3)  # Reduced padding from 5 to 3
agreement_display.insert("1.0", agreement_text)
agreement_display.config(state="disabled")

Checkbutton(agreement_frame, text=" I have read and agree to all terms and conditions above. ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა", 
           variable=agreed_var, bg="#E8F4FD", font=("Arial", 10, "bold"),  # Changed bg
           wraplength=500).pack(anchor="w", padx=5, pady=3)  # Reduced padding from 8,5 to 5,3

# Submit function
def submit():
    if not all([name_var.get(), email_var.get(), phone_var.get(), agreed_var.get()]):
        messagebox.showerror("Error", "Please fill required fields and agree to terms")
        return
    
    try:
        conn = sqlite3.connect("dog_adoption.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            email TEXT, 
            phone TEXT, 
            city TEXT, 
            state TEXT,
            dog_name TEXT, 
            dog_breed TEXT, 
            experience TEXT, 
            reason TEXT,
            agreement TEXT, 
            submission_date TEXT)""")
        conn.execute("""INSERT INTO applications VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)""",
                    (name_var.get(), 
                     email_var.get(), 
                     phone_var.get(), 
                     city_var.get(), 
                     state_var.get(), 
                     dog_name_var.get(), 
                     dog_breed_var.get(),
                     experience_text.get("1.0", END).strip(), 
                     reason_text.get("1.0", END).strip(),
                     "Agreed", 
                     datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Application submitted successfully!\n\nApplicant: {name_var.get()}")
        clear_form()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to submit application: {str(e)}")

def clear_form():
    for var in [name_var, email_var, phone_var, city_var, state_var, 
               dog_name_var, dog_breed_var]:
        var.set("")
    experience_text.delete("1.0", END)
    reason_text.delete("1.0", END)
    agreed_var.set(False)

# Simple payment window with database
def payments():
    payment_window = Toplevel(root)
    payment_window.title("Payment Details")
    payment_window.maxsize(0, 0)  # Reduced height since removing amount field
    payment_window.configure(bg="lightyellow")
    
    Label(payment_window, text="💳 Payment", font=("Arial", 15, "bold"), bg="lightyellow").pack(pady=15)

    # Name
    Label(payment_window, text="Full Name", font=("Arial", 12, "bold"), bg="lightyellow").pack(anchor="w", padx=20)
    name_entry = Entry(payment_window, width=30, font=("Arial", 11), relief="solid", bd=1)
    name_entry.pack(pady=5, padx=20)

    # Address
    Label(payment_window, text="Address", font=("Arial", 12, "bold"), bg="lightyellow").pack(anchor="w", padx=20)
    address_entry = Entry(payment_window, width=30, font=("Arial", 11), relief="solid", bd=1)
    address_entry.pack(pady=5, padx=20)

    # Phone
    Label(payment_window, text="Phone Number", font=("Arial", 12, "bold"), bg="lightyellow").pack(anchor="w", padx=20)
    phone_entry = Entry(payment_window, width=30, font=("Arial", 11), relief="solid", bd=1)
    phone_entry.pack(pady=5, padx=20)

    # Payment Method
    Label(payment_window, text="Payment Method", font=("Arial", 12, "bold"), bg="lightyellow").pack(anchor="w", padx=20)
    method_var = StringVar(value="🚚 cash on delivery💵")
    OptionMenu(payment_window, method_var, "🚚 cash on delivery 💵").pack(pady=5, padx=20)

    # Confirm Payment
    def confirm_payment():
        if not all([name_entry.get(), address_entry.get(), phone_entry.get()]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        # Create simple payment table and insert data (without amount)
        conn = sqlite3.connect("dog_adoption.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            address TEXT, 
            phone TEXT, 
            method TEXT, 
            date TEXT)""")
        conn.execute("INSERT INTO payments VALUES (NULL,?,?,?,?,?)",
                    (name_entry.get(), 
                     address_entry.get(), 
                     phone_entry.get(), 
                     method_var.get(), 
                     datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", f"Payment processed successfully!\nMethod: {method_var.get()}")
        payment_window.destroy()
    
    Button(payment_window, text="🦴Confirm Payment", bg="#358B1B", fg="white", 
           font=("Arial", 12, "bold"), command=confirm_payment).pack(pady=20)

# Submit Button Section
button_frame = Frame(main_container, bg="#E8F4FD")  # Changed bg
button_frame.pack(fill="x", padx=0, pady=20)

Button(button_frame, text="SUBMIT APPLICATION", bg="#367AE0", fg="white", 
       font=("Arial", 10, "bold"), command=submit, width=20, height=1,
       relief="solid", bd=1).pack(side="left", padx=10)
Button(button_frame, text="CLEAR FORM", bg="#151414", fg="white", 
       font=("Arial", 10, "bold"), command=lambda: clear_form(), width=20, height=1,
       relief="solid", bd=1).pack(side="left", padx=10)
Button(button_frame, text="PAYMENT", bg="#71B321", fg="white", 
       font=("Arial", 10, "bold"), command=payments, width=20, height=1,
       relief="solid", bd=1).pack(side="left", padx=10)
root.mainloop()

