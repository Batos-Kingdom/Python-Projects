def cinsiyet_sec():
    secim = input("Cinsiyetinizi girin (Kadın: K, Erkek: E): ").upper()
    return secim

def kilo_al():
    return int(input("Kilonuzu girin (kg): "))

def boy_al():
    return int(input("Boyunuzu girin (cm): "))

def ideal_kilo_hesapla(cinsiyet, boy):
    if cinsiyet == 'K':
        ideal = 45.5 + 2.3 * ((boy / 2.54) - 60)
    elif cinsiyet == 'E':
        ideal = 50 + 2.3 * ((boy / 2.54) - 60)
    else:
        print("Hatalı cinsiyet seçimi.")
        return None
    return round(ideal, 2)

def hesaplama():
    cinsiyet = cinsiyet_sec()
    boy = boy_al()
    kilo = kilo_al()

    ideal = ideal_kilo_hesapla(cinsiyet, boy)

    if ideal is not None:
        print(f"\nİdeal kilonuz: {ideal} kg")
        fark = kilo - ideal
        if fark > 0:
            print(f"{fark:.1f} kg fazlanız var.")
        elif fark < 0:
            print(f"{-fark:.1f} kg almanız gerekebilir.")
        else:
            print("Tebrikler! İdeal kilonuzdasınız. 🎉")

# Programı çalıştır
hesaplama()

input("Kapatmak için bir tuşa tıklayınız...")
