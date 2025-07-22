from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os
from application_form import application_form1


def available_dog():
    gallery = Toplevel()
    gallery.title("Available Dogs")
    gallery.state('zoomed')
    gallery.configure(bg="#e6f7ff")

    Label(gallery, text="🐶 Available Dogs for Adoption 🐾", font=("Arial", 26, "bold"), bg="#e6f7ff").pack(pady=30)

    main_frame = Frame(gallery, bg="#e6f7ff")
    main_frame.pack(pady=10)


    # 🔧 Base directory for images
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # 🐶 Dog Data 
    dogs = [
        {
            "name": "Buddy", "breed": "Labrador Retriever", "age": "2 years",
            "gender": "Male", "color": "Golden", "weight": "10 kg",
            "img": os.path.join(BASE_DIR, "images", "dog1.png"),
            "description": "Buddy is a playful and loving Labrador. Great with kids and very loyal. Friendly, intelligent, and loyal. Great with families and kids. Loves swimming and outdoor play. Needs regular exercise. Easy to train and very social."
        },
        {
            "name": "Lucy", "breed": "Beagle", "age": "1.5 years",
            "gender": "Female", "color": "Brown & White", "weight": "12 kg",
            "img": os.path.join(BASE_DIR, "images", "dog2.png"),
            "description": "Lucy is energetic and loves to sniff around. She’s friendly and curious! Small, curious, and energetic. Known for strong sense of smell. Friendly with children and other pets. Needs walks and playtime to stay happy. A bit stubborn in training."
        },
        {
            "name": "Charlie", "breed": "Pomeranian", "age": "3 years",
            "gender": "Male", "color": "White", "weight": "6 kg",
            "img": os.path.join(BASE_DIR, "images", "dog3.png"),
            "description": "Charlie is a fluffy ball of joy. Perfect for cuddles and short walks! Tiny, fluffy, and alert. Big personality in a small body. Very loyal and active indoors. Needs brushing due to thick fur. Can be vocal and protective."
        },
        {
            "name": "Daisy", "breed": "Golden Retriever", "age": "2.5 years",
            "gender": "Female", "color": "White", "weight": "13 kg",
            "img": os.path.join(BASE_DIR, "images", "dog4.png"),
            "description": "Daisy is calm and gentle. She’s great with families and loves affection. Gentle, loyal, and super friendly. Excellent with kids and families. Intelligent and easy to train. Needs regular walks and loves playing fetch. Sheds a lot."
        },
        {
            "name": "Max", "breed": "German Shepherd", "age": "4 years",
            "gender": "Male", "color": "Black", "weight": "15 kg",
            "img": os.path.join(BASE_DIR, "images", "dog5.png"),
            "description": "Max is protective and intelligent. He’s a brave friend and very obedient. Smart, brave, and hardworking. Often used in police and guard work. Protective of family. Needs training and lots of exercise. Very loyal and alert."
        },
    ]

    dog_photos = []  # Prevent garbage collection of images

    def open_dog_profile(dog):

        profile = Toplevel()
        profile.title(f"{dog['name']}'s Profile")
        profile.state('zoomed')
        profile.configure(bg="#f5e6cc")

        Label(profile, text=f"{dog['name']}'s Profile", font=("Arial", 28, "bold"), bg="#f5e6cc").pack(pady=20)

        content = Frame(profile, bg="#f5e6cc")
        content.pack(pady=10, padx=40, fill=BOTH, expand=True)

        left = Frame(content, bg="#f5e6cc")
        left.pack(side=LEFT, padx=50)

        img = Image.open(dog["img"])
        img = img.resize((400, 400))
        photo = ImageTk.PhotoImage(img)
        dog_photos.append(photo)  # Prevent image garbage collection

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

        Button(profile, text="Adopt Me 🐾", font=("Arial", 14, "bold"),command=application_form1,
        bg="#4CAF50", fg="white", padx=20, pady=10).pack(pady=30)

    def see_dog():
        see=Toplevel()
        see.title("check")
        see.configure(bg="green")
        see.geometry("400x200")
        Label(see, text="Enter Phone Number :", font=("Arial", 15, "bold"),bg="green").pack(pady=20)
        entry_ph = Entry(see, width=20, font=("Arial", 10))
        entry_ph.pack(pady=5)

        def btn_confirm():

            entry_ph1 = entry_ph.get()
            if not entry_ph1:
                messagebox.showwarning("Warning", "Phone number is required")
                return
                
            conn = sqlite3.connect("users.db")
            cursor= conn.cursor()
            cursor.execute("SELECT * FROM users WHERE phone = ?", (entry_ph1,))
            result2=cursor.fetchone()
            conn.commit()
            conn.close()

            if result2!=None:
                open_dog_profile(dog)
            else:
                messagebox.showinfo("please", "Login First")
                return

            
        btn1=Button(see, text="Confirm", font=("Arial", 16), fg="blue",command= btn_confirm)
        btn1.pack(pady=14)

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

        btn = Button(card, image=photo, bd=0, bg="white", command=see_dog)
        btn.pack()
        Label(card, text=dog["name"], font=("Arial", 14, "bold"), bg="white").pack(pady=5)

    gallery.mainloop()