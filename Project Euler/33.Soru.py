Liste = list()
for pay in range(10,100):
    for payda in range(10,100):
        if str(pay)[1] == str(payda)[0] and "0" != str(payda)[1]:
            bolum = int(str(pay)[0]) / int(str(payda)[1])
            if pay / payda == bolum:
                Liste.append(bolum)

sum = sum(i for i in Liste)
payda = 1
while int(sum) != sum:
    sum *= 10
    payda *= 10

print(payda)