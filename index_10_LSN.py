# #pirmas būdas išrtraukti info iš failo
# ====================================================================
# with open('rezultatas.txt') as failas:
#     rezultatas = failas.read()
#     print(rezultatas)
#

# #antras būdas išrtraukti info iš failo
# ====================================================================
# failas = open('rezultatas.txt')
# rezultatas = failas.read()
# print(rezultatas)
# failas.close()


# #būdas įrašyti info į failą
# ====================================================================
# with open('rezultatas.txt', 'w') as failas:
#     rezultatas = failas.write('aaa')
#     print(rezultatas)


with open('km.txt') as failas:
    rezultatas = failas.read()
    sarasas = rezultatas.split('/n')

for i in sarasas:
    sk = int(sarasas)
    sk = str(sk*1.6)
    with open('mylios.txt', 'w') as failas:
        for x in sarasas:
            failas.write(sk)
