
## Defining a class called Pet which is the parent, using the init method that 
# holds parameters & below the arguements is instances variables for the class Pet. 
# This is called everytime a new dog is created. This class has mulitple methods of 
# a dog's actions/behavior when you play, feed, do nothing, etc. 

class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        
    def get_toy(self, toy):
        self.toys.append(toy)
        for toy in self.toys:
            self.happiness += toy.use()

# def __str__ is a description of the objects: It is envoking data into a string 
# This shows the status of the dog's name, fullness, and happiness. 

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        
        """ % (self.name, self.fullness, self.happiness)         

# Cuddlypet is a chlild class. While CuddlyPet has it's own __init__ method, it 
# overrides class Pet it only has access to the functions not the properties.
# The CuddlyPet also has a super() functionb which will go to class Pet and call the funcions
# to instantiate class Pet's properties. 

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger,)
        self.cuddle_level = cuddle_level
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        
    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()



