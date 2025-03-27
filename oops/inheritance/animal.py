class Animal:
    def eat(self):
        print("Animal eat")

    def speak(self):
        print("Animal speak")


class Dog(Animal):
    breed = "Urban"
    def eat(self):
        print("Eat bons")

    def speak(self):
        print("Dog barks")


dog = Dog()
dog.eat()
print(dog.breed)
dog.speak()
del dog.breed


"""
Dog(Animal) means Dog is a subclass of Animal.
Method Overriding: speak() method in Dog overrides the one in Animal.
"""