import customtkinter as ctk

def custom_messagebox(title, message):
    # Yeni bir pencere (Toplevel) oluştur
    msg_box = ctk.CTkToplevel()
    msg_box.geometry("300x150")
    msg_box.title(title)
    msg_box.grab_set()  # Mesaj kutusunu modal yapar

    # Mesaj metni
    ctk.CTkLabel(msg_box, text=message, font=("Helvetica", 14), wraplength=280).pack(pady=20)

    # Kapatma butonu
    ctk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)

# Örnek Kullanım
def show_message():
    custom_messagebox("Bilgilendirme", "Bu bir özel mesaj kutusudur!")

# Ana Pencere
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("CustomTkinter Örnek")

ctk.CTkButton(app, text="Mesaj Göster", command=show_message).pack(pady=50)

app.mainloop()
