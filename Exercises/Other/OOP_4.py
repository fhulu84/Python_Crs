
# MULTIPLE INHERETENCE
class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        self.num_arrows -= 1
        print(f'Attacking with arrows, arrows left: {self.num_arrows}')

    def run(self):
        print('Run really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
      Archer.__init__(self, name, arrows)
      Wizard.__init__(self, name, power)


hb1 = HybridBorg('hb1', 40, 20)
hb1.attack()
hb1.check_arrows()
hb1.sign_in()
