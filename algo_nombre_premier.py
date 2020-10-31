#tester i nombres
def prim(nb):
    for x in range(2, nb-1): #tester si le nb est premeier
        if nb % x == 0:
            return print(f"Le nombre {nb} n'est pas premier.")
    return print(f"Le nombre {nb} est premier.")

def vprime(n):
    for x in range(2, n-1): #tester si le nb est premeier
        if n % x == 0:
            return False
    return True

def liste_prime(z):
    liste = []
    for i in range(2, z):
        if vprime(i):
            liste.append(i)
    return print(liste)

liste_prime(100000)
