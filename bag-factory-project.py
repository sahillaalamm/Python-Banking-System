class Factory():
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips
        
class Bhopal_Factory(Factory):
    def __init__(self, material, zips, colour):
        super().__init__(material, zips)
        self.colour = colour

class Pune_Factory(Bhopal_Factory):
    def __init__(self, material, zips, colour, pockets):
        super().__init__(material, zips, colour)
        self.pockets = pockets