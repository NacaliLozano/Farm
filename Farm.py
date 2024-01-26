class Animal:
    
    def __init__(self):
        self.tease_counter = 5
        self.food_counter = 5
        self.is_dead = False
         
    def increase_tease_counter(self):
        self.tease_counter += 5
        
    def decrease_tease_counter(self):
        self.tease_counter -= 1
        
    def increase_food_counter(self):
        self.food_counter += 5
        
    def decrease_food_counter(self):
        self.food_counter -= 1
     
        
class Dog(Animal):

    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    
    def sound(self):
        return "Meaow!"
    
class Game:
    
    def __init__(self):
        self.game_over = False
        self.cat_instance = Cat()
        self.dog_instance = Dog()
    
    def action(self, action):
        
        if action.lower() == "tease cat":
            if not self.cat_instance.is_dead:
                self.cat_instance.increase_tease_counter()
                print(self.cat_instance.sound())
            else:
                print("Cat is dead!")
        elif action.lower() == "tease dog":
            if not self.dog_instance.is_dead:
                self.dog_instance.increase_tease_counter()
                print(self.dog_instance.sound())
            else:
                print("Dog is dead!")
        elif action.lower() == "feed cat":
            if not self.cat_instance.is_dead:
                self.cat_instance.increase_food_counter()
                print(self.cat_instance.sound())
            else:
                print("Cat is dead!")
        elif action.lower() == "feed dog":
            if not self.dog_instance.is_dead:
                self.dog_instance.increase_food_counter()
                print(self.dog_instance.sound())
            else:
                print("Dog is dead!")
        else:
            pass
        
        self.cat_instance.decrease_tease_counter()
        self.cat_instance.decrease_food_counter()
        
        self.dog_instance.decrease_tease_counter()
        self.dog_instance.decrease_food_counter()
        
        if self.cat_instance.tease_counter == 0 or self.cat_instance.food_counter == 0:
            self.cat_instance.is_dead = True
            print("Cat died!")
        if self.dog_instance.tease_counter == 0 or self.dog_instance.food_counter == 0:
            self.dog_instance.is_dead = True
            print("Dog died!")
        
        if self.cat_instance.is_dead and self.dog_instance.is_dead:
            self.game_over = True
            print("Game Over!")
            
    def loop(self):
        while self.game_over is False:
            self.action(input("Type an action: "))

game_instance = Game()
game_instance.loop()
