#Ülesanne9
#17.02.2022
#Lauri Laanesoo

from dateutil.relativedelta import relativedelta
import datetime

kuud = ["jaanuar", "veebruar", "märts"]

#Tänane kuupäev
aeg = datetime.datetime.today()   
kuupaev = aeg.strftime("%d.%B.%Y")
kuupaeva = aeg.strftime("%d.%m.%Y") 
print("Tänane kuupäev on:", kuupaev)

#Eesti keelne kuupäev
kuupaevad = aeg.strftime('%d.%m.%Y')
d, m, Y = kuupaeva.split('.')
kuu = kuud[int(m)-1]
aeg2 = (d +"."+ kuu +"." + Y)

print(aeg2)

#Isikukood
isikukood = "505080501334"
aasta = int(isikukood[1]+isikukood[2])+2000
kuu = int(isikukood[3]+isikukood[4])
paev = int(isikukood[5]+isikukood[6])

kokku = datetime.datetime(aasta, kuu, paev)
ajad = datetime.datetime(int(aeg.strftime(" %Y")), int(aeg.strftime(" %m")), int(aeg.strftime(" %d")))

erinevus = relativedelta(ajad,kokku).years
print("Aasta vahe on: "+str(erinevus))


