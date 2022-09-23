class StringVar():
    str = ''

    def get(self):
        return self.str

    def set(self, str):
        self.str = str


str = StringVar()
str.set('Бубис')
print(str.get())
