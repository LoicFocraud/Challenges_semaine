''' Enoncé du projet : Challenge du dimanche 27 août 2023
    Auteur : Loic_F (brian_basco)
    Date : 30 août 2023
    But du programme : Trouver la couleur complémentaire. Une fonction get_color_types() qui permet de convertir
    le format RVB hexadécimal d’une couleur aux formats RVB décimal et TSL. Une fonction get_complementary() pour
    trouver la couleur complémentaire et qui retourne la couleur au format hexadécimal.
'''

import colorsys

def check_entry(hex):
    '''Fonction permettant de valider le format input RVB hexadécimal'''
    if hex[0] == "#" and len(hex) == 7:
        for i in range(1, 7) :
            if hex[i].isalnum():
                return True
    return False

def hex_to_rvb(hex):
    '''Fonction permettant de convertir de RVB hexadécimal en RVB décimal
    J'ai trouvé la formule sur la page
    https://www.adobe.com/fr/creativecloud/design/discover/color-hex-codes.html'''
    hex = hex.replace('#', '')
    rvb_list = []
    for i in range(6):
        if hex[i] in ["a", "b", "c", "d", "e", "f"]:
            j = ord(hex[i])-87 #transforme les lettres de a à f en valeur
        else:
            j = int(hex[i])
        rvb_list.append(j)
    r = rvb_list[0]*16 + rvb_list[1]
    v = rvb_list[2]*16 + rvb_list[3]
    b = rvb_list[4]*16 + rvb_list[5]
    rvb = [r, v, b]
    return rvb
            
def rvb_to_hex(rvb):
    '''Fonction permettant de convertir de RVB décimal en RVB hexadécimal'''
    hex = "#"
    r = int(rvb[0]/16)
    rr = rvb[0]%16
    v = int(rvb[1]/16)
    vr = rvb[1]%16
    b = int(rvb[2]/16)
    br = rvb[2]%16
    for i in [r, rr, v, vr, b, br]:
        if i >= 10:
            i = chr(i+87) #si i >=10 transforme en lettres de a à f
        hex = hex + str(i)
    return hex

def rvb_to_tsl(rvb):
    '''Fonction permettant de convertir de RVB décimal en TSL'''
    r=rvb[0]/255 #plage de 255 couleur
    v=rvb[1]/255
    b=rvb[2]/255
    hls = colorsys.rgb_to_hls(r, v, b)
    tsl = hls[0], hls[2], hls[1]
    return tsl

def tsl_to_rvb(tsl):
    '''Fonction permettant de convertir de TSL en RVB décimal'''
    h=tsl[0]
    l=tsl[2]
    s=tsl[1]
    rvb = colorsys.hls_to_rgb(h, l, s)
    rvb = round(rvb[0]*255), round(rvb[1]*255), round(rvb[2]*255)
    return rvb

def tsl_to_tsl_norm(tsl):
    '''Fonction permettant de convertir de TSL en TSL normé
    (teinte en degrés 360°, saturation en % et luminosité en %)'''
    t = str(round(tsl[0]*360))+"°"
    s = str(round(tsl[1]*100))+"%"
    l = str(round(tsl[2]*100))+"%"
    tsl_norm = t, s, l
    return tsl_norm


def get_color_types(hex):
    '''Fonction finale Input RVB_hexa => RVB => TSL => TSL_norm.
    Retourne le dictionnaire.'''
    rvb = hex_to_rvb(hex)
    tsl = rvb_to_tsl(rvb)
    tsl_norm = tsl_to_tsl_norm(tsl)   
    color_types = {'hex': str(hex), 'rvb': rvb, 'tsl_norm': tsl_norm, 'tsl': tsl}
    return color_types

def mirror_tsl(tsl):
    '''Fonction permettant de trouver la couleur complémentaire. "mirroir" du TSL.
    Utilisation de TSL plutôt que TLS_norm car plus précis'''
    t = tsl[0]
    if t >=0.5:
        t -= 0.5
    else:
        t += 0.5
    s= tsl[1]
    l= tsl[2]
    tsl = t, s, l 
    return tsl

def get_complementary(hex):
    '''Fonction finale qui retourne le RVB_hexa de la couleur complémentaire.
    RVB couleur initiale => TSL couleur initiale => TSL couleur complémentaire
    => RVB couleur complémentaire'''
    rvb = hex_to_rvb(hex)
    tsl = rvb_to_tsl(rvb)
    tsl_mirror = mirror_tsl(tsl)
    rvb = tsl_to_rvb(tsl_mirror)
    complementary = rvb_to_hex(rvb)
    return complementary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

hex = input("RVB hexadecimal ?").lower()
while not check_entry(hex):
    hex = input("RVB hexadecimal ?").lower()

color_types = get_color_types(hex)
complementary = get_complementary(hex)
print(color_types)
print(complementary)