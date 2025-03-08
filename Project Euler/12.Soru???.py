sayi = 1
bolen = 0

while bolen < 50: 
    print(sayi)
    bolen = 0
    sayi += 1
    for i in range(1,sayi+1):
        if sayi % i == 0:
            bolen += 1
            
print(sayi)


n = 1
triangle_number = 1
while True:
    count = 0
    for i in range(1, int(triangle_number**0.5) + 1):
        if triangle_number % i == 0:
            count += 2
    if int(triangle_number**0.5) ** 2 == triangle_number:
        count -= 1
    if count > 500:
        print(triangle_number)
        break
    n += 1
    triangle_number += n
    