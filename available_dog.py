from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Available Dogs")
root.geometry("900x600")

# Sample Dog Data
dogs = [
    {"name": "Buddy", "breed": "Labrador", "age": "2 years", "gender": "Male", "img": "dog1.png"},
    {"name": "Lucy", "breed": "Beagle", "age": "1.5 years", "gender": "Female", "img": "dog2.png"},
    {"name": "Charlie", "breed": "Pomeranian", "age": "3 years", "gender": "Male", "img": "dog3.png"},
    {"name": "Daisy", "breed": "Golden Retriever", "age": "2.5 years", "gender": "Female", "img": "dog4.png"},
    {"name": "Max", "breed": "German Shepherd", "age": "4 years", "gender": "Male", "img": "dog5.png"},
]

dog_photos = []
details_labels = []

def show_dogs():
    for widget in content_frame.winfo_children():
        widget.destroy()
    dog_photos.clear()
    details_labels.clear()

    for i, dog in enumerate(dogs):
        # Image Section
        img = Image.open(dog["img"])
        img = img.resize((120, 120))
        photo = ImageTk.PhotoImage(img)
        dog_photos.append(photo)

        # Frame for each dog block
        dog_frame = Frame(content_frame, padx=20, pady=10)
        dog_frame.grid(row=0, column=i)

        btn = Button(dog_frame, image=photo, command=lambda d=dog, lbl=None, f=dog_frame: show_details_below(d, f))
        btn.pack()

        # Empty label to hold details later
        details_lbl = Label(dog_frame, text="", font=("Arial", 10))
        details_lbl.pack()
        details_labels.append(details_lbl)

def show_details_below(dog, frame):
    text = f"Name: {dog['name']}\nBreed: {dog['breed']}\nAge: {dog['age']}\nGender: {dog['gender']}"
    for lbl in details_labels:
        lbl.config(text="")  # Clear others
    for widget in frame.winfo_children():
        if isinstance(widget, Label):
            widget.config(text=text)

# Main GUI
title = Label(root, text="Available Dogs", font=("Arial", 20, "bold"))
title.pack(pady=10)

show_btn = Button(root, text="Show Dogs", font=("Arial", 14), command=show_dogs)
show_btn.pack(pady=10)

content_frame = Frame(root)
content_frame.pack(pady=20)

root.mainloop()
