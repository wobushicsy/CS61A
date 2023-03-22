class Bear:
    """A Bear."""

    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)

class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, str):
        if str in self.pouch_contents:
            print('object already in pouch')
            return
        self.pouch_contents += [str]

    def __str__(self):
        if len(self.pouch_contents) == 0:
            return "The kangaroo's pouch is empty"
        else:
            return "The kangaroo's pouch contains: " + str(self.pouch_contents)