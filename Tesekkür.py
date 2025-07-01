import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Öğrenci listesi
ogrenciler = [
    "1.Arda Korkmaz",
    "2.Veysel Can Yıldız",
    "3.Doğanay Duran",
    "4.Fatma Dilara Tiren",
    "5.Ömer Akkuş",
    "6.Arda Deniz Yıldırım",
    "7.Ulaş Doruk Karakuş",
    "8.Yiğit Efe Çınar",
    "9.Emirhan Kartal",
    "10.Ege Karakuş",
    "11.Miraç Meydan",
    "12.Mehmet Ali Çınar",
    "13.Kerim Kılıçoğlu",
    "14.Deniz Akpınar",
    "15.Efe Ersoy",
    "16.Berat Arif Gönül",
    "17.Samed Özkan",
    "18.Kaan Bahçeci",
    "19.Umut Arslan",
    "20.Atakan Kerim",
    "21.Abdurrahman Kütük",
    
]

# Teşekkür mesajlarını sırayla göstermek için
def tesekkur_et():
    def mesaj_goster(i):
        if i < len(ogrenciler):
            ogrenci = ogrenciler[i]
            mesaj = f"{ogrenci} diyor ki:\n\nTeşekkür ederiz hocam! Emekleriniz için minnettarız. 🙏"
            
            messagebox.showinfo("Teşekkür Mesajı", mesaj)
            pencere.after(100, mesaj_goster, i + 1)  # 2 saniye sonra sonraki mesaj

            # Log kaydı
            with open("tesekkur_log.txt", "a", encoding="utf-8") as dosya:
                zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                dosya.write(f"[{zaman}] {ogrenci}: Teşekkür etti.\n")

    mesaj_goster(0)

# Ana pencere
pencere = tk.Tk()
pencere.title("Tüm Öğrencilerden Teşekkür!")
pencere.geometry("450x300")
pencere.configure(bg="#1c1c1c")

# Başlık
etiket = tk.Label(pencere, text="Tüm öğrencilerden bilişim hocamıza teşekkür mesajları!",
                  font=("Arial", 12, "bold"), fg="white", bg="#1c1c1c", wraplength=400)
etiket.pack(pady=30)

# Başlat butonu
buton = tk.Button(pencere, text="👨‍🏫 Teşekkür Mesajlarını Göster", font=("Arial", 12),
                  width=30, height=2, bg="#2196f3", fg="white", command=tesekkur_et)
buton.pack()

# Alt bilgi
alt = tk.Label(pencere, text="by Berat Arif Gönül", fg="gray", bg="#1c1c1c", font=("Courier", 9))
alt.pack(side="bottom", pady=10)

# Pencereyi çalıştır
pencere.mainloop()
