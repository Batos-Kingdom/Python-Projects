import tkinter as tk

def kaydet():
    metin = yazi.get("1.0", "end-1c")
    with open("notlar.txt", "w", encoding="utf-8") as f:
        f.write(metin)

pencere = tk.Tk()
pencere.title("Karanlık Tema")
pencere.configure(bg="#2b2b2b")

yazi = tk.Text(pencere, bg="#1e1e1e", fg="white", insertbackground="white" )
yazi.pack(fill="both", expand=True)

kaydetButonu= tk.Button(pencere, text="Kaydet", bg="#444", fg="white", command=kaydet)
kaydetButonu.pack()

pencere.mainloop()