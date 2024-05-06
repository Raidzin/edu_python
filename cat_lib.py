class Cat:
    def __init__(self, name):
        self._cat_name = name

    @property
    def name(self):
        return self._cat_name

    @name.setter
    def name(self, value):
        print('Мне нельзя менять имя')