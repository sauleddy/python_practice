
class Person():
    def __init__(self, name):
        # print('Person()__init__')
        self.name = name
        self.__hidden_name = name + '_hidden'

    @property
    def hide_name(self):
        print('inside hidden_name getter')
        return self.__hidden_name

    @hide_name.setter
    def hide_name(self, input_name):
        print('inside hidden_name setter')
        self.__hidden_name = input_name

    def get_name(self):
        return self.name

    def talk(self):
        print('I am ' + self.name)


class SuperMan(Person):
    def __init__(self):
        # print('SuperMan()__init__')
        super().__init__('Clark')
        SuperMan.static_name = 'static_name'

    def talk(self):
        print('I am superman ' + self.name)

    @classmethod
    def fly(cls):
        print('I can fly.')


Ed = Person('Ed')
print(Ed.get_name())

Clark = SuperMan()
Clark.fly()
Clark.talk()
print(Clark.get_name())

print(Clark.hide_name)
Clark.hide_name = 'Tom'

