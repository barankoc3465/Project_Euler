sayi = 600851475143

for i in range(int(sayi**0.5)+1,1,-1):
    if sayi % i  == 0:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0 :
                break
        else:
            asal_sayi = i
            break

print(asal_sayi)


