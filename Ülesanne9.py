#Ülesanne9
#17.02.2022
#Lauri Laanesoo


import datetime
kuud = ["jaanuar, veebruar, märts"]

kuup = datetime.datetime.today()   
kuupaev = aeg.strftime("%d.%m.%Y") 
print("Tänane kuupäev on:", kuupaev)

kuu = int(kuup.month)
kuup2 = datetime.date(kuup2.year, 1, kuup2.day)
print(kuup.strftime("%d.+""str([kuu-1]).%Y"))



isikukood = "505080501334"
aasta = int("20"+isikukood[1]+isikukood[2])
kuu = int(isikukood[3]+isikukood[4])
paev = int(isikukood[5]+isikukood[6])
kuup = datetime.date(aasta, kuu, paev)
print(kuup)

from dateutil.relativedelta import relativedelta

aeg = datetime.datetime(kuup)
praegu = datetime.datetime.now()

erinevus = relativedelta(praegu,aeg)
print("Aasta vahe on: "+str(erinevus.years))