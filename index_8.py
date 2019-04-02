#=========================================================
# while ciklas - kol salyga teisinga/True , tol kartoja

# slaptas_skaicius = 9
# spejimas = 9
#
#
# while spejimas != slaptas_skaicius:
#     spejimas = int(input("iveskite spejima nuo 0 iki 9: "))
#     if spejimas == slaptas_skaicius:
#         print("sveikinu atspejus")
#     else:
#         print("bandykite dar karta")



#=========================================================
# For ciklas - kartoja cikla kazkiek kartu

# slaptas_skaicius = 4
# spejimas = 0
#
# for i in range(5):
#     print(i) #kiek kartu jau prasukta - nuolat dideja
#     spejimas = int(input("iveskite spejima nuo 0 iki 9: "))
#     if spejimas == slaptas_skaicius:
#         print("sveikinu atspejus")
#         break
#     else:
#         print("bandykite dar karta")

#=========================================================
#

# slaptas_skaicius = 4
# spejimas = 0
# sarasas =[1, "bmw", float(),]
#
# for i in sarasas:
#     print(i) #kiek kartu jau prasukta - nuolat dideja
#     spejimas = int(input("iveskite spejima nuo 0 iki 9: "))
#     if spejimas == slaptas_skaicius:
#         print("sveikinu atspejus")
#         break
#     else:
#         print("bandykite dar karta")

#=========================================================
#while

# temperatura = int(input('ivesk temperatura: '))
# while temperatura > 0:
#     print('silta')
#     temperatura = int(input('ivesk temperatura: '))


#=========================================================
# FOR 10 kartu - rubas

# temperatura = 0
#
# for i in range(10):
#     print(i) #kiek kartu jau prasukta - nuolat dideja
#     temperatura = int(input("iveskite temperatura: "))
#     if temperatura > 10:
#         print("eik su sortais")
#         break
#     else:
#         print("dekis palta")

#=========================================================
# bibliotekos importavimas
import random #pilna biblioteka random
print(random.randint(1,10))#isves random skaiciu nuo 1 iki 10

from random import randint #tik integer is random bibliotekos
print(randint(1,10)) #isves random skaiciu nuo 1 iki 10