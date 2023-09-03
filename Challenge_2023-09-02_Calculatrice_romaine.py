''' Enoncé du projet : Challenge du dimanche 03 septembre 2023
    Auteur : Loic_F (brian_basco)
    Date : 03 septembre 2023
    But du programme : Développer un script qui permet de calculer la somme de deux ou plusieurs nombres
    écrits en chiffres romains. => La calculette de nos rêves :-D
'''

def check_number(number:str)->bool:
    '''Fonction permettant de vérifier le respect des consignes :
    - Les chiffres romains sont : IVXLCDM, en majuscules
    - I, X et C ne peuvent pas être répétés plus de trois fois
    - V, L et D ne peuvent pas apparaître plus d'une fois'''
    Caract = {"I": 0, "V": 0, "X": 0, "L": 0, "C": 0, "D": 0, "M": 0}
    for car in number:    
        if car in Caract.keys():    
            Caract[car] += 1
        else:
            return False
    if (Caract["I"] > 3 or Caract["X"] > 3 or Caract["C"] > 3 or
        Caract["V"] > 1 or Caract["L"] > 1 or Caract["D"] > 1):
        return False
    return True

def check_operation(calculate:str)->bool:
    '''Fonction permettant de vérifier le respect des consignes :
    - Chaque nombre dans l'opération est au bon format (fonction check_number)
    - Seules les additions sont acceptées'''
    for car in calculate:
        if car not in ["I", "V", "X", "L", "C", "D", "M", "+"]:
            return False
    if "+" not in calculate: # N'accepte pas s'il n'y a qu'un nombre en entrée
        return False
    operation = calculate.split("+")
    for number in operation:
        if not check_number(number):
            return False
    return True

def conv_rom_ara(rom:str)->int:
    '''Fonction permettant de convertir les nombres en chiffres romains "rom"
    en nombres en chiffres arabes "ara" '''      
    conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ara = prio = 0
    for chiffre in rom[::-1]: #Les nombres romains, c'est comme les mangas,
        if conv[chiffre] >= prio: # on les lit de droite à gauche :-)
            ara += conv[chiffre]
        else :  
            ara -= conv[chiffre]
        prio = conv[chiffre]
    return ara

def conv_ara_rom(ara:int)->str:
    '''Fonction permettant de convertir les nombres en chiffres arabes "ara"
    nombres en chiffres romains "rom" '''      
    conv2 ={'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    rom = ""
    for key in conv2.keys():
        div = ara//conv2[key]
        rom = rom + div*key
        ara -= div*conv2[key]
    return rom

def add_romans(calculate:str)->str:
    '''Fonction permettant de calculer la somme
     de deux ou plusieurs nombres écrits en chiffres romains.''' 
    operation = calculate.split("+")
    resultat = 0
    for number in operation:
        resultat += conv_rom_ara(number)
    if resultat > 3999:
        return "erreur (débordement, doit respecter la plage de I à MMMCMXCIX inclus)"
    resultat = conv_ara_rom(resultat)
    return resultat

calculate = input("Ecrivez l'opération en chiffres romains :").replace(" ", "")
while not check_operation(calculate):
    calculate = input("Erreur de format. Ecrivez l'opération en chiffres romains :").replace(" ", "")
print(add_romans(calculate))