from tkinter import *
<<<<<<< Updated upstream
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Happy Hooves Adoption")
root.geometry("1000x750")
root.configure(bg="white")

# 🔧 Base directory for images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🐶 Dog Data 
dogs = [
    {
        "name": "Buddy", "breed": "Labrador Retriever", "age": "2 years",
        "gender": "Male", "color": "Golden", "weight": "10 kg",
        "img": os.path.join(BASE_DIR, "dog1.png"),
        "description": "Buddy is a playful and loving Labrador. Great with kids and very loyal. Friendly, intelligent, and loyal. Great with families and kids. Loves swimming and outdoor play. Needs regular exercise. Easy to train and very social."
    },
    {
        "name": "Lucy", "breed": "Beagle", "age": "1.5 years",
        "gender": "Female", "color": "Brown & White", "weight": "12 kg",
        "img": os.path.join(BASE_DIR, "dog2.png"),
        "description": "Lucy is energetic and loves to sniff around. She’s friendly and curious! Small, curious, and energetic. Known for strong sense of smell. Friendly with children and other pets. Needs walks and playtime to stay happy. A bit stubborn in training."
    },
    {
        "name": "Charlie", "breed": "Pomeranian", "age": "3 years",
        "gender": "Male", "color": "White", "weight": "6 kg",
        "img": os.path.join(BASE_DIR, "dog3.png"),
        "description": "Charlie is a fluffy ball of joy. Perfect for cuddles and short walks! Tiny, fluffy, and alert. Big personality in a small body. Very loyal and active indoors. Needs brushing due to thick fur. Can be vocal and protective."
    },
    {
        "name": "Daisy", "breed": "Golden Retriever", "age": "2.5 years",
        "gender": "Female", "color": "White", "weight": "13 kg",
        "img": os.path.join(BASE_DIR, "dog4.png"),
        "description": "Daisy is calm and gentle. She’s great with families and loves affection. Gentle, loyal, and super friendly. Excellent with kids and families. Intelligent and easy to train. Needs regular walks and loves playing fetch. Sheds a lot."
    },
    {
        "name": "Max", "breed": "German Shepherd", "age": "4 years",
        "gender": "Male", "color": "Black", "weight": "15 kg",
        "img": os.path.join(BASE_DIR, "dog5.png"),
        "description": "Max is protective and intelligent. He’s a brave friend and very obedient. Smart, brave, and hardworking. Often used in police and guard work. Protective of family. Needs training and lots of exercise. Very loyal and alert."
    },
]

dog_photos = []

def open_dog_profile(dog):
    profile = Toplevel(root)
    profile.title(f"{dog['name']}'s Profile")
    profile.state('zoomed')
    profile.configure(bg="#f5e6cc")  # Light brown

    Label(profile, text=f"{dog['name']}'s Profile", font=("Arial", 28, "bold"), bg="#f5e6cc").pack(pady=20)

    content = Frame(profile, bg="#f5e6cc")
    content.pack(pady=10, padx=40, fill=BOTH, expand=True)

    left = Frame(content, bg="#f5e6cc")
    left.pack(side=LEFT, padx=50)

    img = Image.open(dog["img"])
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    dog_photos.append(photo)

    Label(left, image=photo, bg="#f5e6cc").pack()

    right = Frame(content, bg="#f5e6cc")
    right.pack(side=LEFT, padx=50, anchor="n")

    Label(right, text=f"Name: {dog['name']}", font=("Arial", 18, "bold"), bg="#f5e6cc").pack(anchor="w", pady=5)
    Label(right, text=f"Breed: {dog['breed']}", font=("Arial", 16), bg="#f5e6cc").pack(anchor="w", pady=2)
    Label(right, text=f"Age: {dog['age']}", font=("Arial", 16), bg="#f5e6cc").pack(anchor="w", pady=2)
    Label(right, text=f"Gender: {dog['gender']}", font=("Arial", 16), bg="#f5e6cc").pack(anchor="w", pady=2)
    Label(right, text=f"Color: {dog['color']}", font=("Arial", 16), bg="#f5e6cc").pack(anchor="w", pady=2)
    Label(right, text=f"Weight: {dog['weight']}", font=("Arial", 16), bg="#f5e6cc").pack(anchor="w", pady=2)

    Label(right, text="\nAbout:", font=("Arial", 16, "bold"), bg="#f5e6cc").pack(anchor="w", pady=(10, 0))
    Label(right, text=dog["description"], font=("Arial", 14), wraplength=500, justify=LEFT, bg="#f5e6cc").pack(anchor="w", pady=5)

    Button(profile, text="Adopt Me 🐾", font=("Arial", 14, "bold"),
           bg="#4CAF50", fg="white", padx=20, pady=10).pack(pady=30)

def show_dog_gallery():
    gallery = Toplevel(root)
    gallery.title("Available Dogs")
    gallery.state('zoomed')
    gallery.configure(bg="#e6f7ff")  # Light blue

    Label(gallery, text="🐶 Available Dogs for Adoption 🐾", font=("Arial", 26, "bold"), bg="#e6f7ff").pack(pady=30)

    main_frame = Frame(gallery, bg="#e6f7ff")
    main_frame.pack(pady=10)

    row = None
    for i, dog in enumerate(dogs):
        if i % 3 == 0:
            row = Frame(main_frame, bg="#e6f7ff")
            row.pack(pady=30)

        card = Frame(row, bg="white", bd=1, relief=SOLID, padx=10, pady=10)
        card.pack(side=LEFT, padx=40)

        img = Image.open(dog["img"])
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        dog_photos.append(photo)

        btn = Button(card, image=photo, bd=0, bg="white", command=lambda d=dog: open_dog_profile(d))
        btn.pack()
        Label(card, text=dog["name"], font=("Arial", 14, "bold"), bg="white").pack(pady=5)

# Home Button
Button(root, text="Available Dogs", font=("Arial", 16, "bold"),
       bg="black", fg="white", padx=40, pady=15, command=show_dog_gallery).pack()

root.mainloop()
=======
from tkinter import messagebox
import sqlite3
from datetime import datetime

root = Tk()
root.title("Dog Adoption Application Form")
root.geometry("700x750")  # Increased size to fit all content
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

Label(dog_frame, text="Preferred Dog Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(dog_frame, textvariable=dog_name_var, width=35, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(dog_frame, text="Preferred Breed", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
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

# Emergency Contact Section
emergency_frame = LabelFrame(main_container, text="5. Emergency Contact", 
                            font=("Arial", 12, "bold"), bg="white", fg="#1C1E1F", 
                            relief="solid", bd=1, padx=10, pady=10)
emergency_frame.pack(fill="x", padx=0, pady=5)

Label(emergency_frame, text="Emergency Contact Name", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(emergency_frame, textvariable=emergency_name_var, width=30, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=1, padx=10, pady=5)

Label(emergency_frame, text="Emergency Contact Phone", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
Entry(emergency_frame, textvariable=emergency_phone_var, width=30, font=("Arial", 10), relief="solid", bd=1).grid(row=0, column=3, padx=10, pady=5)

# Agreement Section
agreement_frame = LabelFrame(main_container, text="6. Terms and Conditions", 
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

>>>>>>> Stashed changes
