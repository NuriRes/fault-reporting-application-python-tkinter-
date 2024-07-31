import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tc_dogrulama
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

form = tk.Tk()
form.config(bg="black")
form.geometry("300x300")
form.title("Ariza Bildirim Uygulaması")
lbl_baslık = tk.Label(form, text="Arıza Bildirim Uygulaması", bg="black", fg="white", font="times 17 bold")
lbl_baslık.pack()

lbl_ad = tk.Label(form, text="Kullanıcı adı:", bg="black", fg="white", font="times 11 bold")
lbl_ad.place(x=20, y=90)

lbl_sifre = tk.Label(form, text="sifre:", bg="black", fg="white", font="times 12 bold")
lbl_sifre.place(x=20, y=130)

entry_ad = tk.Entry(form)
entry_ad.place(x=120, y=95)
entry_sifre = tk.Entry(form, show="*")
entry_sifre.place(x=120, y=135)

def giris():
    if entry_ad.get() == "nuri" and entry_sifre.get() == "1234":
        msg = messagebox.showinfo("Tebrikler", message="Giriş Başarılı")
        if msg == "ok":
            basvuru_formu = tk.Toplevel()
            basvuru_formu.geometry("350x350")
            basvuru_formu.title("Ariza Bildirim Formu")
            basvuru_formu.config(bg="yellow")
            baslık_label = tk.Label(basvuru_formu, text="Arıza Bildirim Formu", bg="yellow", fg="red", font="times 20 bold")
            baslık_label.pack()
            label_ad = tk.Label(basvuru_formu, text="Ad-Soyad", font="consoles 12 italic", bg="yellow", fg="black").place(x=40, y=50)
            label_tc = tk.Label(basvuru_formu, text="Tc-No", font="consoles 12 italic", bg="yellow", fg="black").place(x=40, y=90)
            label_modem = tk.Label(basvuru_formu, text="Modem Tipi", font="consoles 12 italic", bg="yellow", fg="black").place(x=40, y=130)
            label_ariza = tk.Label(basvuru_formu, text="Arıza Tipi", font="consoles 12 italic", bg="yellow", fg="black").place(x=40, y=170)
            label_adres = tk.Label(basvuru_formu, text="Adres", font="consoles 12 italic", bg="yellow", fg="black").place(x=40, y=210)
            label_mail = tk.Label(basvuru_formu, text="Mail", font="consoles 12 italic", bg="yellow", fg="black").place(x=40, y=250)

            entry_ad_soyad = tk.Entry(basvuru_formu)
            entry_ad_soyad.place(x=140, y=50)

            entry_tc_no = tk.Entry(basvuru_formu)
            entry_tc_no.place(x=140, y=90)

            liste = ["Tmp", "KMNR", "2TMNX", "MTPL", "NMPY", "PNDAS"]
            combo_modem = ttk.Combobox(basvuru_formu, values=liste)
            combo_modem.place(x=140, y=130)

            liste1 = ["Kablo", "Giriş Arızalı", "Wifi Çalışmıyor", "İnternet Çekmiyor"]
            combo_ariza = ttk.Combobox(basvuru_formu, values=liste1)
            combo_ariza.place(x=140, y=170)

            entry_adres = tk.Entry(basvuru_formu)
            entry_adres.place(x=140, y=210)

            entry_mail = tk.Entry(basvuru_formu)
            entry_mail.place(x=140, y=250)

            def oluştur():
                kosul = tc_dogrulama.Tc(entry_tc_no.get())

                if kosul:
                    msgm = messagebox.showinfo("Başarıyla Oluştu", message="Arıza Bildiriminiz Gerçekleştirildi.")
                    
                    if msgm == "ok":
                        masaustu_yolu = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                        dosya_adi = os.path.join(masaustu_yolu, "ariza_bildirimi.pdf")
                        c = canvas.Canvas(dosya_adi, pagesize=letter)
                        c.drawString(100, 750, f"Ad-Soyad: {entry_ad_soyad.get()}")
                        c.drawString(100, 730, f"Tc-No: {entry_tc_no.get()}")
                        c.drawString(100, 710, f"Modem Tipi: {combo_modem.get()}")
                        c.drawString(100, 690, f"Arıza Tipi: {combo_ariza.get()}")
                        c.drawString(100, 670, f"Adres: {entry_adres.get()}")
                        c.drawString(100, 650, f"Mail: {entry_mail.get()}")
                        c.save()
                else:
                    messagebox.showerror("Başarılı", "Tc Kimlik Numaranızı Doğru Girdiğinize Emin Olunuz")

            buton = tk.Button(basvuru_formu, text="Oluştur", command=oluştur).place(x=150, y=290)
            basvuru_formu.mainloop()

def iptal():
    pass

btn_giris = tk.Button(form, text="Giriş", activebackground="green", command=giris).place(x=120, y=180, width=60)
btn_iptal = tk.Button(form, text="İptal", activebackground="red", command=iptal)
btn_iptal.place(x=190, y=180, width=60)

form.mainloop()
