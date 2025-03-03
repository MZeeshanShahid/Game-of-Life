import random

from celle import Celle


class Rutenett:
    def __init__(self, ant_rader, ant_kolonner):
        self.ant_rader = ant_rader
        self.ant_kolonner = ant_kolonner
        self.rutene = []  # Oppretter en tom liste

        for x in range(ant_rader):
            rad = []  # Oppretter en tom liste for én rad
            for z in range(ant_kolonner):
                rad.append(Celle())  # Legger til et nytt Celle-objekt i raden
            self.rutene.append(rad)  # Legger hele raden til rutenettet. Dette blir en to-dimensjonalt array hvor rader er horisontale og kolonner er vertikale.
    
    def lag_celle(self, rad, kol):
        celle = Celle()
        self.rutene[rad][kol] = celle
        if random.random() <= 0.3333:
            celle.sett_levende()
        else:
            celle.sett_doed()
    
    def fyll_med_tilfeldige_celler(self):
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.lag_celle(rad, kol)
    
    def hent_celle(self, rad, kol):
        if rad < 0 or kol < 0 or rad >= self.ant_rader or kol >= self.ant_kolonner:
            return None
        else:
            return self.rutene[rad][kol]
    
    
    def tegn_rutenett(self):
        print("+---" * self.ant_kolonner + "+")
        
        for rad in self.rutene:
            # Oppretter en liste for celle-statusene i denne raden
            celle_statuser = []
            for celle in rad:
                celle_statuser.append(celle.hent_status_tegn())  
            
            rad_tekst = "| " + " | ".join(celle_statuser) + " |"  # Sett sammen celle-statusene med " | " som separator
            print(rad_tekst)  # Skriv ut celleraden
            print("+---" * self.ant_kolonner + "+") # Tegner horisontal linje etter hver rad

    def sett_naboer(self, rad, kol):
        sjekk_nabo = [-1, 1]
        celle = self.hent_celle(rad, kol)
        if celle:
            for i in sjekk_nabo:
                nabo = self.hent_celle(rad + i, kol) # Naboene over og under.
                if nabo:
                    celle.legg_til_nabo(nabo)
                
                nabo = self.hent_celle(rad + i, kol - i) # Naboene øverst venstre og nederst høyre.
                if nabo:
                    celle.legg_til_nabo(nabo)
                
                nabo = self.hent_celle(rad + i, kol + i) # Naboene øverst høyre og nederst venstre.
                if nabo:
                    celle.legg_til_nabo(nabo)
                
                nabo = self.hent_celle(rad, kol + i) # Naboene til venstre og høyre.
                if nabo:
                    celle.legg_til_nabo(nabo)
    
    def koble_alle_celler(self):
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.sett_naboer(rad, kol)

    def antall_levende(self):
        teller = 0
        for i in range(len(self.rutene)):
            for z in range(len(self.rutene[i])):
                if self.rutene[i][z].er_levende():
                    teller += 1
        return teller
