import random



def guess():
    parties = 0
    replay = True
    points = 0
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError
    while replay:
        parties += 1
        rnb = random.randint(0, tranche)
        check = True
        coups = 0
        while check:
            coups += 1
            guess = int(input(f"Choisissez un nombre au hazard entre 0 et {tranche} :"))
            if guess == rnb:
                check = False
                print("gg")
            elif guess > rnb:
                print("Trop Haut!")
            elif guess < rnb:
                print("Trop Bas!")
        print(f'Vous avez trouve en {coups} coups. ') # ==, <=, >=, <, >, !=, and, or
        if coups == 1:
            print(f'Vous avez obtenu 10 points.')
            points += 10
        elif coups == 2:
            print(f'Vous avez obtenu 7 points.')
            points += 7
        elif coups == 3 or coups == 4:
            print(f'Vous avez obtenu 5 points.')
            points += 5
        elif coups == 5 or coups == 6:
            print(f'Vous avez obtenu 3 points.')
            points += 3
        elif coups > 6:
            print(f'Vous avez rien obtenu (Vous etes nul)')
        
        question2 = input('Voulez-vous un recapitulatif des points? ([y] = oui, [n] = non)')
        if question2 == 'y':
            print(f'{points} points')
        question = input('Voulez-vous rejouer? ([y] = oui, [n] = non)')
        if question == 'n':
            replay = False
        
    print(f'Vous avez obtenu {points} points en {parties} parties')


def guess_auto_random():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError("La tranche doit etre superieur a 0")
    nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
    if nombre > tranche:
        raise ValueError("Le nombre doit etre plus petit ou egal a la tranche")
    check = True
    coups = 0
    while check:
        coups += 1
        guess = random.randint(0, tranche)
        if guess == nombre:
            check = False
    print(f'Le bot a trouve en {coups} coups.')

def guess_auto_algo():
    error = True
    tranche = 0
    nombre = 0
    while error:
        try:
            tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
            if tranche < 0:
                raise ValueError("La tranche doit etre superieur a 0, reessayez")
            error = False
        except ValueError as identifier:
            print(identifier)
    error = True
    while error:
        try:
            nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
            if nombre > tranche:
                raise ValueError("Le nombre doit etre plus petit ou egal a la tranche, reessayez")
            error = False
        except ValueError as identifier:
            print(identifier)
    check = True
    coups = 0
    low_guess = 0
    high_guess = tranche
    #guess = random.randint(0, tranche)
    guess = tranche/2
    print(guess)
    while check:
        coups += 1
        if guess == nombre:
            check = False
        elif guess > nombre:
            high_guess = guess
            guess = guess - (guess-low_guess)//2
            print(guess)
        elif guess < nombre:
            low_guess = guess
            guess = guess + (high_guess-guess)//2
            print(guess)
    print(f'Le bot a trouve en {coups} coups.')

guess_auto_algo()
