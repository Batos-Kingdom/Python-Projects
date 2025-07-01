import random

def sayi_oyunu():
    hedef_sayi = random.randint(1,200)
    sayi_tahmin=0
    
    print("Sayı Tahmin Oyununa Hoşgeldin! Bir sayı tuttum bil bakalım :D \n")
    
    print("DEMO\n")
    
    while True:
       tahmin = input("Sayıyı tahmin et (1-200)")
       
       if not tahmin.isdigit():
           print("Sadece sayı giriniz: ")
           continue
       
       tahmin=int(tahmin)
       sayi_tahmin += 1
       
       if tahmin < hedef_sayi:
           print("Tahmini yükselt")
       elif tahmin > hedef_sayi:
           print("Tahmini düşür")
       else:
           print(f"Tebrik ederim! {sayi_tahmin} denemede doğru tahmine ulaştın.\n")
           print("\nBu oyunu geliştirmeye devam edeceğim!\n")
           break
       
sayi_oyunu()

input("Kapatmak bir tuşa basınız.")