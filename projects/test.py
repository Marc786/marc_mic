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





def pri():   
    print(etat_partie()['murs'])

def etat_partie():
    dico = {
        'joueurs':['x', 'y'],
        'murs': 6
    }
    return dico

pri()


        # def __str__(self):
        # """Représentation en art ascii de l'état actuel de la partie.

        # Cette représentation est la même que celle du projet précédent.

        # Returns:
        #     str: La chaîne de caractères de la représentation.
        # """
        # etat_partie = self.état_partie()
        # j1 = ''
        # j2 = ''
        # if len(etat_partie['joueurs'][0]['nom']) > len(etat_partie['joueurs'][1]['nom']):
        #     diff = len(etat_partie['joueurs'][0]['nom']) - len(etat_partie['joueurs'][1]['nom'])
        #     j2 = etat_partie['joueurs'][1]['nom'] + ', ' + (diff)*' '
        #     j1 = etat_partie['joueurs'][0]['nom'] + ', '
        # elif len(etat_partie['joueurs'][1]['nom']) > len(etat_partie['joueurs'][0]['nom']):
        #     diff = len(etat_partie['joueurs'][1]['nom']) - len(etat_partie['joueurs'][0]['nom'])
        #     j1 = etat_partie['joueurs'][0]['nom'] + ', ' + (diff)*' '
        #     j2 = etat_partie['joueurs'][1]['nom'] + ', '
        # else:
        #     j1 = etat_partie['joueurs'][0]['nom'] + ', '
        #     j2 = etat_partie['joueurs'][1]['nom'] + ', '
        # legende = [
        #     'Légende:',
        #     '   1='+j1+'murs='+etat_partie['joueurs'][0]['murs']*'|',
        #     '   2='+j2+'murs='+etat_partie['joueurs'][1]['murs']*'|'
        # ]
        
        # damier = [
        # ['--|'+35*'-'+'\n', '  | 1', '   2', '   3', '   4', '   5', '   6', '   7', '   8', '   9'],
        # ['1 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['2 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['3 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['4 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['5 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['6 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['7 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['8 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['  |','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ',' ','   ','|'],
        # ['9 | ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.','   ','.',' |'],
        # ['   '+35*'-']
        # ]

        # for i in range(len(etat_partie['murs']['horizontaux'])):
        #     x = 2*(etat_partie['murs']['horizontaux'][i][0] - 1)
        #     y = 2*(etat_partie['murs']['horizontaux'][i][1] - 1)
        #     damier[y][x+1] = '---'
        #     damier[y][x+2] = '-'
        #     damier[y][x+3] = '---'
        # for i in range(len(etat_partie['murs']['verticaux'])):
        #     x = 2*(etat_partie['murs']['verticaux'][i][0] - 1)
        #     y = 2*(etat_partie['murs']['verticaux'][i][1] - 1)
        #     damier[y+1][x] = ' | '
        #     damier[y+2][x] = '|'
        #     damier[y+3][x] = ' | '
        # for i in range(2):
        #     x = 2*etat_partie['joueurs'][i]['pos'][0] - 1
        #     y = 2*etat_partie['joueurs'][i]['pos'][1] - 1
        #     damier[y][x] = str(i+1)
        # for line in range(3):
        #     print(*legende[line], sep='')
        # for line in reversed(range(19)):
        #     print(*damier[line], sep='')
