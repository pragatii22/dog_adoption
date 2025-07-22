from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk


def admin_interface():
    
    admin = Toplevel()
    admin.title("Admin Dashboard")
    admin.geometry("900x600")
    admin.configure(bg="lightpink")

    admin_frame = Frame(admin, bg="white")
    admin_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)




    # ------------------ All Functions ------------------
    def logout():
        admin.destroy()
        
        
    def manage_dog():
        dog = Toplevel(admin)
        dog.title("Manage Dog")
        dog.geometry("800x800")
        dog.configure(bg="light blue")
        dog.resizable(False, False)

        add_frame = Frame(dog, bg="white") 
        add_frame.place(relx=0.27, rely=0.1, width=390, height=280) 

        def add_dog():
            name_dog= add_name_entry.get()
            dog_age1 = dog_entry.get()
            dog_id1 = id_entry.get()
            if not name_dog or not dog_age or not dog_id1:
                messagebox.showwarning("Warning!!!", "All fields are required")
                return

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute('''
                 INSERT INTO doginformation (dogname, dogid, dogage)
                VALUES (?, ?, ?)
                ''', (name_dog, dog_id1, dog_age1 ))
            conn.commit()
            conn.close()    

            messagebox.showinfo(" yayy Success", "Dog added successfully")
            add_name_entry.delete(0, END)
            dog_entry.delete(0, END)
            id_entry.delete(0, END)

        def delete_dog():
            dog_id2 = id_num1_entry.get()
            if not dog_id2:
                messagebox.showwarning("Warning!!!", "ID is required")
                return

            conn = sqlite3.connect("users.db")
            cursor= conn.cursor()

            cursor.execute("SELECT * FROM doginformation WHERE dogid = ?", (dog_id2,))
            result1=cursor.fetchone()
            conn.commit()
            conn.close()
            if result1!=None:
                conn= sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute('''
                          DELETE FROM doginformation WHERE dogid = ?
                          ''', (dog_id2,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success yayy", "Dog removed successfully")
                id_num1_entry.delete(0, END)


            else:
                messagebox.showerror("Warning!!!", "ID not found.")



        # ---------- Add Dog Section ----------
        add_label = Label(add_frame, text="Add Dog",bg= "white", fg="black" ,font=("Arial", 18, "bold"))
        add_label.place(x=110,y=10)

        name_label = Label(add_frame, text="Name:", fg="black",bg="white", font=("Arial", 13))
        name_label.place(x=20, y=58)
        add_name_entry = Entry(add_frame, width=20,bg="white", fg="black")
        add_name_entry.place(x=140, y=60)

        dog_age = Label(add_frame, text="Age:", fg="black",bg="white",font=("Arial", 13))
        dog_age.place(x=20, y=105)
        dog_entry = Entry(add_frame, width=20,bg="white", fg="black")
        dog_entry.place(x=140, y=105)

        id_label = Label(add_frame, text="Id number:", fg="black", bg="white", font=("Arial", 13))
        id_label.place(x=20, y=155)
        id_entry = Entry(add_frame, width=20,bg="white", fg="black")
        id_entry.place(x=140, y=150)

    
        btn_save = Button(add_frame, text="Save", fg="Green", width=12, font=("Arial", 14), command=add_dog)
        btn_save.place(x=100, y=200)
    
        #dog frame 
        remove_frame = Frame(dog, bg="white") 
        remove_frame.place(relx=0.27, rely=0.5, width=390, height=280) 

        # ---------- Remove dog ----------
        remove_dog = Label(remove_frame, text="Remove Dog",bg= "white", fg="black", font=("Arial", 18, "bold"))
        remove_dog.place(x=85,y=20)

        id_num_label = Label(remove_frame, text="Dog ID:", fg="black",bg="white", font=("Arial", 14))
        id_num_label.place(x=25, y=90)
        id_num1_entry = Entry(remove_frame, width=20,bg="white",fg="black")
        id_num1_entry.place(x=157, y=90)

    

        btn_del = Button(remove_frame, text="Delete", fg="blue", width=12, font=("Arial", 14),command= delete_dog)
        btn_del.place(x=100, y=160)

        # ------------------ Image ------------------
    img = Image.open("images/seti.jpeg")
    img = img.resize((880, 560))
    photo1 = ImageTk.PhotoImage(img)
    img_label1 = Label(admin_frame, image=photo1)
    img_label1.place(x=0, y=0)

    

    #  Buttons on Left
    manage_doctors_btn = Button(admin_frame, text="Manage Dog", font=("Arial", 14), width=18, command=manage_dog)
    manage_doctors_btn.place(x=30, y=150)

    admin_logout_btn = Button(admin_frame, text="Log Out", font=("Arial", 14), width=18, fg="red",command=logout)
    admin_logout_btn.place(x=30, y=230)




    admin.mainloop()