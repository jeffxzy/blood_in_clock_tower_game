from classing.character_class.character import *
from classing.game import *

class FunctionClass():
    def __init__(self) -> None:
        self.game = Game()
        self.from_character = Character()
        self.to_character = Character()
        self.func = self.func_default()
        print(self.from_character.name)
    
    def func_default():
        print(f"[Error] Reached an empty function!")

    def run_func(self):
        if self.from_character.name == "Character" or self.to_character.name == "Character":
            print(f"[Error] From None Character {self.from_character.name}, To None Character {self.to_character.name}. ")
        self.func(game=self.game, from_character=self.from_character, to_character=self.to_character)    
