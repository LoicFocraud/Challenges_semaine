import re

texte = """Récemment, j'ai eu l'opportunité de rencontrer des entrepreneurs exceptionnels lors d'une conférence. Par exemple, j'ai été inspiré par l'histoire de M. Thomas Bernard, qui a démarré sa propre entreprise dans la Silicon Valley. Vous pouvez le contacter à l'adresse email thomas.b@alphamail.com ou au numéro suivant +33 1 12 34 56 78. Une autre personne fascinante était Mme Claire Martin, la fondatrice d'une startup technologique innovante. Elle est joignable à cmartin@betainbox.org, son numéro de téléphone est le 09 01 23 45 67. Ensuite, il y avait monsieur Lucas Petit, un innovateur dans le domaine de la construction durable, contactable à lp@experimentalpost.net, son téléphone est le 0890 12 34 56.

En parcourant mon ancien annuaire, je suis tombé sur quelques contacts intéressants. Par exemple, j'ai redécouvert le contact de Mlle Sophie Martin. Son numéro de téléphone est 07 89 01 23 45, et elle est facilement joignable à l'adresse sophie@prototypemail.com. Un autre contact noté était celui du Dr Lucas Dupont. Je me souviens avoir eu plusieurs discussions avec lui. Son numéro est 06 78 90 12 34 et son mail est drdupont@randominbox.org. C'est fascinant de voir comment certains contacts peuvent rapidement nous rappeler des souvenirs passés.

Lors de notre dernière réunion, Madame Jennifer Laroche, joignable au 05.67.890.123 ou par e-mail à laroche@trialmail.net, a exprimé sa satisfaction concernant les avancées du projet. Elle a insisté sur la pertinence du feedback fourni par M. Sébastien Girard, qui peut être contacté au 0456789012 ou par email à sebastieng@demomail.org. De plus, notre consultante externe, mademoiselle Chloé Lefebvre, dont le numéro est le 03.45.67.89.01 et l'e-mail est lefebvre_chloe@testinbox.net, a fourni un rapport détaillé qui a été bien reçu par l'équipe."
"""

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







