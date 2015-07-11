__author__ = 'Nataly'


class Project:

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name




