birler = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
onlar = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
yuzler = ["one hundred","two hundred","three hundred","four hundred"
          , "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
binler = ["one thousand"]
Sozluk = dict()
Sozluk[1000] = binler[0]

for i in range(9):
    Sozluk[i+1] = birler[i]
    Sozluk[(i+1)*10] = onlar[i]
    Sozluk[(i+1)*100] = yuzler[i]

Liste = list()

for sayi in range(1,1001):
    kelime = str(sayi)[::-1]
    for indis in range(len(kelime)):
        rakam = int(kelime[indis])*(10**indis)
        if rakam != 0:
            Liste.append(rakam)

toplam = 40 # 11 ile 20 arasındaki fark

for sayi in Liste:
    for karakter in str(Sozluk[sayi]):
        if karakter.isalpha() == True:
            toplam += 1

ve = "and"

for i in range(100,1000):
    toplam += len(ve)

toplam -= 9*3 # yüzün katlarında end yok

print(toplam)
