#Ülesanne9
#17.02.2022
#Lauri Laanesoo


import datetime
kuud = ["jaanuar", "veebruar", "märts"]

aeg = datetime.datetime.today()   
kuupaev = aeg.strftime("%d.%B.%Y")
kuupaeva = aeg.strftime("%d.%m.%Y") 
print("Tänane kuupäev on:", kuupaev)

ajad = aeg.strftime("%d.")+kuud[int(aeg.strftime("%m"))-1]+" "+aeg.strftime("%Y")

print(ajad)




isikukood = "505080501334"
aasta = int("20"+isikukood[1]+isikukood[2])
kuu = int(isikukood[3]+isikukood[4])
paev = int(isikukood[5]+isikukood[6])

vanus = str(paev)+"."+str(kuu)+"."+str(aasta)
from dateutil.relativedelta import relativedelta

erinevus = relativedelta(kuupaeva,vanus)
print("Aasta vahe on: "+str(erinevus))
