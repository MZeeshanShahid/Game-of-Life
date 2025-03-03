class Celle:
    def __init__(self):
        self.levende = False
        self.naboer = []  
        self.ant_naboer = 0
        self.ant_levende_naboer = 0

    def sett_doed(self):
        self.levende = False
    
    def sett_levende(self):
        self.levende = True
    
    def er_levende(self):
        if self.levende:
            return True
        else:
            return False
    
    def hent_status_tegn(self):
        if self.levende:
            return 'O'
        else:
            return '.'
    
    def legg_til_nabo(self, nabo):
        self.naboer.append(nabo)
    
    def tell_levende_naboer(self):
        self.ant_levende_naboer = 0
        for nabo in self.naboer:
            #if nabo is not None:
                if nabo.er_levende():
                    self.ant_levende_naboer += 1
    
    def oppdater_status(self):
        if self.levende:
            if self.ant_levende_naboer < 2:
                self.sett_doed()
            elif self.ant_levende_naboer > 3:
                self.sett_doed()
        else:
            if self.ant_levende_naboer == 3:
                self.sett_levende()