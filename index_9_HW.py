#9.1 excersise - unit converter
#===========================================================
print("Sveiki. Programa skirta konvertuoti mylias i kilometrus ir atvirksciai - kilometrus i mylias.")

print("Kuria operacija atliksite?")
print("1 - km->mile")
print("2 - mile->km")

conv_type = 0
km = 0
mylios = 0
kartoti = 1
teisingas_pasirinkimas = True

#suka tol kol norima kartoti
while kartoti == 1:
    conv_type = int(input("Iveskite Operacijos nr.: "))

    #jei km->mylias
    if conv_type == 1:
        km = int(input("Iveskite kilometrus: "))
        mylios = float(km * 1.6)
        print(f"{km} kilometrai yra {mylios} mylios")
        teisingas_pasirinkimas = False

    #jei mylias->km
    elif conv_type == 2:
        mylios = float(input("Iveskite mylias: "))
        km = float(mylios / 1.6)
        print(f"{mylios} mylios yra {km} kilometru")
        teisingas_pasirinkimas = False

    else:
        for i in range (3):
            kartoti_str = str(input("Ar norite kartoti? (T/N): "))
            if kartoti_str == 'T':
                kartoti = True
            elif kartoti == 'N':
                kartoti = False
        kartoti = False
        print('nemoki skaityti ko praso')

    while not teisingas_pasirinkimas:
        for i in range(3):
            kartoti_str = str(input("Ar norite kartoti? (T/N): "))
            if kartoti_str == 'T':
                kartoti = True
                teisingas_pasirinkimas = True
                break
            elif kartoti_str == 'N':
                kartoti = False
                teisingas_pasirinkimas = True
                break
            else:
                print('neteisingai ivesta verte')
        teisingas_pasirinkimas = True
        kartoti = False
        print('nemoki skaityti ko praso')

print("Aciu kad naudojotes programa")