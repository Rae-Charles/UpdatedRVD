from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd_list = []
        self.herd()

    def herd(self):
        trex = Dinosaur("Trex", 200, 25)
        velociraptor = Dinosaur("Velociraptor", 200, 25)
        triceratops = Dinosaur("Triceratops", 200, 25)
        self.herd_list.append(trex)
        self.herd_list.append(velociraptor)
        self.herd_list.append(triceratops)