class Person:
    def __init__(self, height, weight, name, country, experience=0):
        self.height = height
        self.weight = weight
        self.name = name
        self.country = country
        self.experience = experience

    def get_profile(self):
        return f"{self.name} is {self.height} cm tall, weighs {self.weight} kgs, lives in {self.country} and " \
               f"has {self.experience} years of experience in that field."


first_person = Person(174, 82, "Pesho", "Bulgaria")

print(first_person.get_profile())