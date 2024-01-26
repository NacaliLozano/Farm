class Animal:
    
    def __init__(self):
        self.tease_counter = 5
        
    def sound(self):
        pass
    
    def increase_tease_counter(self):
        self.tease_counter += 5
        
    def decrease_tease_counter(self):
        self.tease_counter -= 1
        
class Dog(Animal):

    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    
    def sound(self):
        return "Meaow!"
    
def animal_sound(animal):
    return animal.sound()

class Game:
    
    def __init__(self):
        self.game_over = False
        self.cat_instance = Cat()
        self.dog_instance = Dog()
    
    def action(self, action):
        
        if action.lower() == "tease cat":
            self.cat_instance.increase_tease_counter()
            animal_sound(self.cat_instance)
        elif action.lower() == "tease dog":
            self.dog_instance.increase_tease_counter()
            animal_sound(self.dog_instance)
        else:
            pass
        
        self.cat_instance.decrease_tease_counter()
        self.dog_instance.decrease_tease_counter()
        
        if self.cat_instance.tease_counter == 0:
            print("Cat died.")
        if self.dog_instance.tease_counter == 0:
            print("Dog died.")
        
        if self.cat_instance.tease_counter < 1 and self.dog_instance.tease_counter < 1:
            self.game_over = True
            print("Game Over.")
            
    def loop(self):
        while self.game_over is False:
            self.action(input("Type an action: "))

game = Game()
game.loop()
