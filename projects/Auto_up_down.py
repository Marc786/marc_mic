import random



def guess():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError
    rnb = random.randint(0,tranche)
    check = True
    while check:
        guess = int(input("Choisissez un nombre au hazard :"))
        if guess == rnb:
            check = False
            print("gg")
        elif guess > rnb:
            print("Trop Haut!")
        elif guess < rnb:
            print("Trop Bas!")

def guess_auto_random():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError
    nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
    check = True
    coups = 0
    while check:
        coups += 1
        guess = random.randint(0, tranche)
        if guess == nombre:
            check = False
    print(f'Le bot a trouve en {coups} coups.')

def guess_auto_algo():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError
    nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
    check = True
    coups = 0
    while check:
        coups += 1
        
