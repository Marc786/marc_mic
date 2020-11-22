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


joueurs = ['joueur1', {'nom': 'x', 'murs': 10, 'pos': (1, 2)}]
etat_de_jeu = {
            'joueurs': [
                #{'nom': self.joueurs[0]['nom'], 'murs': self.joueurs[0]['murs'], 'pos': self.joueurs[0]['pos']},
                #{'nom': self.joueurs[1]['nom'], 'murs': self.joueurs[1]['murs'], 'pos': self.joueurs[1]['pos']}
            ],
            'murs': {
                'horizontaux':[],
                'verticaux':[]
            }
}
murs = {
    "joueurs": 'allo',
    "murs":{
        'horizontaux':[[1, 2], [3, 4], [5, 6]],
        'verticaux':[]
    }
}
for murs in murs['murs']['horizontaux']:
    etat_de_jeu['murs']['horizontaux'].append(murs)
print(etat_de_jeu)





# etat_de_jeu = {
#             'joueurs': [
#                 {'nom': self.joueurs[0]['nom'], 'murs': self.joueurs[0]['murs'], 'pos': self.joueurs[0]['pos']},
#                 {'nom': self.joueurs[1]['nom'], 'murs': self.joueurs[1]['murs'], 'pos': self.joueurs[1]['pos']}
#             ],
#             'murs': {
#                 'horizontaux':[],
#                 'verticaux':[]
#             }
#         }
#         for murs in self.murs['horizontaux']:
#             etat_de_jeu['murs']['horizontaux'].append(murs)
#         for murs in self.murs['verticaux']:
#             etat_de_jeu['murs']['verticaux'].append(murs)
# return etat_de_jeu

