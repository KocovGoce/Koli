class Kola(object):  #objekt roditel 
    def __init__(self,tip_kola,boja_kola):#odredi atributi 
        print(tip_kola,boja_kola)#print na aatributie
class Ford(Kola):# klasa sin
     def __init__(self):
        super().__init__('Ford Taunos','bela')
       

print("amerikanska kola ")
class Fiat(Kola):
    def __init__(self):
        super().__init__('Fiat', 'crvena')

class Lancia(Kola):
  def  __init__(self):

        super().__init__('Lancia','rozeva')

kola1=Ford() #povikuvanje na sinovi klasii
kola2=Fiat()
kola3=Lancia()