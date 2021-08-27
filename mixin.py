class Person():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + ' is walking')


class StudyMixin():
    def study(self):
        print(self.name + ' is studying')   



class Student(Person,StudyMixin):
    def __init__(self, name,age):
        Person.__init__(self,name)
        self.age=age

    def eat(self):
        print(self.name + ' is eating')




Student('Tom',10).study()
# StudyMixin().study()
