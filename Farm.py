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

class Game:
    
    def __init__(self):
        self.cat_tease_counter = 5
        self.dog_tease_counter = 5
        self.game_over = False
    
    def action(self, action):
        if action.lower() == "tease cat":
            self.cat_tease_counter += 5
            print("Cat teased.")
        elif action.lower() == "tease dog":
            self.cat_tease_counter += 5
            print("Dog teased.")
        else:
            pass
        
        self.cat_tease_counter -= 1
        self.dog_tease_counter -= 1
        
        if self.cat_tease_counter == 0:
            print("Cat died.")
        if self.dog_tease_counter == 0:
            print("Dog died.")
        
        if self.cat_tease_counter < 1 and self.dog_tease_counter < 1:
            self.game_over = True
            print("Game Over.")
            
    def loop(self):
        while self.game_over is False:
            self.action(input("Type an action: "))

game = Game()
game.loop()
