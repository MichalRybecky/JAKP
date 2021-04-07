###Premeny mien

#Denný kurzový lístok ECB 
#valid: 7.4.2021



## eur to xyz ##
def eur_to_usd(eur):
    return round(eur * 1.1884, 2)

def eur_to_gbp(eur):
    return round(eur * 0.86065, 2)

def eur_to_czk(eur):
    return round(eur * 25.919, 2)

#Madare
def eur_to_huf(eur):
    return round(eur * 359.68, 2)

#Polska
def eur_to_pln(eur):
    return round(eur * 4.5756, 2)

#Hrvatska
def eur_to_hrk(eur):
    return round(eur * 7.5763, 2)

#Cinani
def eur_to_cny(eur):
    return round(eur * 7.7761, 2)

#Russia
def eur_to_rub(eur):
    return round(eur * 92.3359, 2)



## xyz to eur ##
def usd_to_eur(usd):
    return round(usd / 1.1884, 2)

def gbp_to_eur(gpb):
    return round(gpb / 0.86065, 2)

def czk_to_eur(czk):
    return round(gpb / 25.919, 2)

#Madare
def huf_to_eur(huf):
    return round(huf / 359.68, 2)

#Polska
def pln_to_eur(pln):
    return round(pln / 4.5756, 2)

#Hrvatska
def hrk_to_eur(hrk):
    return round(hrk / 7.5763, 2)

#Cinani
def cny_to_eur(cny):
    return round(cny / 7.7761, 2)

#Russia
def rub_to_eur(rub):
    return round(rub / 92.3359, 2)


# len na vyskusanie
#print(rub_to_eur(156), eur_to_czk(156), pln_to_eur(156), eur_to_hrk(156))