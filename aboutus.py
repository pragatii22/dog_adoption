from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Heaven of Happy Hooves")
root.state("zoomed")  
bg_image = Image.open("images/lab.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)
bg_item = canvas.create_image(0, 0, image=bg_photo, anchor="nw")

overlay = Frame(canvas, bg="#000000", padx=40, pady=20)
canvas_overlay = canvas.create_window(root.winfo_width() // 2, 100, window=overlay, anchor="n")

try:
    paw_img = Image.open("images/brown.jpeg").resize((80, 80))
    paw_photo = ImageTk.PhotoImage(paw_img)
    Label(overlay, image=paw_photo, bg="#000000").pack(pady=(0, 15))
except:
    Label(overlay, text="[Paw Image Missing]", fg="white", bg="#000000", font=("Arial", 16)).pack(pady=(0, 15))

Label(overlay, text="Heaven of Happy Hooves", font=("Helvetica", 36, "bold"),
      bg="#000000", fg="white").pack(pady=8)
Label(overlay, text="Rescue, love, adopt:", font=("Helvetica", 22),
      bg="#000000", fg="white").pack(pady=2)
Label(overlay, text="Changing lives paw by paw!", font=("Helvetica", 16, "italic"),
      bg="#000000", fg="white").pack(pady=8)


btn_frame = Frame(canvas, bg="#000000")
canvas_btns = canvas.create_window(root.winfo_width() // 2, 300, window=btn_frame, anchor="n")

Button(btn_frame, text="Adopt Now", font=("Arial", 16), bg="#00d1b2", fg="white", padx=30, pady=8).pack(side=LEFT, padx=20)
Button(btn_frame, text="Visit Us", font=("Arial", 16), bg="#3273dc", fg="white", padx=30, pady=8).pack(side=LEFT, padx=20)


footer_frame = Frame(canvas, bg="#f5f5f5", pady=20, padx=40)
canvas_footer = canvas.create_window(root.winfo_width() // 2, root.winfo_height() - 180, window=footer_frame, anchor="n")

Label(footer_frame, text="⭐ ⭐ ⭐ ⭐ ⭐", font=("Arial", 18), bg="#f5f5f5").pack()
Label(footer_frame, text="Rated 4.9/5 by our happy adopters!", bg="#f5f5f5", font=("Arial", 12)).pack(pady=8)
Label(footer_frame, text="Reviews:", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=(10, 2))

reviews = [
    '"The best place to find your furry friend!" - Jane Doe',
    '"Adopting here changed my life forever!" - John Smith',
    '"Wonderful service and loving pets!" - Emily Taylor'
]
for r in reviews:
    Label(footer_frame, text=r, bg="#f5f5f5", font=("Arial", 11)).pack(anchor="w", padx=10)

Label(footer_frame, text="Follow us: Facebook | Twitter | Instagram", bg="#f5f5f5", fg="blue", font=("Arial", 11)).pack(pady=10)
Label(footer_frame, text="© 2025 Heaven of Happy Hooves. All rights reserved.", bg="#f5f5f5", font=("Arial", 10)).pack()

def resize(event):
    new_bg = bg_image.resize((event.width, event.height))
    canvas.new_bg = ImageTk.PhotoImage(new_bg)
    canvas.itemconfig(bg_item, image=canvas.new_bg)

    canvas.coords(canvas_overlay, event.width // 2, 100)
    canvas.coords(canvas_btns, event.width // 2, 300)
    canvas.coords(canvas_footer, event.width // 2, event.height - 180)

canvas.bind("<Configure>", resize)

root.mainloop()
