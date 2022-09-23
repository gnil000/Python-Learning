class Animal():
    name = ''

    def __init__(self, name):
        self.name = name
        print('Родилось животное ' + self.name)

    def eat(self):
        print('Ням-ням')

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def makeNoise(self):
        print(self.name + ' говорит Гррр')


ani = Animal('Булка')
print(ani.getName())
ani.setName('Оля Серябкина')
ani.eat()
ani.makeNoise()
