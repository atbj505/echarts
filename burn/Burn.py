from pyecharts import Line


class Burn(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("name must be string")
        self._name = name