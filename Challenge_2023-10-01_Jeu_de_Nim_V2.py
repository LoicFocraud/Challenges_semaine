''' Enoncé du projet : Challenge du dimanche 01 octobre 2023
    Auteur : Loic_F (brian_basco)
    Date : 07 octobre 2023
    But du programme : Développer le jeu de Nim, chaque joueur prend entre 1 et 3 bâtonnets à son tour,
                        celui qui obtient le dernier à perdu.
'''

from random import randint

def IA(X: int)-> int:
# Fonction permettant à l'ordi de gagner à tous les coups, avec 20 bâtons et s'il commence à jouer.
    return (X-1)%4

rest = 20 # Paramétrage du nb de bâtons
print(("# "*rest+"\n")*3)
while rest > 1:
    take = IA(rest)
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



