Pisagor_ucluleri = [(a*b*int((a**2+b**2)**0.5)) 
                    for a in range(1,1000) 
                    for b in range(1,1000)
                    if a + b + (a**2+b**2)**0.5 == 1000
                    if b > a]

print(Pisagor_ucluleri)

