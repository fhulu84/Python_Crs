
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self,email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        # User.__init__(self,email) #old_method
        super().__init__(email)  # cleaner
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f'Attacking with arrows, arrows left: {self.num_arrows}')


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
# wizard1.sign_in()
# wizard1.attack()

archer1 = Archer('Robin', 30, 'robin@gmail.com')
# archer1.sign_in()
# archer1.attack()
# archer1.attack()
# archer1.attack()

# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))

# POLYMORPHISM

# def player_attack(char):
#   char.attack()


# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#   char.attack()

print(wizard1.email)
print(archer1.email)
