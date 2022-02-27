re, kesk, kokku = 0, 0, 0
erakonnad = []

with open('s6pru_l6ustaraamatus.txt','r') as sobrad:
    for rida in sobrad:
         enimi, vnimi, er, arv = rida.split(" ")
         print(f"{rida[0]:11} {rida[1]:11}", file=open("nimed", "a"))
         print(f"{enimi:11}{vnimi:11}{er:4}{arv:5}",end="")
         if er=="RE":
            re= re + 1
         elif er=="KE":
            kesk= kesk + 1
         if er not in erakonnad:
            erakonnad.append(erakonnad)
             
    print(f"Reformikad: {re}\nKesikuid: {kesk}\n")
    print(f"Erakondi kokku: {len(erakonnad)}")
