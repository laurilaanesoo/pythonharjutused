# Ülesanne 3
# Lauri Laanesoo
# 01.02.2022

#Palindroom



#Tundide ajad
aeg1 = input("Sisesta tundide algus: ")
aeg2 = input("Sisesta tundide lõpp: ")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2) * 60 +int(mm2)) - (int(hh1) * 60 +int(mm1))
tund = vastus//60
minut = vastus%60
print(f"{tund}:{minut}")


#Email
email = input("Sisesta oma email: ")
print("@" in email)


#Vandumine
sona = input("Sisesta sõna: ")
sona = sona.lower()
kurat= sona.replace("kurat","*****")
print(kurat)


#Nimi
nimi = input("Sisesta oma nimi: ")
nimi = nimi.strip().capitalize()
print("Tere,",nimi+"!")
