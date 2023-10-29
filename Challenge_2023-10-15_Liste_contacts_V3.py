''' Enoncé du projet : Challenge du dimanche 15 octobre 2023
    Auteur : Loic_F (brian_basco)
    Date : 18 octobre 2023
    But du programme : Script permettant d'extraire les noms, prénoms, téléphones et emails à partir d'un paragraphe,
puis de créer une base de données afin de les afficher clairement à l'écran.
'''

import re

with open("text.txt", encoding = "utf-8") as fichier:
    texte = str([elem for elem in fichier])

dico = {"prenom_nom": [], "telephone": [], "email": []} 

#Recherche des Prénoms Noms :
names = re.findall(r'(M.|Mme|Mlle|Dr|Monsieur|Madame|Mademoiselle|Docteur|monsieur|madame|mademoiselle|docteur)((\s(\w+)){2})', texte)   
[dico["prenom_nom"].append(elem[1]) for elem in names]

#Recherche des e-mails
mail = re.findall(r'(((\w+)|((\w+)(\.)(\w+)))@(\w+)(\.)(\w){3})', texte)  
[dico["email"].append(elem[0]) for elem in mail]

#Recherche des téléphones
phone = re.findall(r'((33|0)(\.| |\d)+(\D))', texte)
for elem in phone:
    tel = re.sub('\D+', '', [elem][0][0])
    tel = '{}{}.{}.{}{}.{}{}.{}{}.{}{}'.format(*tel) if len(tel) == 11 else '{}{}.{}{}.{}{}.{}{}.{}{}'.format(*tel)
    dico["telephone"].append(tel)   
        
name_larg = len(max(dico["prenom_nom"], key = len)) #largeur de la colonne Nom & Prénom   
mail_larg = len(max(dico["email"], key = len))       #largeur de la colonne Mail 
phone_larg = len(max(dico["telephone"], key = len))  #largeur de la colonne Numéro   

# Affichage
print(f'| {"Nom & Prénom" : ^{name_larg}} | {"Mail" : ^{mail_larg}} | {"Numéro" : ^{phone_larg}} |')
print(f'|-{"-"*name_larg}-|-{"-"*mail_larg}-|-{"-"*phone_larg}-|')
for i in range(len(dico["prenom_nom"])):
    print(f'| {dico["prenom_nom"][i] : <{name_larg}} | {dico["email"][i] : <{mail_larg}} | {dico["telephone"][i] : <{phone_larg}} |')
print(f'|-{"-"*name_larg}-|-{"-"*mail_larg}-|-{"-"*phone_larg}-|')







