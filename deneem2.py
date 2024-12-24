import customtkinter as ctk
import json

JSON_KULLANICI = "KullaniciDataBase.json"

Kayitli_Hesaplar = {}
aktif_kullanici = None

def verileri_yukle():
    global Kayitli_Hesaplar
    try:
        with open(JSON_KULLANICI, "r") as jkul:
            Kayitli_Hesaplar = json.load(jkul)
    except FileNotFoundError:
        Kayitli_Hesaplar = {}

def kullanici_Kaydet():
    with open(JSON_KULLANICI, "w") as jkul:
        json.dump(Kayitli_Hesaplar, jkul, indent=4)

def giris():
    global aktif_kullanici
    name = kullanici_entry.get()
    password = sifre_entry.get()

    if name in Kayitli_Hesaplar and Kayitli_Hesaplar[name] == password:
        aktif_kullanici = name
        basar_label.configure(text="Giriş Başarılı!", text_color="green")
        ana_ekran()
    else:
        basar_label.configure(text="Hatalı Giriş!", text_color="red")

def kayitOl(kayit_pencere, kullanici_adi_entry, ksifre_entry, ksifreTekrar_entry):
    kullanici_adi = kullanici_adi_entry.get()
    sifre = ksifre_entry.get()
    sifreTekrar = ksifreTekrar_entry.get()

    if kullanici_adi in Kayitli_Hesaplar:
        basar_label.configure(text="Kullanıcı zaten kayıtlı!", text_color="red")
    elif sifre == sifreTekrar:
        Kayitli_Hesaplar[kullanici_adi] = sifre
        kullanici_Kaydet()
        kayit_pencere.destroy()
        basar_label.configure(text="Kayıt Başarılı!", text_color="green")
    else:
        basar_label.configure(text="Şifreler uyuşmuyor!", text_color="red")

def kayitEkran():
    kayit_pencere = ctk.CTkToplevel(form)
    kayit_pencere.geometry("400x350")
    kayit_pencere.title("Kayıt Ol")

    ctk.CTkLabel(kayit_pencere, text="Kayıt Ol", font=("Helvetica", 16)).pack(pady=10)

    ctk.CTkLabel(kayit_pencere, text="Kullanıcı Adı:").place(x=50, y=70)
    kullanici_adi_entry = ctk.CTkEntry(kayit_pencere)
    kullanici_adi_entry.place(x=150, y=70)

    ctk.CTkLabel(kayit_pencere, text="Şifre:").place(x=50, y=120)
    ksifre_entry = ctk.CTkEntry(kayit_pencere, show="*")
    ksifre_entry.place(x=150, y=120)

    ctk.CTkLabel(kayit_pencere, text="Şifre Tekrar:").place(x=50, y=170)
    ksifreTekrar_entry = ctk.CTkEntry(kayit_pencere, show="*")
    ksifreTekrar_entry.place(x=150, y=170)

    ctk.CTkButton(kayit_pencere, text="Kayıt Ol", command=lambda: kayitOl(kayit_pencere, kullanici_adi_entry, ksifre_entry, ksifreTekrar_entry)).place(x=150, y=220)

def ana_ekran():
    global aktif_kullanici
    form.destroy()

    mainS = ctk.CTk()
    mainS.geometry("600x400")
    mainS.title("Ana Ekran")

    ctk.CTkLabel(mainS, text=f"{aktif_kullanici}, Hoş Geldiniz!", font=("Helvetica", 16)).pack(pady=20)

    ctk.CTkButton(mainS, text="Oturumu Kapat", command=mainS.destroy).pack(pady=10)
    ctk.CTkButton(mainS, text="Çıkış", command=mainS.quit).pack(pady=10)

    mainS.mainloop()

# Giriş Ekranı
ctk.set_appearance_mode("System")  # "Light" veya "Dark"
ctk.set_default_color_theme("blue")  # "green" veya "dark-blue"

form = ctk.CTk()
form.geometry("400x300")
form.title("Kullanıcı Giriş Ekranı")

ctk.CTkLabel(form, text="Kullanıcı Girişi", font=("Helvetica", 16)).pack(pady=10)

ctk.CTkLabel(form, text="Kullanıcı Adı:").place(x=50, y=70)
kullanici_entry = ctk.CTkEntry(form)
kullanici_entry.place(x=150, y=70)

ctk.CTkLabel(form, text="Şifre:").place(x=50, y=120)
sifre_entry = ctk.CTkEntry(form, show="*")
sifre_entry.place(x=150, y=120)

basar_label = ctk.CTkLabel(form, text="", font=("Helvetica", 10))
basar_label.pack(pady=10)

ctk.CTkButton(form, text="Giriş", command=giris).place(x=150, y=170)
ctk.CTkButton(form, text="Kayıt Ol", command=kayitEkran).place(x=150, y=210)

form.mainloop()
