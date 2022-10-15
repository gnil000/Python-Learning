# Ветеринарная лечебница:
# список животных
# список болезней
# список хозяев
# журнал посещений

import sqlite3

con = sqlite3.connect('Veterinary hospital.db')
curObj = con.cursor()


def createDB():  # Создание таблиц базы данных
    curObj.execute(
        'create table Animals(id integer primary key autoincrement, animal_name text not null)')
    con.commit()
    curObj.execute(
        'create table Disease(id_animal integer, disease text, foreign key(id_animal) references Animals(id))')
    con.commit()
    curObj.execute(
        'create table Master(id_animal integer, master text, foreign key(id_animal) references Animals(id))')
    con.commit()
    curObj.execute(
        'create table Visits(id_animal integer, visit text, foreign key(id_animal) references Animals(id))')
    con.commit()


def intoValueInDB(value):  # Заполнение таблицы анималс, без айдишника, айдишник сам заполняется
    curObj.execute("insert into Animals(animal_name) values(?)", value)
    con.commit()


# Заполнение таблицы хозяев животных, вводится айди животного и его хозяин
def intoValueDB2(value):
    curObj.execute("insert into Master values(?, ?)", value)
    con.commit()

# Это был цикл на заполнение таблицы анималс
# value = []
# newVal = input()
# value.append(newVal)
# while (str(value[0]) != str(0)):
#     intoValueInDB(value)
#     value[0] = input()


# Ето цикл на заполнение хозяев, больше я не стала заполнять таблицы, там такой же принцип, можно же так оставить?
s = input()
value = s.split()
while (str(value[0]) != str(0)):
    intoValueDB2(value)
    s = input()
    value = s.split()


con.close()
