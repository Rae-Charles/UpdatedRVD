from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.fleet()
    
    def fleet(self):
        terminator1 = Robot("Terminator T1", 200)
        terminator2 = Robot("Terminator T2", 200)
        terminator3 = Robot("Terminator T3", 200)
        self.fleet_list.append(terminator1)
        self.fleet_list.append(terminator2)
        self.fleet_list.append(terminator3)