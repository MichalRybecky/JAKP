import locale

def text_sorter(text):
    locale.setlocale(locale.LC_COLLATE, ('sk_SK', 'UTF8'))
    text1 = text.lower()
    words = text1.split(" ") 
    words.sort(key=locale.strxfrm)
    sorted = " ".join(words)
    return sorted

#line 2 a 3 sa asi da aj zjednotit ale neviem ako
# "input" text musi byt v stringu aby to fungovalo
# vie to sortovat aj slovenske znaky, som nasiel nejake 200iq "Locale"

#Na ukazku ako funguje
sentence1 = "my, mykať sa, mýliť sa, ômar, myslieť, myšlienka, myseľ, umývať sa, mydlo, myš, šmýkať sa, hmyz, žmýkať, priemysel, Myjava, mýto, mys, zamykať, pomykov, hmýriť sa, šmyk, priesmyk, omyl, zmysel, pomyje"
sentence2 = "A stable sort is one where the initial order of equal elements is preserved."
print(text_sorter(sentence1))
  

        
        


    
    
