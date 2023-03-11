class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

person = Person("Amy Juma", 18, "Female")
print(person.get_info())

person.set_name("Yuri Gideon")
person.set_age(22)
person.set_gender("Male")

print(person.get_info())

person.set_name("Felisters Georgia")
person.set_age(15)
person.set_gender("Female")

print(person.get_info())


class Voter(Person):
    def can_vote(self):
        try:
            if self.age >= 18:
                print("This person is eligible to vote.")
            else:
                print("This person is not eligible to vote yet.")
        except TypeError:
            print("Age must be an integer.")


voter = Voter("Yuri", 22, "Male")
voter.get_info()
voter.can_vote()

voter = Voter("Thuso", "twenty", "Female")
voter.get_info()
voter.can_vote()



