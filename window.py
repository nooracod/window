from tkinter import Tk, Entry, Button, Label, messagebox, StringVar, OptionMenu
from peewee import *


db = SqliteDatabase('hospital.db')

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    role = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([User])


def handle_user():
    usr = e_usr.get()
    pwd = e_password.get()
    rl = selected_role.get()

    if not usr or not pwd:
        messagebox.showwarning("خطا", "لطفاً تمام فیلدها را پر کنید")
        return

    try:
       
        user_record = User.get(User.username == usr)
        
        
        if user_record.password == pwd:
            messagebox.showinfo("ورود", f"خوش آمدید {user_record.role} {usr}")
        else:
            messagebox.showerror("خطا", "رمز عبور اشتباه است")
            
    except User.DoesNotExist:
       
        User.create(username=usr, password=pwd, role=rl)
        messagebox.showinfo("ثبت نام", f"کاربر جدید ({rl}) با موفقیت ساخته شد")


window = Tk()
window.title("سیستم بیمارستان")
window.geometry('300x300')

Label(window, text="نقش:").pack()
roles = ["Doctor", "Nurse", "Patient"]
selected_role = StringVar(window)
selected_role.set(roles[0])
OptionMenu(window, selected_role, *roles).pack()

Label(window, text="نام کاربری:").pack()
e_usr = Entry(window)
e_usr.pack()

Label(window, text="رمز عبور:").pack()
e_password = Entry(window, show="*")
e_password.pack()

 
Button(window, text="ورود / ثبت نام", command=handle_user, bg="lightblue").pack(pady=20)

window.mainloop()