"""
Inheritance -have ts own methods and also parent's
child/derived --> parent/base
class A --> class B
single inheritance
"""
class carshowroom:

    def __init__(self):
        print("BMW Car showroom")
    def doors(self):
        print("Doors")
    def wheels(self):
        print("wheels")

#class ThreeM:
 #   def folier(self):
  #      print("Foilers")

class BMW(carshowroom):

    def sunroof(self):
        print("Sunroof")

c=BMW()
c.doors()
c.wheels()
c.sunroof()
#c.folier()