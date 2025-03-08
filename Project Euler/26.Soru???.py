en_uzun = 0
for d in range(2,10):
    bolum = 1 / d
    kesir = str(bolum).split(".")[1]
    for rakam_indisi in range(len(kesir)):
        if kesir[rakam_indisi] == kesir:
            