''' Enoncé du projet : Challenge du dimanche 17 septembre 2023
    Auteur : Loic_F (brian_basco)
    Date : 24 septembre 2023
    But du programme : Développer un codeur/décodeur suivant la logique de cryptographie symétrique
                        qui utilise une clef numérique très simple pour chiffrer et déchiffrer.
'''

import re #pour reg ex match
from math import * #pour ceil arrondi supérieur

def coder(tocode:str, key:str)->str:
    tocode = tocode.replace(" ","_")
    line = ceil(len(tocode)/int(key)) # line = nb de lignes nécessaires pour le chiffrage
    tocode = tocode + "*"*(int(key)*line-len(tocode)) # complète l'input avec les *
    coded = [tocode[i+j] for i in range(int(key)) for j in range(0, len(tocode), int(key))] #chiffrage
    return(str(coded).replace("[", "").replace("]", "").replace("'", "").replace(", ", ""))

def decoder(todecode:str, key:str)-> str:
    line = ceil(len(todecode)/int(key))
    decoded = [todecode[i+j] for i in range(line) for j in range(0, len(todecode), line)] # déchiffrage
    decoded = str(decoded).replace("[", "").replace("]", "").replace("'", "").replace(", ", "")
    ast = re.match(r'(\**)', decoded[::-1]) # cherche les * à la fin
    return(decoded.split(ast.group())[0].replace("_"," "))

phrase = input("Phrase à chiffrer : ")
while len(phrase) <=1 :
    phrase = input("La phrase doit contenir plusieurs caractères.\nPhrase à chiffrer : ")
cle = input("Clé de chiffrement : ")
while not cle.isdigit() or int(cle) > len(phrase) or int(cle) <=1 :
    cle = input("La clé doit être :\n - un nombre\n - supérieure à 1\n - plus petite que le nombre de caractères de la phrase à chiffrer.\nClé de chiffrement : ")
print(coder(phrase, cle))
code = input("Phrase à déchiffrer : ")
print(decoder(code, cle))






