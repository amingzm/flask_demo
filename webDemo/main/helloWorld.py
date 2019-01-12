class Student():
    def __init__(self, score):
        self.score = score

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must between 0 ~ 100!')
        self._age = value


s = Student(100)
s.age = 10
print(s.age)
