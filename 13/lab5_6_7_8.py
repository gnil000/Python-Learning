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


class Cat(Animal):
    color = ''
    weight = ''

    def __init__(self, name, color, weight):
        Animal.__init__(self, name)
        self.name = name
        self.color = color
        self.weight = weight
        print('Родился кот ' + self.name)

    def meow(self):
        print('МЯУ')

    def makeNoise(self):
        print(self.name+' говорит Мяу')

    def seeInform(self):
        print('Имя киси: ' + self.name, 'Цвет: ' +
              self.color, 'Вес: ' + self.weight + 'кг', sep='\n')


class Dog(Animal):
    breed = ''
    weight = ''

    def __init__(self, name, breed, weight):
        Animal.__init__(self, name)
        self.name = name
        self.breed = breed
        self.weight = weight
        print('Родилась собака ' + self.name)

    def makeNoise(self):
        print(self.name + ' говорит Гав')

    def seeInform(self):
        print('Имя собеки: ' + self.name, 'Порода: ' +
              self.breed, 'Вес: ' + self.weight + 'кг', sep='\n')


kitty = Cat('Мейби Бейби', 'Белая', '7')
dog1 = Dog('Псинка', 'Бигль', '9')
dog2 = Dog('Мухтар', 'Чихуа-хуа', '2')
animal = Animal('Животинка')
kitty.eat()
kitty.makeNoise()
dog1.eat()
dog1.makeNoise()
dog2.eat()
dog2.makeNoise()
animal.eat()
animal.makeNoise()
