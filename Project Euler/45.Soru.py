def T(n):
    return n * (n + 1) / 2

def is_P(n):
    kontrol_P =  (1 + (1 + 24*n)**0.5) / 6
    if int(kontrol_P) == kontrol_P:
        return True

def is_H(n):
    kontrol_H = (1 + (1 + 8*n)**0.5) / 4
    if int(kontrol_H) == kontrol_H:
        return True
    
adet = 0
t = 0 
while adet != 3:
    t += 1
    tringular_sayi = T(t)
    if is_P(tringular_sayi) == True and is_H(tringular_sayi) == True:
        adet += 1

print(int(tringular_sayi))