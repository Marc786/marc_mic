# grille = {
#                 'joueurs': [
#                     {'nom': 'x', 'murs': '1', 'pos': (1, 2)},
#                     {'nom': 'y', 'murs': '2', 'pos': (2, 1)},
#                 ],
#                 'murs': {
#                     'horizontaux': [...],
#                     'verticaux': [...],
#                 }
# }

# print(len(grille['joueurs']))


# # joueurs = ['joueur1', {'nom': 'x', 'murs': 10, 'pos': (1, 2)}]
# etat_de_jeu = {
#             'joueurs': [
#                 #{'nom': self.joueurs[0]['nom'], 'murs': self.joueurs[0]['murs'], 'pos': self.joueurs[0]['pos']},
#                 #{'nom': self.joueurs[1]['nom'], 'murs': self.joueurs[1]['murs'], 'pos': self.joueurs[1]['pos']}
#             ],
#             'murs': {
#                 'horizontaux':[],
#                 'verticaux':[]
#             }
# }
# murs = {
#     "joueurs": 'allo',
#     "murs":{
#         'horizontaux':[[1, 2], [3, 4], [5, 6]],
#         'verticaux':[]
#     }
# }
# for murs in murs['murs']['horizontaux']:
#     etat_de_jeu['murs']['horizontaux'].append(murs)
# print(etat_de_jeu)





# def pri():   
#     print(etat_partie()['murs'])
#     return 7
# def etat_partie():
#     dico = {
#         'joueurs':['x', 'y'],
#         'murs': 6
#     }
#     return dico

# pri()

# murs = {
#     'horizontaux': [],
#     'verticaux': []
# }

# joueurs = [
#     {'nom': 'joueurs1',  'murs': 6, 'pos':['x','y']},
#     {'nom': 'joueurs2',  'murs': 6, 'pos':['x','y']}
# ]

# import random

# for i in range(9):
#     print(random.randint(0,3))

# liste = [1,2]
# print(len(liste))
# liste = []
# for i in range(9):
#     liste.append(i)
# print(liste)

# def func1(n, y, z):
#     return (100+n, 200+y, 300+z)

# x = func1(5, 6, 7)
# print(x)
n = 100
liste = []
liste1= []
liste2 = []
liste3 = []
for i in range(1, n+1):
    if i%2==0:
        liste.append(i)
    elif i%2 == 1:
        liste1.append(i)
    if i%4==0:
        liste2.append(i)
    elif i%4==1 or i%4==2 or i%4==3:
        liste3.append(i)
print(liste)
print(liste1)
print(liste2)
print(liste3)