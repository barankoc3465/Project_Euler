ucgen = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
Liste = [i for i in ucgen.split("\n")]
Yeni_liste = [i.split() for i in Liste]
Yepyeni_liste = list()

for satir in Yeni_liste:
    Yeni = list()
    for sutun in satir:
        if sutun[0] != "0":
            Yeni.append(int(sutun))
        else:
            Yeni.append(int(str(sutun[1])))
    Yepyeni_liste.append(Yeni)

for satir_indisi in range(len(Yepyeni_liste)-2,-1,-1):
    for sutun_indisi in range(len(Yepyeni_liste[satir_indisi])):
        if Yepyeni_liste[satir_indisi+1][sutun_indisi] > Yepyeni_liste[satir_indisi+1][sutun_indisi+1]:
            Yepyeni_liste[satir_indisi][sutun_indisi] += Yepyeni_liste[satir_indisi+1][sutun_indisi]
        else:
            Yepyeni_liste[satir_indisi][sutun_indisi] += Yepyeni_liste[satir_indisi+1][sutun_indisi+1]
            
print(Yepyeni_liste[0][0])