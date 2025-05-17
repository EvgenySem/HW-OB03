# 1. Создайте базовый класс `Animal`,
# который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
from fcntl import FASYNC

import jsonpickle

class Animal:
    def __init__(self, kind, name, age, health_status, sound):
        self.kind = kind
        self.name = name
        self.age = age
        self.health_status = health_status
        self.sound = sound

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} кушает')


# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
    def __init__(self, kind, name, age, health_status, sound, wings_size):
        super().__init__(kind, name, age, health_status, sound)
        self.wings_size = wings_size

    def make_sound(self):
        print(f'Птица вида {self.kind} издала звук: {self.sound}')

    def eat(self):
        print(f'{self.kind} {self.name} кушает')


class Mammal(Animal):
    def __init__(self, kind, name, age, health_status, sound, diet):
        super().__init__(kind, name, age, health_status, sound)
        self.diet = diet  # herbivores or carnivores

    def make_sound(self):
        print(f'Млекопитающее вида {self.kind} издало звук: {self.sound}')

    def eat(self):
        print(f'{self.kind} {self.name} кушает')


class Reptile(Animal):
    def __init__(self, kind, name, age, health_status, sound, is_snake):
        super().__init__(kind, name, age, health_status, sound)
        self.is_snake = is_snake

    def make_sound(self):
        print(f'Рептилия вида {self.kind} издала звук: {self.sound}')

    def eat(self):
        print(f'{self.kind} {self.name} кушает')


# 3. Продемонстрируйте полиморфизм:
# создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

def animal_sound(*animals_lists):
    animals = []
    for arg in animals_lists:
        animals += arg

    for animal in animals:
        animal.make_sound()


# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        self.zoo_workers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'{animal.kind} {animal.name} добавлен в зоопарк {self.name}')

    def add_worker(self, worker):
        self.zoo_workers.append(worker)
        print(f'{worker.job} {worker.name} добавлен в зоопарк {self.name}')


# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Worker:
    def __init__(self, work_id, name, job):
        self.work_id = work_id
        self.name = name
        self.job = job


class ZooKeeper(Worker):
    def __init__(self, work_id, name, job):
        super().__init__(work_id, name, job)

    def feed_animal(self, animal):
        print(f'{self.job} {self.name} покормил {animal.kind} {animal.name}')


class Veterinarian(Worker):
    def __init__(self, work_id, name, job):
        super().__init__(work_id, name, job)

    def heal_animal(self, animal, status):
        animal.health_status = status
        print(f'{self.job} {self.name} лечил {animal.kind} {animal.name}. Статус здоровья: {status}')


#------------------------------------------------------------
# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ
# Save to file
def save_zoo(zoo):
    encoded_ex = jsonpickle.encode(zoo)
    print(encoded_ex)
    with open("saved_zoo", "w") as f:
        f.write(encoded_ex)

    return print(f'Данные зоопарка {zoo.name} были сохранены в файл')

# Download from file
def download_zoo():
    with open("saved_zoo", "r+") as f:
        written_instance = f.read()
        decoded_ex = jsonpickle.decode(written_instance)
        print(f'Данные зоопарка {decoded_ex.name} успешно загружены')
    return decoded_ex


# Загрузка объекта Зоопарка из файла
zoo_Central = download_zoo()

# Запуск функции звучания для всех животных в зоопарке
animal_sound(zoo_Central.animals)

# Запуск методов работников из объекта зоопарка
zoo_Central.zoo_workers[0].feed_animal(zoo_Central.animals[3])

print(zoo_Central.animals[2].health_status)
zoo_Central.zoo_workers[2].heal_animal(zoo_Central.animals[2], "Healing in progress") # "Good" or "Healing in progress" (to test)
print(zoo_Central.animals[2].health_status)

#------------------------------------------------------------
# ПЕРВЫЙ ЗАПУСК ПРОГРАММЫ (Без файла с сохраненным состоянием)
# Первое создание экземпляров каждого класса
#
# birds = [Bird("Sparrow","Jack", 2, "Good", "Чирик","20 sm"),
#          Bird("Chicken","Coco", 1, "Good", "Ко-ко-ко", "15 sm"),
#          Bird("Hawk","Birdie", 3, "Healing", "Иииии", "20 sm")]
#
# mammals = [Mammal("Tiger", "Diego", 3, "Good", "Рррррр", "carnivores"),
#            Mammal("Panther", "Blacky", 3, "Good", "Рррраааауу", "carnivores"),
#            Mammal("Deer", "John", 4, "Goood", "Иу-иии-и-и", "herbivores")]
#
# reptiles = [Reptile("Lizard", "Blizzard", 1, "Good", "Ххх", False),
#             Reptile("Cobra", "Marry", 2, "Good", "Ссссссс", True),
#             Reptile("Crocodile", "Bombardile", 3, "Good", "Аррр", False)]
#
# employes = [ZooKeeper("1","Ivan Ivanov", "Смотритель"),
#             ZooKeeper("2","Vasily Vasilyev", "Смотритель"),
#             Veterinarian("3","Anna Healer", "Главный Врач")]
#
# zoo_Central = Zoo("Central", "New York")
#
# #------------------------------------------------------------
# # Запуск функции звучания для списка животных (при первом создании)
# animal_sound(birds, mammals, reptiles)
# print('')
#
# #------------------------------------------------------------
# # Первое добавление всех экземпляров класса в зоопарк
# for animal in birds:
#     zoo_Central.add_animal(animal)
#
# for animal in mammals:
#     zoo_Central.add_animal(animal)
#
# for animal in reptiles:
#     zoo_Central.add_animal(animal)
#
# for worker in employes:
#     zoo_Central.add_worker(worker)
# print('')
#
# #------------------------------------------------------------
# # Запуск методов работников зоопарка их списка работников (при первом создании)
# employes[0].feed_animal(mammals[1])
# employes[1].feed_animal(reptiles[0])
#
# print(birds[2].health_status)
# employes[2].heal_animal(birds[2], "Good")
# print(birds[2].health_status)
#
#------------------------------------------------------------
# Сохранение состояния экземпляра зоопарка
save_zoo(zoo_Central)

