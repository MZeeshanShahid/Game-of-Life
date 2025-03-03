from rutenett import Rutenett



class Verden:
    def __init__(self, ant_rader, ant_kolonner):
        self.ant_rader = ant_rader
        self.ant_kolonner = ant_kolonner
        self.rutenett = Rutenett(ant_rader, ant_kolonner)
        self.rutenett.fyll_med_tilfeldige_celler()
        self.rutenett.koble_alle_celler()
        self.gen_nr = 0
    
    def tegn(self):
        self.rutenett.tegn_rutenett()
        print("Generasjon:", self.gen_nr)
        print("Antall levende celler: ",self.rutenett.antall_levende())
    
    def oppdatering(self):
        self.tegn()
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.rutenett.hent_celle(rad, kol).tell_levende_naboer()
        for rad in range(self.ant_rader):
            for kol in range(self.ant_kolonner):
                self.rutenett.hent_celle(rad, kol).oppdater_status()
        self.gen_nr += 1
