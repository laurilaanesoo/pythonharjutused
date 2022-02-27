#Ülesanne5
#27.02.2022
#Lauri Laanesoo


#Tärnid
import random
arv = []
for h in range(10):
    arv.append(random.randint(1,20))
   
for d in range(len(arv)):
    print("*" * arv[d])


#Vanused
arvud = []
vanused = [8,23,96,32,75]
print()
print(f"Suurim arv: {max(vanused)} \nVäikseim arv {min(vanused)} Keskmine: {sum(vanused)/len(vanused)} Kokku: {sum(vanused)}")


#Duplikaadid
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
puh_opilased = []
for i in range(len(opilased)):
    if opilased[i] not in puh_opilased:
        puh_opilased.append(opilased[i])


for i in range(len(puh_opilased)):
    print(puh_opilased[i],end=", ")

#Õpilased

opilased = ['Juhan','Kati','Maarja','Mario','Mati']

print("Vali number, mida soovid muuta: ")


for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
valik = int(input("Sisesta number: "))
del opilased[valik-1]
uusnimi = input("Sisesta uus nimi: ")
opilased.insert(valik-1,uusnimi)
print("Nimi on muudetud")
print(opilased)


#Nimede lisamine loendisse

nimed=[] 
for i in range(5):
    nimi = input("Sisesta 5 nime: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
