from tkinter import *
from PIL import Image, ImageTk
import os

def contact_interface():
    contact = Toplevel()
    contact.title("Contact Us")
    contact.geometry("700x500")
    contact.configure(bg="#fdf6e3")

    contact_frame = Frame(contact, bg="white")
    contact_frame.place(relx=0.5, rely=0.5, anchor="center", width=850, height=600)

    # Load image if exists
    img_path = "images/paw.png"
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = Label(contact_frame, image=photo, bg="white")
        img_label.image = photo  # keep reference
        img_label.pack(pady=10)

    # Contact title
    title_label = Label(contact_frame, text="Contact Us", font=("Helvetica", 20, "bold"), bg="white")
    title_label.pack(pady=10)

    # Contact info text
    contact_text = (
    "🐾 Welcome to Heaven of Happy Hooves!\n\n"
    "At our shelter, every dog is treated like family. We believe that love,\n"
    "care, and a safe home can transform lives — not just for the dogs, but for\n"
    "the people who open their hearts to them. Adopting a rescue dog means\n"
    "giving a second chance to a loyal friend who’s ready to fill your life\n"
    "with joy, companionship, and unconditional love.\n\n"
    "Whether you’re looking to adopt, volunteer, or simply learn more about\n"
    "our mission, we welcome you with open arms.\n\n"
    "Email: happyhooves.adopt@gmail.com\n"
    "Phone: +977-9800000000\n"
    "Location: Kathmandu, Nepal"
)

    info_label = Label(contact_frame, text=contact_text, font=("Arial", 14), bg="white", justify=LEFT)
    info_label.pack(padx=20, pady=10)

    # Close button
    close_btn = Button(contact_frame, text="Close", font=("Arial", 12), bg="#4CAF50", fg="white", command=contact.destroy)
    close_btn.pack(pady=15)
