class Cat():
    name = ''
    color = ''
    weight = ''

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self):
        print('МЯУ')

    def seeInform(self):
        print('Имя киси: ' + self.name, 'Цвет: ' +
              self.color, 'Вес: ' + self.weight + 'кг', sep='\n')


kitty = Cat('Баунти', 'Чёрно-белый', '9')
kitty.meow()
kitty.seeInform()
