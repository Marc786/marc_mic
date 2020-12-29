import time


def vprime(n):
    for x in range(2, n-1):
        if n % x == 0:
            return False
    return True

def liste_prime(z):
    liste = []
    for i in range(2, z):
        if vprime(i):
            liste.append(i)
    return print(liste)
    
def liste2(z):
    liste = []
    for i in range(2, z):
        verif = True
        for x in range(2, i-1):
            if i % x == 0:
                verif = False
                break
        if verif:
            liste.append(i)
    return liste

r = 100
# prime = ''
# liste = liste2(r)
# for i in liste:
#     prime += (str(i) + ' ')
# debut = time.perf_counter()
# liste_prime(r)
# liste2(r)
# fin = time.perf_counter()
# print(f"La liste des nombres premiers parmis les {r} premiers nombres a été trouvé en {fin - debut} secondes.")
# print(f"les nombres premiers de 0 a {r} sont : {prime}")
