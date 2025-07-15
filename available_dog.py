from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Dog Adoption")
root.geometry("800x600")

dogs = [
    {"name": "Buddy", "breed": "Labrador", "age": "2 years", "gender": "Male", "img": "dog1.png"},
    {"name": "Lucy", "breed": "Beagle", "age": "1.5 years", "gender": "Female", "img": "dog2.png"},
    {"name": "Charlie", "breed": "Pomeranian", "age": "3 years", "gender": "Male", "img": "dog3.png"},
    {"name": "Daisy", "breed": "Golden Retriever", "age": "2.5 years", "gender": "Female", "img": "dog4.png"},
    {"name": "Max", "breed": "German Shepherd", "age": "4 years", "gender": "Male", "img": "dog5.png"},
]

dog_photos = []

def show_details(dog):
    top = Toplevel(root)
    top.title(dog["name"])
    top.geometry("300x200")
    
    Label(top, text=f"Name: {dog['name']}", font=("Arial", 14)).pack(pady=5)
    Label(top, text=f"Breed: {dog['breed']}", font=("Arial", 14)).pack(pady=5)
    Label(top, text=f"Age: {dog['age']}", font=("Arial", 14)).pack(pady=5)
    Label(top, text=f"Gender: {dog['gender']}", font=("Arial", 14)).pack(pady=5)

def show_dogs():
    y_start = 100
    x_start = 30
    for index, dog in enumerate(dogs):
        img = Image.open(dog["img"])
        img = img.resize((120, 120))
        photo = ImageTk.PhotoImage(img)
        dog_photos.append(photo)  # Prevent garbage collection

        btn = Button(root, image=photo, command=lambda d=dog: show_details(d))
        btn.place(x=x_start + (index % 5) * 150, y=y_start)

# Main Button
available_btn = Button(root, text="Available Dogs", font=("Arial", 16), command=show_dogs)
available_btn.pack(pady=20)

root.mainloop()
