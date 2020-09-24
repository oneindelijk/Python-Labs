import time
from random import randint
from datetime import timedelta

class Tamagotchi:
  
    def __init__(self, name):
        self.name = name 
        self.kleur = self.kieskleur()
        
    def kieskleur (self):
        Kleuren = ["rood","groen","bruin"]
        GekozenKleur = Kleuren[randint(0,2)]
        return GekozenKleur

    def geboorte (self):
        '''de hond wordt geboren en krijgt een geboortedatum.  
        De gebruiker krijgt de mogelijkheid om een naam te kiezen'''
        self.geboortedatum = time.time()

    def wakeup (self):
        print(f"{self.name} is geboren")

    def leeftijd (self):
        leeftijd = time.time() - self.geboortedatum
        return leeftijd
    
    def hondenjaren (self):
        hondenjaren = (time.time() - self.geboortedatum) * 7
        return hondenjaren

    def info (self):
        infoleeftijd = timedelta(seconds = self.leeftijd())
        infoleeftijdhondenjaren = timedelta(seconds = self.hondenjaren())
        print("{} is {} seconden oud".format(self.name, infoleeftijd.seconds))
        print("maar voor {} voelt dit als {} seconden oud".format(self.name, infoleeftijdhondenjaren.seconds))
        
print("Hoe wil jij jou tamagotchi noemen ? ")
Tamaname = input()
hond = Tamagotchi(Tamaname)
hond.geboorte()
hond.wakeup()
hond.info()
'''
hondjaren
geboorte functie uitbreiden, merk en zo
soort en kleur random
een beetje denken over de spelregels. 
random()
'''