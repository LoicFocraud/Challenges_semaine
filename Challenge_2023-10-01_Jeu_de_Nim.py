''' Enoncé du projet : Challenge du dimanche 01 octobre 2023
    Auteur : Loic_F (brian_basco)
    Date : 03 octobre 2023
    But du programme : Développer le jeu de Nim, chaque joueur prend entre 1 et 3 bâtonnets à son tour,
                        celui qui obtient le dernier à perdu.
'''

from random import randint

def IA(X0:int, X: int)-> int:
# Fonction permettant à l'ordi de gagner à tous les coups, avec 20 bâtons et s'il commence à jouer.
    if X0 == X or (X-3)%4 == 1 : # L'ordi est sûr de gagner en laissant 17, 13, 9 ou 5 bâtons au joueur
        return 3
    elif (X-1)%4 == 1:
        return 1
    elif (X-2)%4 == 1:
        return 2
    else:
        return randint(1, 3) # Au cas où on paramètre plus de 20 batons.

start = rest = 20 # Paramétrage du nb de bâtons
print(("# "*rest+"\n")*3)
while rest > 1:
    take = IA(start, rest)
    print(f"L'ordinateur prend {take} bâtons.\n")  
    rest -= take
    print(("# "*rest+"\n")*3)
    if rest == 1:
        print("Vous avez perdu !")
    else :   
        take = input("Combien en prenez-vous ? ")
        while take not in ("1", "2", "3"):
            take = input("Combien en prenez-vous ? ")  
        rest -= int(take)
        print(("# "*rest+"\n")*3)
        if rest == 1:
            print("Vous avez gagné !")   


