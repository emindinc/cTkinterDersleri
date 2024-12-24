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
        basar = cTk.CTkLabel(text="Giris Basarili", font=font)
        basar.pack(side=tk.BOTTOM)
        Hatalar.basarili()
        basar.destroy()
        ana_ekran()
    else:
        if name in Kayitli_Hesaplar and Kayitli_Hesaplar[name] != password:
            hata = cTk.CTkLabel(text="Sifre Yanlis!", font=font)
            hata.pack(side=tk.BOTTOM)
            Hatalar.hataliSifre()
            hata.destroy()
            sifre_entry.delete(0, tk.END)
        else:
            hata = cTk.CTkLabel(text="Hatali Giris!", font=font)
            hata.pack(side=tk.BOTTOM)
            Hatalar.hatali()
            hata.destroy()
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

    font = ("Helvetica", 9)  # Define the font as a tuple

    cTk.CTkLabel(kayit, text="Kayit Ol", font=font).pack(pady=20)

    cTk.CTkLabel(kayit, text="Kullanıcı Adı: ", font=("Roboto", 12)).place(x=100, y=70)

    kulla