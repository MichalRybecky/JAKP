###Premeny mien

#Denný kurzový lístok ECB 
#valid: 11.4.2021


kurzy = {"usd": 1.1884, "jpy": 130.42, "bgn": 1.9558, "czk": 25.945, "dkk": 7.4372, "gbp": 0.86658, "huf": 357.97, "pln": 4.5392, "ron": 4.9198, "sek": 10.1725, "chf": 1.1010, "isk": 151.90, "nok": 10.1130, "hrk": 7.5755, "rub": 91.8152, "try": 9.6903, "aud": 1.5579, "brl": 6.6641, "cad": 1.4950, "cny": 7.7934, "hkd": 9.2470, "idr": 17354.52, "ils": 3.9093, "inr": 88.8145, "krw": 1331.28, "mxn": 23.9374, "myr": 4.9157, "nzd": 1.6860, "php": 57.764, "sgd": 1.5941, "thb": 37.388, "zar": 17.3100}
        
def from_eur(mena, hodnota):
   vysledok = round(kurzy[mena] * hodnota, 2)
   return vysledok


def from_xyz(mena, hodnota):
    vysledok = round(hodnota / kurzy[mena], 2)
    return vysledok

