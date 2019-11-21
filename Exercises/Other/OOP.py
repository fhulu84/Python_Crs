class PlayerCharacter:
    membership = True  # class object attribute, STATIC not dynamic like the attributes in init
    # magic method/dunder method, constructor or init method, it is called when we instantiate an object

    def __init__(self, name='anonymous', age=0):  # default values
        if self.membership:  # or if PlayerCharacter.membership:
            self.name = name  # attributes
            self.age = age

    def run(self):  # self: refers to the playercharacter (like 'this' I think)
        print('run')
        return 'done'  # now it doesnt print None in terminal

    def shout(self):
        print(f'My name is {self.name}')
        # print(f'My name is {PlayerCharacter.name}') # Error: PlayerObject has no attribute name
        # print(f'Membership: {membership}') # Error: membership not defined
        print(f'Membership: {PlayerCharacter.membership}')  # Membership: True
        print(f'Membership: {self.membership}')  # Membership: True

    # STATIC method with cls, not used often, 
    # need to use it when we care about the class attributes maybe to change them
    @classmethod  
    def adding_things(cls, num1, num2):
        # return num1 + num2
        return cls('Teddy', num1 + num2) # instantiated a new object with cls, cls like self
    
    #STATIC method no access to cls, no idea about the class state, doesnt care attributes
    @staticmethod 
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter()
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

# print(f'Player1: {player1.name}, {player1.age}')
# print(f'Player2: {player2.name}, {player2.age}')

# print(player2.attack)  # 50
# print(player1.attack)  # Error, bcs no attack attribute

# prints run and None(because there is no return in the method)
# print(player1.run())

# help(player1) # prints blueprint of class
# help(list)

# print(player1.shout())

# no need an instance to run the method
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.shout())
