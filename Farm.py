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

class Cow(Animal):
    
    def sound(self):
        return "Moo!"
    
class Sheep(Animal):
    
    def sound(self):
        return "Baa!"
    
class Pig(Animal):
    
    def sound(self):
        return "Oink!"
    
class Game:
    
    def __init__(self):
        self.game_over = False
        self.cat_instance = Cat()
        self.dog_instance = Dog()
        self.cow_instance = Cow()
        self.sheep_instance = Sheep()
        self.pig_instance = Pig()
    
    def action(self, action):
        
        if action.lower() == "tease cat":
            if not self.cat_instance.is_dead:
                self.cat_instance.increase_tease_counter()
                print(self.cat_instance.sound())
            else:
                print("Cat is dead!")
        elif action.lower() == "feed cat":
            if not self.cat_instance.is_dead:
                self.cat_instance.increase_food_counter()
                print(self.cat_instance.sound())
            else:
                print("Cat is dead!")
                
        elif action.lower() == "tease dog":
            if not self.dog_instance.is_dead:
                self.dog_instance.increase_tease_counter()
                print(self.dog_instance.sound())
            else:
                print("Dog is dead!")
        elif action.lower() == "feed dog":
            if not self.dog_instance.is_dead:
                self.dog_instance.increase_food_counter()
                print(self.dog_instance.sound())
            else:
                print("Dog is dead!")

        elif action.lower() == "tease cow":
            if not self.cow_instance.is_dead:
                self.cow_instance.increase_tease_counter()
                print(self.cow_instance.sound())
            else:
                print("Cow is dead!")
        elif action.lower() == "feed cow":
            if not self.cow_instance.is_dead:
                self.cow_instance.increase_food_counter()
                print(self.cow_instance.sound())
            else:
                print("Cow is dead!")
        
        elif action.lower() == "tease sheep":
            if not self.sheep_instance.is_dead:
                self.sheep_instance.increase_tease_counter()
                print(self.sheep_instance.sound())
            else:
                print("Sheep is dead!")
        elif action.lower() == "feed sheep":
            if not self.sheep_instance.is_dead:
                self.sheep_instance.increase_food_counter()
                print(self.sheep_instance.sound())
            else:
                print("Sheep is dead!")
        
        elif action.lower() == "tease pig":
            if not self.pig_instance.is_dead:
                self.pig_instance.increase_tease_counter()
                print(self.pig_instance.sound())
            else:
                print("Pig is dead!")
        elif action.lower() == "feed pig":
            if not self.pig_instance.is_dead:
                self.pig_instance.increase_food_counter()
                print(self.pig_instance.sound())
            else:
                print("Pig is dead!")
        
        else:
            pass
        
        self.cat_instance.decrease_tease_counter()
        self.cat_instance.decrease_food_counter()
        
        self.dog_instance.decrease_tease_counter()
        self.dog_instance.decrease_food_counter()
        
        self.cow_instance.decrease_tease_counter()
        self.cow_instance.decrease_food_counter()
        
        self.sheep_instance.decrease_tease_counter()
        self.sheep_instance.decrease_food_counter()
        
        self.pig_instance.decrease_tease_counter()
        self.pig_instance.decrease_food_counter()
        
        if self.cat_instance.tease_counter == 0 or self.cat_instance.food_counter == 0:
            self.cat_instance.is_dead = True
            print("Cat died!")
        if self.dog_instance.tease_counter == 0 or self.dog_instance.food_counter == 0:
            self.dog_instance.is_dead = True
            print("Dog died!")
        if self.cow_instance.tease_counter == 0 or self.cow_instance.food_counter == 0:
            self.cow_instance.is_dead = True
            print("Cow died!")
        if self.sheep_instance.tease_counter == 0 or self.sheep_instance.food_counter == 0:
            self.sheep_instance.is_dead = True
            print("Sheep died!")
        if self.pig_instance.tease_counter == 0 or self.pig_instance.food_counter == 0:
            self.pig_instance.is_dead = True
            print("Pig died!")
        
        if self.cat_instance.is_dead and self.dog_instance.is_dead and self.sheep_instance.is_dead and self.cow_instance.is_dead and self.pig_instance.is_dead:
            self.game_over = True
            print("Game Over!")
            
    def loop(self):
        while self.game_over is False:
            self.action(input("Type an action: "))

game_instance = Game()
game_instance.loop()
