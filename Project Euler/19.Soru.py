Aylar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sayac = 0
gun_sayaci = 0

for yil in range(1901,2001):
    if (yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0:
        Aylar = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for gun_sayisi in Aylar:
        for gun in range(1,gun_sayisi+1):
            gun_sayaci += 1
            if gun_sayaci % 6 == 0 and gun == 1:
                sayac += 1
            if gun_sayaci % 7 == 0:
                gun_sayaci = 0
    Aylar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
print(f"Ayın ilk gününe denk gelen Pazar sayısı : {sayac}")
