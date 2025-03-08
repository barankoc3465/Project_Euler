toplam = 1

for i in range(3,1002,2):
    kare = i ** 2
    ara_toplam = 0
    for j in range(4):
        ara_toplam += kare - j*(i-1)
    toplam += ara_toplam

print(toplam)  
