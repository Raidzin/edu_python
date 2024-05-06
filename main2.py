class Pet:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('fndsjldbhuiawbnkajbdwjkb')


class Cat(Pet):
    def __init__(self, name, speechless: bool):
        super().__init__(name)
        self.speechless = speechless


    def say(self):
        if self.speechless:
            super().say()
            return
        print('mew')


class Dog(Pet):
    def say(self):
        print('gav')


class Snake(Pet):
    pass


cat = Cat('Барсик')
dog = Dog('Бобик')
snake = Snake('Гоша')


def say_hello(pet: Pet):
    pet.say()


for pet in (cat, dog, snake):
    say_hello(pet)
