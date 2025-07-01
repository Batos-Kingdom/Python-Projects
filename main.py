import random

def sayi_tahmin_oyunu():
    hedef_sayi = random.randint(1, 100)  # 1-100 arasında rastgele sayı
    tahmin_sayisi = 0

    print("Sayı Tahmin Oyununa Hoşgeldin! 1 ile 100 arasında bir sayı tuttum.")

    while True:
        tahmin = input("Tahminini gir: ")

        # Tahminin sayı olup olmadığını kontrol et
        if not tahmin.isdigit():
            print("Lütfen sadece sayı gir.")
            continue

        tahmin = int(tahmin)
        tahmin_sayisi += 1

        if tahmin < hedef_sayi:
            print("Daha büyük bir sayı söyle.")
        elif tahmin > hedef_sayi:
            print("Daha küçük bir sayı söyle.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettin.")
            break

# Oyunu başlat
sayi_tahmin_oyunu()

input("Kapatmak için bir tuşa basınız...")