class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == 'Dog':
            return Dog()
        elif animal_type == 'Cat':
            return Cat()
        return None

# Usage
animal = AnimalFactory.get_animal("Dog")
print(animal.speak())  # Output: Woof!
