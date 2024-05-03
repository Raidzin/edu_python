class Pet:
    def __init__(self, name, typ, age, says='mew'):
        self.name = name
        self.typ = typ
        self.age = age
        self.says = says

    def say(self):
        print(f'{self.name} говорит: {self.says}. но это {self.typ}')


    def __str__(self):
        return f'Pet: {self.name},{self.age}'



# pets = [
#     {
#         'name': 'Бася',
#         'type': 'кот',
#         'age': 8,
#     },
#     {
#         'name': 'Влад',
#         'type': 'пёс',
#         'age': 20,
#     },
#     {
#         'name': 'Себастьян',
#         'type': 'рыба',
#         'age': 0.5,
#     },
# ]


pets = [
    Pet('Бася', 'кот', 8),
    Pet('Влад', 'пёс', 20, 'гав'),
    Pet('Себас', 'рыба', 0.5, 'Слава великому Аинзу'),
]


if __name__ == '__main__':
    for pet in pets:
        pet.say()
        print(pet.name, pet.says)