class Dog:
    '''Representing a dog'''
    def __init__(self,_name,_age,_color):
        self.name=_name
        self._age=_age
        self.color=_color
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_color(self):
        return self.color
    def bark(self):
        print("Ghew ghew")
    def __str__(self):
        return self.name
dog = Dog("jemmy", 2,"white")
print(dog.get_color())
print(dog)
anohter_dog = Dog("dog_name", 23,'blue')
anohter_dog.bark()