''' Enoncé du projet : Challenge du dimanche 17 septembre 2023
    Auteur : Loic_F (brian_basco)
    Date : 17 septembre 2023
    But du programme : Développer un script qui permet d'afficher l'heure dans un format digital. Chaque chiffre est composé
    de 7 segments.
'''

from datetime import datetime

def digital(chiffre:str)->dict:
    # Fonction permettant de convertir un chiffre arabe (format str) en son format digital (dictionnaire des segments)
    digi ={"a, d, g": ["   #", "####", "#  #"], "b, c, e, f": [" ", "#"]} # "coloriage possible des 7 segments a à g)

    if chiffre == 0:
        a = d = digi["a, d, g"][1]
        b = c = e = f = digi["b, c, e, f"][1]   
        g = digi["a, d, g"][2]
        
    elif chiffre == 1:
        a = d = g = digi["a, d, g"][0]
        b = c = digi["b, c, e, f"][1]   
        e = f = digi["b, c, e, f"][0]

    elif chiffre == 2: 
        a = d = g = digi["a, d, g"][1]
        b = e = digi["b, c, e, f"][1]
        c = f = digi["b, c, e, f"][0]
    
    elif chiffre == 3 :
        a = d = g = digi["a, d, g"][1]
        b = c = digi["b, c, e, f"][1]
        e = f = digi["b, c, e, f"][0]
    
    elif chiffre == 4 :
        a = digi["a, d, g"][2]
        b = c = f = digi["b, c, e, f"][1]
        d = digi["a, d, g"][0]    
        e = digi["b, c, e, f"][0]
        g = digi["a, d, g"][1]

    elif chiffre == 5 :
        a = d = g = digi["a, d, g"][1]
        b = e = digi["b, c, e, f"][0]
        c = f = digi["b, c, e, f"][1] 
    
    elif chiffre == 6 :
        a = d = g = digi["a, d, g"][1]
        b = digi["b, c, e, f"][0]
        c = e = f = digi["b, c, e, f"][1]    

    elif chiffre == 7 :
        a = digi["a, d, g"][1]
        b = c = digi["b, c, e, f"][1]
        e = f = digi["b, c, e, f"][0]  
        d = g = digi["a, d, g"][0]
    
    elif chiffre == 8 :
        a = d = g = digi["a, d, g"][1]
        b = c = e = f = digi["b, c, e, f"][1]  

    elif chiffre == 9 :
        a = d = g = digi["a, d, g"][1]
        b = c = f = digi["b, c, e, f"][1]
        e = digi["b, c, e, f"][0]
    
    digit = {"a" : a, "b" : b, "c" : c, "d" : d , "e" : e, "f" : f, "g" : g}
    return digit

def digital_time(heure: str, minute: str)->str:
    # Fonction permettant de convertir l'heure (4 chiffres au format str) en format digital
    digit_1 = digital(int(heure[0]))
    digit_2 = digital(int(heure[1]))
    digit_3 = digital(int(minute[0]))
    digit_4 = digital(int(minute[1]))
    # Affichage des 5 lignes :
    L1 = digit_1["a"]+" "+digit_2["a"]+"   "+digit_3["a"]+" "+digit_4["a"]
    L2 = digit_1["f"]+"  "+digit_1["b"]+" "+digit_2["f"]+"  "+digit_2["b"]+" # "+digit_3["f"]+"  "+digit_3["b"]+" "+digit_4["f"]+"  "+digit_4["b"]
    L3 = digit_1["g"]+" "+digit_2["g"]+"   "+digit_3["g"]+" "+digit_4["g"]
    L4 = digit_1["e"]+"  "+digit_1["c"]+" "+digit_2["e"]+"  "+digit_2["c"]+" # "+digit_3["e"]+"  "+digit_3["c"]+" "+digit_4["e"]+"  "+digit_4["c"]
    L5 = digit_1["d"]+" "+digit_2["d"]+"   "+digit_3["d"]+" "+digit_4["d"]

    heure_digital = L1+"\n"+L2+"\n"+L3+"\n"+L4+"\n"+L5
    return heure_digital

now = datetime.now()
heure = f"{now.hour:02d}"
minute = f"{now.minute:02d}"
heure_digital = digital_time(heure, minute)
print(heure_digital)

