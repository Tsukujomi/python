#9.1 excersise - unit converter
#===========================================================
print("Sveiki. Programa skirta konvertuoti mylias i kilometrus ir atvirksciai - kilometrus i mylias.")

print("Kuria operacija atliksite?")
print("1 - km->mile")
print("2 - mile->km")

conv_type = 0
km = 0
p = True
p2 = True
mylios = 0
kartoti = 1

#suka tol kol norima kartoti
while kartoti == 1:
    conv_type = int(input("Iveskite Operacijos nr.: "))

    #jei km->mylias
    if conv_type == 1:
        km = int(input("Iveskite kilometrus: "))
        mylios = float(km * 1.6)
        print(f"{km} kilometrai yra {mylios} mylios")
        break

    #jei mylias->km
    elif conv_type == 2:
        mylios = float(input("Iveskite mylias: "))
        km = float(mylios / 1.6)
        print(f"{mylios} mylios yra {km} kilometru")
        break

    #jei blogas pasirinkimas
    else:
        while p == True:
            for i in range(3):
                #tikrinam ar nori kartoti operacija
                print(p)
                print("Neteisingai ivesta verte")
                kartoti_str = str(input("Ar norite kartoti konvertavimą? (T/N): "))
                if kartoti_str == "T":
                    kartoti = 1
                    p = False
                    break
                elif kartoti_str == "N":
                    kartoti = 0
                    p = False
                    break
            # kartoti = 0

        #jei blogas pasirinkimas 3 kartus
    while p2 == True:
        for x in range(3):
            kartoti_str = str(input("Ar norite kartoti? (T/N): "))
            if kartoti_str == "T":
                kartoti = 1
                p2 = False
                break
            elif kartoti_str == "N":
                kartoti = 0
                p2 = False
                break
            else:
                print("Neteisingai ivesta verte")
                break
print("Aciu kad naudojotes programa")