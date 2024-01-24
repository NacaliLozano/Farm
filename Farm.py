class Animal:
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meaow!"
    
def animal_sound(animal):
    return animal.sound()

# Example usage:
dog_instance = Dog()
cat_instance = Cat()

print(animal_sound(dog_instance))  # Outputs: Woof!
print(animal_sound(cat_instance))  # Outputs: Meow!