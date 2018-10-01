class people:
    def __init__(self, name, emotion, sex, age):
        self.name = name
        self.emotion = emotion
        self.sex = sex
        self.age = age

    def life(self):
        print(self.name + ' is ' + self.emotion)
        if self.sex == 'male':
            print(self.name + ' is a ' + self.sex + ' and he is ' + self.age)
        elif self.sex == 'female':
            print(self.name + ' is a ' + self.sex + ' and she is ' + self.age)
        else:
            print('Wrong sex!')


people_name = input('Please input the name:\n')
people_emotion = input('Please input the emotion:\n')
people_sex = input('Please input the sex (male / female):\n')
people_age = input('Please input the age:\n')
# p1 = people('小明', 'HAPPY 😄', 'male', '20')
print('\n')
p1 = people(people_name, people_emotion, people_sex, people_age)
p1.life()
