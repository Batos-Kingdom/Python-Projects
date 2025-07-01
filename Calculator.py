def topla(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    if sayi2 == 0:
        raise ZeroDivisionError("Sıfıra bölme hatası!")
    return sayi1 / sayi2

def mod_alma(sayi1, sayi2):
    return sayi1 % sayi2

def hesap_makinesi():
    while True:
        print("\n** HESAP MAKİNESİ **")
        try:
            islem = input("İşlem girin (+, -, *, /, %, çıkmak için q): ")

            if islem == 'q':
                print("Çıkılıyor...")
                break

            sayi1 = int(input("1. sayıyı giriniz: "))
            sayi2 = int(input("2. sayıyı giriniz: "))

            if islem == '+':
                sonuc = topla(sayi1, sayi2)
            elif islem == '-':
                sonuc = cikarma(sayi1, sayi2)
            elif islem == '*':
                sonuc = carpma(sayi1, sayi2)
            elif islem == '/':
                sonuc = bolme(sayi1, sayi2)
            elif islem == '%':
                sonuc = mod_alma(sayi1, sayi2)
            else:
                print("Geçersiz işlem! (+, -, *, /, %, q)")
                continue

            print(f"Sonuç: {sonuc}")

            with open("log.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"{sayi1} {islem} {sayi2} = {sonuc}\n")

        except ValueError:
            print("Lütfen sayıları düzgün girin!")
        except ZeroDivisionError as z:
            print(z)
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

# Programı başlat
hesap_makinesi()

input("\nKapatmak için bir tuşa basınız...")
