a = 0 
b = 1
toplam = 0

while True:
    if a > 4000000:
        break
    c = a
    a = b
    b = b + c
    if a % 2 == 0:
        toplam += a

print(toplam)
