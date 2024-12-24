import tkinter as tk
import customtkinter as cTk
import json
import Hatalar

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
        Hatalar.basarili()
        ana_ekran()
    else:
        if name in Kayitli_Hesaplar and Kayitli_Hesaplar[name] != password:
            Hatalar.hataliSifre()
            sifre_entry.delete(0, tk.END)
        else:
            Hatalar.hatali()
            kullanici_entry.delete(0, tk.END)
            sifre_entry.delete(0, tk.END)

def kayitOl(kayit, kullanici_adi_entry, ksifre_entry, ksifreTekrar_entry):
    kullanici_adi = kullanici_adi_entry.get()
    sifre = ksifre_entry.get()
    sifreTekrar = ksifreTekrar_entry.get()

    if kullanici_adi in Kayitli_Hesaplar:
        Hatalar.hataliKayit()
    else:
        if sifre == sifreTekrar:
            Kayitli_Hesaplar[kullanici_adi] = sifre
            Hatalar.basariliKayit()
            kullanici_Kaydet()
            kayit.destroy()
        else:
            Hatalar.sifrelerUyusmuyor()


def kayitEkran():
    kayit = cTk.CTkToplevel(form)
    kayit.title("Kayit Ol")
    kayit.geometry("400x350+600+350")
    kayit.grab_set()

    cTk.CTkLabel(kayit, text="Kayit Ol", font=font).pack(pady=20)

    cTk.CTkLabel(kayit, text="Kullanıcı Adı: ", font=("Roboto", 12)).place(x=100, y=70)

    kullanici_adi_entry = cTk.CTkEntry(kayit)
    kullanici_adi_entry.place(x=180, y=70)

    cTk.CTkLabel(kayit, text="Sifre Olusturun: ", font=("Roboto", 12)).place(x=85, y=120)

    ksifre_entry = cTk.CTkEntry(kayit, show="*")
    ksifre_entry.place(x=180, y=120)

    cTk.CTkLabel(kayit, text="Sifrenizi Dogrulayin: ", font=("Roboto", 12)).place(x=63, y=170)

    ksifreTekrar_entry = cTk.CTkEntry(kayit, show="*")
    ksifreTekrar_entry.place(x=180, y=170)

    kayitOl_button = cTk.CTkButton(kayit, text="Kayit Ol", command=lambda: kayitOl(kayit, kullanici_adi_entry, ksifre_entry, ksifreTekrar_entry))
    kayitOl_button.place(x=165, y=220)

    kayit.mainloop()


def ana_ekran():
    global aktif_kullanici
    form.destroy()

    mainS = cTk.CTk()
    mainS.title("Ana Ekran")
    mainS.geometry("950x600+500+200")

    bilgi_label = cTk.CTkLabel(mainS, text=f"{aktif_kullanici} HOS GELDINIZ")
    bilgi_label.pack(pady=10)

    cikis_button = cTk.CTkButton(mainS, text="Cikis", command=mainS.quit)
    cikis_button.pack(side = tk.BOTTOM)

    oturum_kapat = cTk.CTkButton(mainS, text="Oturumu Kapat", command=mainS.quit)
    oturum_kapat.pack(side=tk.BOTTOM)

    mainS.mainloop()

form = cTk.CTk()
verileri_yukle()
form.title("Giriş")
form.config(bg="#101014")
form.geometry("450x350+500+250")
form.resizable(width=False, height=False)

font = ("Roboto", 16)

cTk.CTkLabel(form, text="Kullanıcı Adı", font=font).place(x=150, y=60)

kullanici_entry = cTk.CTkEntry(form, width=150, font=("Roboto", 12))
kullanici_entry.place(x=150, y=92)

cTk.CTkLabel(form, text="Sifre", font=font).place(x=150, y=135)

sifre_entry = cTk.CTkEntry(form, show="*", width=150, font=("Roboto", 12))
sifre_entry.place(x=150, y=167)

giris_button = cTk.CTkButton(form, text="Giris",width = 100, height = 30,command=giris).place(x=170, y=220)

kayit_buton = cTk.CTkButton(form, text="Kayit Ol",width = 100, height = 30, command=kayitEkran).place(x=170, y=260)

form.mainloop()

