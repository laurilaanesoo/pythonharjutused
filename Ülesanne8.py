#Ülesanne 8
#Lauri Laanesoo
#16.02.2022

class auto:
    automark = 0
    aasta = 0
    hind = 0
    kiirus = 0
    varv = 0
    
    def lisaaasta(self,x):
        self.aasta = x
    
    def lisahind(self,x):
        self.hind = x
    
    def lisamark(self,x):
        self.mark = x
    
    def varv(self,x):
        self.varv = x
    
    def kiirus(self,x):
        self.kiirus = x
    
    def kuva(self):
        print(f"{self.mark} {self.aasta} {self.hind} {self.kiirus} {self.varv}")


uusobjekt = auto()
uusobjekt.lisamark("Reliant Robin")
uusobjekt.lisaaasta("1973")
uusobjekt.lisahind("5000€")
uusobjekt.varv("pruun")
uusobjekt.kiirus("80km/h")
uusobjekt.kuva()

uus = auto()
uus.lisamark("Reliant kitten")
uus.lisaaasta("2022")
uus.lisahind("20€")
uus.varv("pruun")
uus.kiirus("50km/h")
uus.kuva()