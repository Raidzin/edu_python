class Square:
    multiplier = 2

    def __init__(self, number: int | float):
        self._number = number

    @property
    def number(self):
        return self._number ** self.multiplier

    @number.setter
    def number(self, value):
        self._number = value ** 0.5


if __name__ == '__main__':
    box = Square(7)
    box2 = Square(4)

    print(box.multiplier)
    print(box2.multiplier)
    Square.multiplier = 3
    print(box.multiplier)
    print(box2.multiplier)

    print(box.number)
    box.number = 9
    print(box.number)
