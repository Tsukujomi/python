# # #pirmas būdas išrtraukti info iš failo
# # ====================================================================
# with open('rezultatas.txt') as failas:
#     rezultatas = failas.read()
#     print(rezultatas)
#
#
# # #antras būdas išrtraukti info iš failo
# # ====================================================================
# failas = open('rezultatas.txt')
# rezultatas = failas.read()
# print(rezultatas)
# failas.close()


# #būdas įrašyti info į failą
# ====================================================================
# with open('rezultatas.txt', 'w') as failas:
#     rezultatas = failas.write('aaa')
#     print(rezultatas)


# with open('km.txt') as failas:
#     rezultatas = failas.read()
#     sarasas = rezultatas.split('/n')
#
# for i in sarasas:
#     sk = int(sarasas)
#     sk = str(sk*1.6)
#     with open('mylios.txt', 'w') as failas:
#         for x in sarasas:
#             failas.write(sk)

import random

secret = random.randint(1, 30)
attempts = 0

with open("rezultatas.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score (attempts): " + str(best_score))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        if attempts < best_score:
            with open("rezultatas.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")