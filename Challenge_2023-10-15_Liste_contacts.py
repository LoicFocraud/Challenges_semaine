import re

texte = """Récemment, j'ai eu l'opportunité de rencontrer des entrepreneurs exceptionnels lors d'une conférence. Par exemple, j'ai été inspiré par l'histoire de M. Thomas Bernard, qui a démarré sa propre entreprise dans la Silicon Valley. Vous pouvez le contacter à l'adresse email thomas.b@alphamail.com ou au numéro suivant +33 1 12 34 56 78. Une autre personne fascinante était Mme Claire Martin, la fondatrice d'une startup technologique innovante. Elle est joignable à cmartin@betainbox.org, son numéro de téléphone est le 09 01 23 45 67. Ensuite, il y avait monsieur Lucas Petit, un innovateur dans le domaine de la construction durable, contactable à lp@experimentalpost.net, son téléphone est le 0890 12 34 56.

En parcourant mon ancien annuaire, je suis tombé sur quelques contacts intéressants. Par exemple, j'ai redécouvert le contact de Mlle Sophie Martin. Son numéro de téléphone est 07 89 01 23 45, et elle est facilement joignable à l'adresse sophie@prototypemail.com. Un autre contact noté était celui du Dr Lucas Dupont. Je me souviens avoir eu plusieurs discussions avec lui. Son numéro est 06 78 90 12 34 et son mail est drdupont@randominbox.org. C'est fascinant de voir comment certains contacts peuvent rapidement nous rappeler des souvenirs passés.

Lors de notre dernière réunion, Madame Jennifer Laroche, joignable au 05.67.890.123 ou par e-mail à laroche@trialmail.net, a exprimé sa satisfaction concernant les avancées du projet. Elle a insisté sur la pertinence du feedback fourni par M. Sébastien Girard, qui peut être contacté au 0456789012 ou par email à sebastieng@demomail.org. De plus, notre consultante externe, mademoiselle Chloé Lefebvre, dont le numéro est le 03.45.67.89.01 et l'e-mail est lefebvre_chloe@testinbox.net, a fourni un rapport détaillé qui a été bien reçu par l'équipe."
"""

dict = {"prenom_nom": [], "telephone": [], "email": []} 
firstname_name = phone = mail = "start"

while firstname_name : #Recherche des Prénoms - Noms
    firstname_name = re.search(r'(M.|Mme|Mlle|Dr|Monsieur|Madame|Mademoiselle|Docteur|monsieur|madame|mademoiselle|docteur)\s(\w+)\s(\w+)', texte)   
    if firstname_name:       
        texte = texte.replace(firstname_name.group(), "")
        prenom_nom = firstname_name.group()[firstname_name.group().find(" ")+1:]
        dict["prenom_nom"].append(prenom_nom)

while mail : #Recherche des e-mails
    mail = re.search(r'((\w+)|((\w+)(\.)(\w+)))@(\w+)(\.)(com|org|fr|net)', texte)
    if mail:      
        texte = texte.replace(mail.group(), "")
        dict["email"].append(mail.group())

texte = texte.replace(" ","").replace(".","").replace("+","") # Désolé pour la méthode de bourrin, je n'ai pas trouvé
                                                              # la Regex qui permettait d'isoler le n° de téléphone
while phone : #Recherche des téléphones
    phone = re.search(r'(33|0)([0-9]{9})', texte)
    if phone:      
        texte = texte.replace(phone.group(), "")
        if len((phone.group()))==11:
            tel = phone.group()[0:2]+"."+phone.group()[2]+"."+phone.group()[3:5]+"."+phone.group()[5:7]+"."+phone.group()[7:9]+"."+phone.group()[9:11]
        else:
            tel = phone.group()[0:2]+"."+phone.group()[2:4]+"."+phone.group()[4:6]+"."+phone.group()[6:8]+"."+phone.group()[8:10]
        dict["telephone"].append(tel)
        
name_larg = max(max([len(elem)+2 for elem in dict["prenom_nom"]]),14) #largeur de la colonne Nom & Prénom   
mail_larg = max(max([len(elem)+2 for elem in dict["email"]]),6)       #largeur de la colonne Mail 
phone_larg = max(max([len(elem)+2 for elem in dict["telephone"]]),8)  #largeur de la colonne Numéro   

esp1, esp2, esp3 = round((name_larg-12)/2), round((mail_larg-4)/2), round((phone_larg-6)/2) # Calcul des espacements

# Affichage
print("|"+" "*esp1+"Nom & Prénom"+" "*(name_larg-esp1-12)+"|"+" "*esp2+"Mail"+" "*(mail_larg-esp2-4)+"|"+" "*esp3+"Numéro"+" "*(phone_larg-esp3-6)+"|")
print("|"+"-"*(name_larg)+"|"+"-"*(mail_larg)+"|"+"-"*(phone_larg)+"|")
for i in range(len(dict["prenom_nom"])):
    print("|"+" "+dict["prenom_nom"][i]+" "*(name_larg-1-(len(dict["prenom_nom"][i])))+"|"+" "+dict["email"][i]+" "*(mail_larg-1-(len(dict["email"][i])))+"|"+" "+dict["telephone"][i]+" "*(phone_larg-1-(len(dict["telephone"][i])))+"|")  
print("|"+"-"*(name_larg)+"|"+"-"*(mail_larg)+"|"+"-"*(phone_larg)+"|")




