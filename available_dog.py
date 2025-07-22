from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Happy Hooves Adoption")
root.geometry("1000x750")
root.configure(bg="white")

# 🐶 Dog Data (with description)
dogs = [
    {
        "name": "Buddy", "breed": "Labrador Retriever", "age": "2 years",
        "gender": "Male", "color": "Golden", "weight": "10 kg", "img": "dog1.png",
        "description": "Buddy is a playful and loving Labrador. Great with kids and very loyal."
    },
    {
        "name": "Lucy", "breed": "Beagle", "age": "1.5 years",
        "gender": "Female", "color": "Brown & White", "weight": "12 kg", "img": "dog2.png",
        "description": "Lucy is energetic and loves to sniff around. She’s friendly and curious!"
    },
    {
        "name": "Charlie", "breed": "Pomeranian", "age": "3 years",
        "gender": "Male", "color": "White", "weight": "6 kg", "img": "dog3.png",
        "description": "Charlie is a fluffy ball of joy. Perfect for cuddles and short walks!"
    },
    {
        "name": "Daisy", "breed": "Golden Retriever", "age": "2.5 years",
        "gender": "Female", "color": "White", "weight": "13 kg", "img": "dog4.png",
        "description": "Daisy is calm and gentle. She’s great with families and loves affection."
    },
    {
        "name": "Max", "breed": "German Shepherd", "age": "4 years",
        "gender": "Male", "color": "Black", "weight": "15 kg", "img": "dog5.png",
        "description": "Max is protective and intelligent. He’s a brave friend and very obedient."
    },
]

dog_photos = []

# 🪟 Dog Profile Page - Fullscreen
def open_dog_profile(dog):
    profile = Toplevel(root)
    profile.title(f"{dog['name']}'s Profile")
    profile.state('zoomed')
    profile.configure(bg="white")

    Label(profile, text=f"{dog['name']}'s Profile", font=("Arial", 28, "bold"), bg="white").pack(pady=20)

    content = Frame(profile, bg="white")
    content.pack(pady=10, padx=40, fill=BOTH, expand=True)

    # Left - Big Dog Image
    left = Frame(content, bg="white")
    left.pack(side=LEFT, padx=50)

    img = Image.open(dog["img"])
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    dog_photos.append(photo)

    Label(left, image=photo, bg="white").pack()

    # Right - Dog Details
    right = Frame(content, bg="white")
    right.pack(side=LEFT, padx=50, anchor="n")

    Label(right, text=f"Name: {dog['name']}", font=("Arial", 18, "bold"), bg="white").pack(anchor="w", pady=5)
    Label(right, text=f"Breed: {dog['breed']}", font=("Arial", 16), bg="white").pack(anchor="w", pady=2)
    Label(right, text=f"Age: {dog['age']}", font=("Arial", 16), bg="white").pack(anchor="w", pady=2)
    Label(right, text=f"Gender: {dog['gender']}", font=("Arial", 16), bg="white").pack(anchor="w", pady=2)
    Label(right, text=f"Color: {dog['color']}", font=("Arial", 16), bg="white").pack(anchor="w", pady=2)
    Label(right, text=f"Weight: {dog['weight']}", font=("Arial", 16), bg="white").pack(anchor="w", pady=2)

    # Dog description
    Label(right, text="\nAbout:", font=("Arial", 16, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
    Label(right, text=dog["description"], font=("Arial", 14), wraplength=500, justify=LEFT, bg="white").pack(anchor="w", pady=5)

    Button(profile, text="Adopt Me 🐾", font=("Arial", 14, "bold"),
           bg="#4CAF50", fg="white", padx=20, pady=10).pack(pady=30)

# 🖼️ Dog Gallery Page
def show_dog_gallery():
    gallery = Toplevel(root)
    gallery.title("Available Dogs")
    gallery.state('zoomed')
    gallery.configure(bg="white")

    Label(gallery, text="🐶 Available Dogs for Adoption 🐾", font=("Arial", 26, "bold"), bg="white").pack(pady=30)

    main_frame = Frame(gallery, bg="white")
    main_frame.pack(pady=10)

    row = None
    for i, dog in enumerate(dogs):
        if i % 3 == 0:
            row = Frame(main_frame, bg="white")
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

# 🏠 HOME PAGE


Button(root, text="Available Dogs", font=("Arial", 16, "bold"),
       bg="black", fg="white", padx=40, pady=15, command=show_dog_gallery).pack()

root.mainloop()
