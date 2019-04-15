# #9.1 excersise - unit converter
# #===========================================================
# print("Sveiki. Programa skirta konvertuoti mylias i kilometrus ir atvirksciai - kilometrus i mylias.")
#
# print("Kuria operacija atliksite?")
# print("1 - km->mile")
# print("2 - mile->km")
#
# conv_type = 0
# km = 0
# mylios = 0
# kartoti = 1
# teisingas_pasirinkimas = True
#
# #suka tol kol norima kartoti
# while kartoti == 1:
#     conv_type = int(input("Iveskite Operacijos nr.: "))
#
#     #jei km->mylias
#     if conv_type == 1:
#         km = int(input("Iveskite kilometrus: "))
#         mylios = float(km * 1.6)
#         print(f"{km} kilometrai yra {mylios} mylios")
#         teisingas_pasirinkimas = False
#
#
#     #jei mylias->km
#     elif conv_type == 2:
#         mylios = float(input("Iveskite mylias: "))
#         km = float(mylios / 1.6)
#         print(f"{mylios} mylios yra {km} kilometru")
#         teisingas_pasirinkimas = False
#
#     else:
#         teisingas_pasirinkimas = False
#         print('Neteisingas pasirinkimas')
#
#     while not teisingas_pasirinkimas:
#         for i in range(3):
#             print(i)
#             kartoti_str = str(input("Ar norite kartoti? (T/N): "))
#             if kartoti_str == 'T':
#                 kartoti = True
#                 teisingas_pasirinkimas = True
#                 print(teisingas_pasirinkimas)
#                 break
#             elif kartoti_str == 'N':
#                 kartoti = False
#                 teisingas_pasirinkimas = True
#                 break
#             else:
#                 print('neteisingai ivesta verte')
#
# print("Aciu kad naudojotes programa")


#9.2 excersise - fizz buzz
#===========================================================
#
# print ("Sveiki")
# kartoti = True
#
# while kartoti:
#     skaicius_isvedimui = 0
#     skaicius = int(input("Įveskite skaičių nuo 0 iki 100: "))
#     if 0<= skaicius <= 100:
#         for i in range(skaicius+1):
#             if ((skaicius_isvedimui % 3) == 0 and (skaicius_isvedimui % 5) == 0):
#                 print("fizzbuzz")
#             elif(skaicius_isvedimui % 3) == 0:
#                 print("fizz")
#             elif (skaicius_isvedimui % 5) == 0:
#                 print("buzz")
#             else:
#                 print(skaicius_isvedimui)
#             skaicius_isvedimui = skaicius_isvedimui + 1
#         teisingas_pasirinkimas = False
#     else:
#         teisingas_pasirinkimas = False
#         print ("Blogai įvestas skaičius")
#
#
#     #tikrinimas ar nori kartoti
#     n = 0 #blogos vertes skaitiklis
#     while not teisingas_pasirinkimas:
#         for i in range(3):
#             kartoti_str = str(input("Ar norite kartoti? (T/N): "))
#             if kartoti_str == 'T':
#                 kartoti = True
#                 teisingas_pasirinkimas = True
#                 break
#             elif kartoti_str == 'N':
#                 kartoti = False
#                 teisingas_pasirinkimas = True
#                 break
#             else:
#                 print('Neteisingai ivesta verte')
#                 n = n + 1
#         if n > 2:
#             kartoti = False
#             teisingas_pasirinkimas = True
#
#
# print("Aciu kad naudojotes programa")

#9.3 excersise - Make string lowercase
#===========================================================
#
# answer = "today is A GREAT day"
# print(answer)
# print(answer.lower()) #viskas iš mažosios
# print(answer.upper()) #viskas iš didžiosios
# print(answer.capitalize()) #tik pirmas žodis iš didžiosios
# print(answer.title()) #kiekvienas žodis iš didžiosios

#Joining strings
#===========================================================

# str_one = "Labas"
# str_two = "Pasauli"
# print(str_one + str_two)
# print(str_one + " " + str_two)
# print("%s %s" % (str_one, str_two))
# print("{0}   {1}".format(str_one, str_two))