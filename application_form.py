from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

root = Tk()
root.title("Dog Adoption Application Form")
root.geometry("700x700")  # Increased size to fit all content
root.configure(bg="skyblue")

# Variables
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar() 
city_var = StringVar()
state_var = StringVar()
dog_name_var = StringVar()
dog_breed_var = StringVar()
emergency_name_var = StringVar()
emergency_phone_var = StringVar()
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
main_container = Frame(root, bg="skyblue")
main_container.pack(fill="both", expand=True, padx=0, pady=0)

# Header
header_frame = Frame(main_container, bg="white", relief="solid", bd=1)  
header_frame.pack(fill="x", padx=0, pady=0)
Label(header_frame, text="🐾 Dog Adoption Application Form 🐾", font=("Arial", 15, "bold"),
        bg="white", fg="#272A2B").pack(pady=10)

# Personal Information Section
personal_frame = LabelFrame(main_container, text="1. Personal Information", 
                           font=("Arial", 12, "bold"), bg="white", fg="#272A2B", 
                           relief="solid", bd=1, padx=8, pady=5)
personal_frame.pack(fill="x", padx=0, pady=5)

Label(personal_frame, text="Full Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(personal_frame, text="Email Address", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=email_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

Label(personal_frame, text="Phone Number", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=phone_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=1, column=1, padx=10, pady=5)

# Address Information Section
address_frame = LabelFrame(main_container, text="2. Address Information", 
                          font=("Arial", 12, "bold"), bg="white", fg="#181A1A", 
                          relief="solid", bd=1, padx=15, pady=10)
address_frame.pack(fill="x", padx=0, pady=5)

Label(address_frame, text="City", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(address_frame, textvariable=city_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(address_frame, text="State", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(address_frame, textvariable=state_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Dog Information Section
dog_frame = LabelFrame(main_container, text="3. Dog Information", 
                      font=("Arial", 12, "bold"), bg="white", fg="#101111", 
                      relief="solid", bd=1, padx=15, pady=10)
dog_frame.pack(fill="x", padx=0, pady=5)

Label(dog_frame, text="Dog Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(dog_frame, text="Dog Breed", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_breed_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Experience and Motivation Section
experience_frame = LabelFrame(main_container, text="4. Experience & Motivation", 
                             font=("Arial", 12, "bold"), bg="white", fg="#101111", 
                             relief="solid", bd=1, padx=10, pady=5)
experience_frame.pack(fill="x", padx=0, pady=5)

Label(experience_frame, text="Previous Pet Experience", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="nw", padx=10, pady=5)
experience_text = Text(experience_frame, width=30, height=3, font=("Arial", 10), relief="solid", bd=1)
experience_text.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

Label(experience_frame, text="Why do you want to adopt?", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="nw", padx=10, pady=5)
reason_text = Text(experience_frame, width=30, height=3, font=("Arial", 10), relief="solid", bd=1)
reason_text.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

# remove the  emergency contact section
# Agreement Section
agreement_frame = LabelFrame(main_container, text="5. Terms and Conditions", 
                            font=("Arial", 12, "bold"), bg="white", fg="#0B0C0C", 
                            relief="solid", bd=1, padx=5, pady=3)  # Reduced padding
agreement_frame.pack(fill="x", padx=0, pady=5)

agreement_inner_frame = Frame(agreement_frame, bg="white")
agreement_inner_frame.pack(fill="x", padx=5, pady=5)  # Reduced padding

agreement_text = """ADOPTION AGREEMENT:
By checking the box below, I agree to:
• Provide proper care, food, water, shelter and veterinary care.
• Never abandon, abuse or neglect the dog. 
• You must be 18 over to able adopt dog.
• Return the dog to the shelter if unable to provide care.
• Allow home visits for welfare checks if requested.
• Follow all local licensing and vaccination requirements.
• Provide a permanent, loving home for the dog's lifetime."""

agreement_display = Text(agreement_inner_frame, height=4, width=80, font=("Arial", 9),  # Reduced height from 6 to 4, width from 90 to 80, font from 10 to 9
                           wrap="word", bg="#F7EBEB", relief="solid", bd=1)  # Reduced border from 2 to 1
agreement_display.pack(fill="x", pady=3)  # Reduced padding from 5 to 3
agreement_display.insert("1.0", agreement_text)
agreement_display.config(state="disabled")

Checkbutton(agreement_frame, text="I have read and agree to all terms and conditions above.", 
           variable=agreed_var, bg="white", font=("Arial", 10, "bold"),  # Reduced font from 11 to 10
           wraplength=500).pack(anchor="w", padx=5, pady=3)  # Reduced padding from 8,5 to 5,3

# Submit function
def submit():
    if not all([name_var.get(), email_var.get(), phone_var.get(), agreed_var.get()]):
        messagebox.showerror("Error", "Please fill required fields and agree to terms")
        return
    
    try:
        conn = sqlite3.connect("dog_adoption.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT, city TEXT, state TEXT,
            dog_name TEXT, dog_breed TEXT, experience TEXT, reason TEXT,
            emergency_name TEXT, emergency_phone TEXT, agreement TEXT, submission_date TEXT)""")
        conn.execute("""INSERT INTO applications VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (name_var.get(), email_var.get(), phone_var.get(), city_var.get(), 
                     state_var.get(), dog_name_var.get(), dog_breed_var.get(),
                     experience_text.get("1.0", END).strip(), reason_text.get("1.0", END).strip(),
                     emergency_name_var.get(), emergency_phone_var.get(), 
                     "Agreed", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Application submitted successfully!\n\nApplicant: {name_var.get()}")
        clear_form()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to submit application: {str(e)}")

def clear_form():
    for var in [name_var, email_var, phone_var, city_var, state_var, 
               dog_name_var, dog_breed_var, emergency_name_var, emergency_phone_var]:
        var.set("")
    experience_text.delete("1.0", END)
    reason_text.delete("1.0", END)
    agreed_var.set(False)

# payment window
def payments():
    payment_window = Toplevel(root)
    payment_window.title("Payment Details")
    payment_window.geometry("400x300")
    payment_window.configure(bg="skyblue")
    Label(payment_window, text="Payment Details", font=("Arial", 15, "bold"), bg="skyblue").pack(pady=10)

    # name
    Label(payment_window, text="Full Name", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=60)
    name_entry = Entry(payment_window, width=50, font=("Arial", 12), relief="solid", bd=1)
    name_entry.pack(pady=10, padx=60)

    


# Submit Button Section
button_frame = Frame(main_container, bg="skyblue")
button_frame.pack(fill="x", padx=0, pady=20)

Button(button_frame, text="SUBMIT APPLICATION", bg="#367AE0", fg="white", 
       font=("Arial", 10, "bold"), command=submit, width=20, height=1,
       relief="solid", bd=1).pack(side="left", padx=10)
Button(button_frame, text="CLEAR FORM", bg="#151414", fg="white", 
       font=("Arial", 10), command=lambda: clear_form(), width=20, height=1,
       relief="solid", bd=1).pack(side="left", padx=10)

root.mainloop()

