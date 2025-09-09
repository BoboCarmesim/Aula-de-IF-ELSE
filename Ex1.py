import random

num = random.randint(0, 5)

adv = int(input("Estou pensando em um número.Em que número eu pensei? "))

if adv == num:
    print("Parabéns! Você acertou!")
else:
    print(f"Errado! Eu pensei no número {num}.")
