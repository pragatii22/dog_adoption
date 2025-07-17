from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime


root = Tk()
root.title("Dog Adoption Application Form")
root.geometry("330x700")  
root.configure(bg="skyblue") 
root.resizable(True, True)  
root.state('zoomed') 

# Variables
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar() 
city_var = StringVar()
state_var = StringVar()
dog_name_var = StringVar()
dog_breed_var = StringVar()
emergency_name_var = StringVar()
emergency_phone_var = StringVar()  # Changed from int() to StringVar()
agreed_var = BooleanVar()


header_frame = Frame(root, bg="white", relief="solid", bd=1)
header_frame.pack(fill="x", padx=20, pady=(20, 10))

Label(header_frame, text="🐕 APPLICATION FORM 🐕", 
      font=("Arial", 18, "bold"), fg="#1E2123", bg="white").pack(pady=15)

# Create scrollable main frame
canvas = Canvas(root, bg="skyblue")
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="white")

# Function to update scroll region
def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

scrollable_frame.bind("<Configure>", configure_scroll_region)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


canvas.bind("<MouseWheel>", on_mousewheel)


canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


canvas.focus_set()


def bind_mousewheel(widget):
    widget.bind("<MouseWheel>", on_mousewheel)
    for child in widget.winfo_children():
        bind_mousewheel(child)


root.after(100, lambda: bind_mousewheel(root))


main_frame = Frame(scrollable_frame, bg="skyblue", relief="solid", bd=1)
main_frame.pack(padx=20, pady=10, fill="both", expand=True)


personal_frame = LabelFrame(main_frame, text="1. Personal Information", 
                           font=("Arial", 12, "bold"), bg="white", fg="#272A2B", 
                           relief="solid", bd=1, padx=15, pady=10)
personal_frame.pack(fill="x", padx=15, pady=10)

Label(personal_frame, text="Full Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(personal_frame, text="Email Address", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=email_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

Label(personal_frame, text="Phone Number", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Entry(personal_frame, textvariable=phone_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=1, column=1, padx=10, pady=5)

# Address Information Section
address_frame = LabelFrame(main_frame, text="2. Address Information", 
                          font=("Arial", 12, "bold"), bg="white", fg="#181A1A", 
                          relief="solid", bd=1, padx=15, pady=10)
address_frame.pack(fill="x", padx=15, pady=10)

Label(address_frame, text="City", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(address_frame, textvariable=city_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(address_frame, text="State", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(address_frame, textvariable=state_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Dog Information Section
dog_frame = LabelFrame(main_frame, text="3. Dog Information", 
                      font=("Arial", 12, "bold"), bg="white", fg="#101111", 
                      relief="solid", bd=1, padx=15, pady=10)
dog_frame.pack(fill="x", padx=15, pady=10)

Label(dog_frame, text="Preferred Dog Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(dog_frame, text="Preferred Breed", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_breed_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Experience and Motivation Section
experience_frame = LabelFrame(main_frame, text="4. Experience & Motivation", 
                             font=("Arial", 12, "bold"), bg="white", fg="#101111", 
                             relief="solid", bd=1, padx=15, pady=10)
experience_frame.pack(fill="x", padx=15, pady=10)

Label(experience_frame, text="Previous Pet Experience", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="nw", padx=10, pady=5)
experience_text = Text(experience_frame, width=45, height=4, font=("Arial", 10), relief="solid", bd=1)
experience_text.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

Label(experience_frame, text="Why do you want to adopt?", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="nw", padx=10, pady=5)
reason_text = Text(experience_frame, width=45, height=4, font=("Arial", 10), relief="solid", bd=1)
reason_text.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

# Emergency Contact Section
emergency_frame = LabelFrame(main_frame, text="5. Emergency Contact", 
                            font=("Arial", 12, "bold"), bg="white", fg="#1C1E1F", 
                            relief="solid", bd=1, padx=15, pady=10)
emergency_frame.pack(fill="x", padx=15, pady=10)

Label(emergency_frame, text="Emergency Contact Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(emergency_frame, textvariable=emergency_name_var, width=30, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(emergency_frame, text="Emergency Contact Phone", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(emergency_frame, textvariable=emergency_phone_var, width=30, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Agreement Section
agreement_frame = LabelFrame(main_frame, text="6. Terms and Conditions", 
                            font=("Arial", 12, "bold"), bg="white", fg="#0B0C0C", 
                            relief="solid", bd=1, padx=15, pady=10)
agreement_frame.pack(fill="x", padx=15, pady=10)

# Create a frame for the agreement text
agreement_inner_frame = Frame(agreement_frame, bg="white")
agreement_inner_frame.pack(fill="x", padx=10, pady=10)
agreement_text = """ADOPTION AGREEMENT:

By checking the box below, I agree to:
• Provide proper care, food, water, shelter and veterinary care.
• Never abandon, abuse or neglect the dog. 
• You must be 18 over to able adopt dog.
• Return the dog to the shelter if unable to provide care.
• Allow home visits for welfare checks if requested.
• Follow all local licensing and vaccination requirements.
• Provide a permanent, loving home for the dog's lifetime."""

# Create scrollable text widget for agreement
agreement_display = Text(agreement_inner_frame, height=8, width=90, font=("Arial", 10), 
                           wrap="word", bg="#F7EBEB", relief="solid", bd=2)
agreement_display.pack(fill="x", pady=5)
agreement_display.insert("1.0", agreement_text)
agreement_display.config(state="disabled")  # Make it read-only

# Agreement checkbox
Checkbutton(agreement_frame, text="I have read and agree to all terms and conditions above.", 
           variable=agreed_var, bg="white", font=("Arial", 11, "bold"), 
           wraplength=600).pack(anchor="w", padx=10, pady=15)

# Submit function
def submit():
    if not all([name_var.get(), email_var.get(), phone_var.get(), agreed_var.get()]):
        messagebox.showerror("Error", "Please fill required fields and agree to terms")
        return
    
    try:
        conn = sqlite3.connect("dog_adoption.db")
        conn.execute("""INSERT INTO applications VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (name_var.get(), email_var.get(), phone_var.get(), city_var.get(), 
                     state_var.get(), dog_name_var.get(), dog_breed_var.get(),
                     experience_text.get("1.0", END).strip(), reason_text.get("1.0", END).strip(),
                     emergency_name_var.get(), emergency_phone_var.get(), 
                     "Agreed", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Application submitted successfully!\n\nApplication for: {dog_name_var.get()}\nApplicant: {name_var.get()}")
        
        # Clear form after submission
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

# Submit Button Section
button_frame = Frame(main_frame, bg="white")
button_frame.pack(fill="x", padx=15, pady=20)

Button(button_frame, text="SUBMIT APPLICATION", bg="#367AE0", fg="white", 
       font=("Arial", 12, "bold"), command=submit, width=25, height=2,
       relief="solid", bd=1).pack(side="left", padx=10)
Button(button_frame, text="CLEAR FORM", bg="#151414", fg="white", 
       font=("Arial", 12), command=lambda: clear_form(), width=20, height=2,
       relief="solid", bd=1).pack(side="left", padx=10)

root.mainloop()

