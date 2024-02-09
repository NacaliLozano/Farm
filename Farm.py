class Animal:
    
    def __init__(self):
        self.caress_counter = 10
        self.food_counter = 10
        self.is_dead = False
        self.sound = None

        
    def makeSound(self):
        return self.sound
         
    def increase_caress_counter(self):
        self.caress_counter += 10
        
    def decrease_caress_counter(self):
        self.caress_counter -= 1
        
    def increase_food_counter(self):
        self.food_counter += 10
        
    def decrease_food_counter(self):
        self.food_counter -= 1
     
        
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.sound = "Woof!"
        
class Cat(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        self.sound = "Meaow!"

class Cow(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        self.sound = "Moo!"
    
class Sheep(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        self.sound = "Baa!"
    
class Pig(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        self.sound = "Oink!"
    
class Game:
    
    def __init__(self):
        self.game_over = False
        self.cat_instance = Cat()
        self.dog_instance = Dog()
        self.cow_instance = Cow()
        self.sheep_instance = Sheep()
        self.pig_instance = Pig()
    
    def action(self, action):
        
        if action.lower() == "caress cat":
            if not self.cat_instance.is_dead:
                self.cat_instance.increase_caress_counter()
                print(self.cat_instance.makeSound())
            else:
                print("Cat is dead!")
        elif action.lower() == "feed cat":
            if not self.cat_instance.is_dead:
                self.cat_instance.increase_food_counter()
                print(self.cat_instance.makeSound())
            else:
                print("Cat is dead!")
                
        elif action.lower() == "caress dog":
            if not self.dog_instance.is_dead:
                self.dog_instance.increase_caress_counter()
                print(self.dog_instance.makeSound())
            else:
                print("Dog is dead!")
        elif action.lower() == "feed dog":
            if not self.dog_instance.is_dead:
                self.dog_instance.increase_food_counter()
                print(self.dog_instance.makeSound())
            else:
                print("Dog is dead!")

        elif action.lower() == "caress cow":
            if not self.cow_instance.is_dead:
                self.cow_instance.increase_caress_counter()
                print(self.cow_instance.makeSound())
            else:
                print("Cow is dead!")
        elif action.lower() == "feed cow":
            if not self.cow_instance.is_dead:
                self.cow_instance.increase_food_counter()
                print(self.cow_instance.makeSound())
            else:
                print("Cow is dead!")
        
        elif action.lower() == "caress sheep":
            if not self.sheep_instance.is_dead:
                self.sheep_instance.increase_caress_counter()
                print(self.sheep_instance.makeSound())
            else:
                print("Sheep is dead!")
        elif action.lower() == "feed sheep":
            if not self.sheep_instance.is_dead:
                self.sheep_instance.increase_food_counter()
                print(self.sheep_instance.makeSound())
            else:
                print("Sheep is dead!")
        
        elif action.lower() == "caress pig":
            if not self.pig_instance.is_dead:
                self.pig_instance.increase_caress_counter()
                print(self.pig_instance.makeSound())
            else:
                print("Pig is dead!")
        elif action.lower() == "feed pig":
            if not self.pig_instance.is_dead:
                self.pig_instance.increase_food_counter()
                print(self.pig_instance.makeSound())
            else:
                print("Pig is dead!")
        
        else:
            pass
        
        self.cat_instance.decrease_caress_counter()
        self.cat_instance.decrease_food_counter()
        
        self.dog_instance.decrease_caress_counter()
        self.dog_instance.decrease_food_counter()
        
        self.cow_instance.decrease_caress_counter()
        self.cow_instance.decrease_food_counter()
        
        self.sheep_instance.decrease_caress_counter()
        self.sheep_instance.decrease_food_counter()
        
        self.pig_instance.decrease_caress_counter()
        self.pig_instance.decrease_food_counter()
        
        if self.cat_instance.caress_counter == 0 or self.cat_instance.food_counter == 0:
            self.cat_instance.is_dead = True
            print("Cat died!")
        if self.dog_instance.caress_counter == 0 or self.dog_instance.food_counter == 0:
            self.dog_instance.is_dead = True
            print("Dog died!")
        if self.cow_instance.caress_counter == 0 or self.cow_instance.food_counter == 0:
            self.cow_instance.is_dead = True
            print("Cow died!")
        if self.sheep_instance.caress_counter == 0 or self.sheep_instance.food_counter == 0:
            self.sheep_instance.is_dead = True
            print("Sheep died!")
        if self.pig_instance.caress_counter == 0 or self.pig_instance.food_counter == 0:
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

