class Doggy:
    birth_of_dogs = 0
    num_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print('왈왈')

    def born(self):
        self.num_of_dogs += 1
        self.birth_of_dogs += 1
        print('강아지가 태어났습니다. 축하합니다!')

    def die(self):
        self.num_of_dogs -= 1
        print('개가 죽었습니다')

    def get_status(self):
        print(f'태어난 강아지의 수는 {self.birth_of_dogs}마리이고 현재 있는 개의 수는 {self.num_of_dogs}마리 입니다')


happy = Doggy('해피', '치와와')
print(happy.name)
print(happy.breed)
print(happy.bark())
print(happy.born())
print(happy.born())
print(happy.born())
print(happy.die())
print(happy.get_status())



