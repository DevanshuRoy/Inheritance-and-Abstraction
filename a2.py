#abstraction

from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def __init__(self,name):
        self.name=name

    def move(self):
        print("I am a", self.name)
        print("I can walk and run")
        print()

class snake(animal):
    def __init__(self,name):
        self.name=name

    def move(self):
        print("I am a", self.name)
        print("I can crawl")
        print()

class crane(animal):
    def __init__(self,name):
        self.name=name
    def move (self):
        print("I am a", self.name)
        print("I can fly and walk")
        print()


human1=human("human")
human1.move()

snake1=snake("snake")
snake1.move()

crane1=crane("crane")
crane1.move()