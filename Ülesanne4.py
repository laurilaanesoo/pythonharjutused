# Ülesanne 4
# Lauri Laanesoo
# 03.02.2022

#Tärnid
#for i in range(1,6):
#    for j in range(1,6):
#        print("* ",end="")
#    print()

for l in range(0,5):
    a=a+1
    for k in range (0,a):
       
        print("* ",end="")
    print()

#Jalgpalli meeskond
sugu = input("Sisesta oma sugu: ")
if sugu == "m":
    vanus = int(input("Sisesta oma vanus: "))
    if vanus >= 16 and vanus <= 18:
         print("Said jalgpalli meeskonda")
    else:
         print("Ei saanud jalgpalli meeskonda")
else:
    print("Ei saanud jalgpalli meeskonda")



#Müük
hind= int(input("Sisesta toote hind: "))
if hind > 10:
    allahindlus = hind * 0.2
else:
    allahindlus = hind * 0.1
print(hind-allahindlus)


#Juubel
aasta = input("Sisesta sünniaeg kujul dd.mm.yyyy: ")
a,b,c = aasta.split(".")
aasta = 2022 - int(c)
if aasta%5==0:
    print("Sul on juubel")
else:
    print("Sul ei ole juubel")


#Matemaatika
a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
c = input("Millist tehet tahad teha? (+ - * /")
if c=="+":
    d= a + b
elif c=="-":
    d= a - b
elif c=="*":
    d= a * b
else:
    d= a / b
print(f"{a}{c}{b}={d}")


#Ruut
a = int(input("Sisesta ruudu esimene külg: "))
b = int(input("Sisesta ruudu teine külg: "))

if a==b:
    print("Kujund on ruut")
else:
    print("Kujund ei ole ruut")