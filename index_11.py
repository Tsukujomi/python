listas = [1, 2, 3]

# for i in listas:
#     print(i)

##pridėti elementą į listą
# listas.append(4)
# print(listas)

# #keisti listo elementa - skaiciuojasi nuo 0
# listas[2]=5
# print(listas)
#
# #listo ilgis - len
# print(len(listas))

# with open("score_list.txt", "r") as score_file:
#     score_list = json.loads(score_file.read())
#     print("Top scores: " + str(score_list))
#
# while True:
# import random
#
# secret = random.randint(1, 30)
# attempts = 0
#
# while True:
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#     attempts += 1
#
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number " + str(secret))
#         print("Attempts needed: " + str(attempts))
#         break
#     elif guess > secret:
#         print("Your guess is not correct... try something smaller")
#     elif guess < secret:
#         print("Your guess is not correct... try something bigger")

#dictionary
profilis = {
    'vardas' : 'Benas',
    'pavarde' : 'Jak'
}

profilis['nuotaika'] = 'gera'

print(profilis)

