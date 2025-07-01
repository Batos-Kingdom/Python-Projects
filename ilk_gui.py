import tkinter as tk

#Butona tıklanınca çalışan kod
def selamla():
    isim = giris.get()
    sonuc_label.config(text=f"Merhaba, {isim}!")

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Selamla Uygulaması")
pencere.geometry("300x150")

# Giriş etiketi ve kutusu
sayi1 = tk.Label(pencere, text="Sayı 1:")
sayi1.pack(pady=5)

sayi2 = tk.Label(pencere, text="Sayı 2")

giris = tk.Entry(pencere)
giris.pack(pady=5)

# Buton
buton = tk.Button(pencere, text="Selamla", command=selamla)
buton.pack(pady=5)

# Sonuç etiketi
sonuc_label = tk.Label(pencere, text="")
sonuc_label.pack(pady=10)

# Pencereyi çalıştır
pencere.mainloop()
