import time
from datetime import timedelta

class Tamagotchi:
  
    def __init__(self):
        pass

    def wakeup (self):
        self.name = "test"
        print("Waarde van self:")

    def geboorte (self, naam):
        '''de hond wordt geboren en krijgt een geboortedatum.  
        De gebruiker krijgt de mogelijkheid om een naam te kiezen'''
        self.naam = naam
        self.geboortedatum = time.time()

    def leeftijd (self):
        leeftijd = time.time() - self.geboortedatum
        return leeftijd
    
    def hondenjaren (self):
        hondenjaren = (time.time() - self.geboortedatum) / 7
        return hondenjaren

    def info (self):
        infoleeftijd = timedelta(seconds = self.leeftijd())
        infoleeftijdhondenjaren = timedelta(seconds = self.hondenjaren())
        print("{} is {} seconden oud".format(self.naam, infoleeftijd.seconds))
        print("maar voor {} voelt dit als {} seconden oud".format(self.naam, infoleeftijdhondenjaren.seconds))
        
'''
hondjaren
geboorte functie uitbreiden, merk en zo
soort en kleur random
een beetje denken over de spelregels. 
'''