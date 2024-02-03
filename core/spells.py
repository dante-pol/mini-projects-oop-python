class Spell:
    def __init__(self, name, description, mana):
        self.__name = name
        self.__description = description
        self.__size_mana = size_mana

    def get_name(self): 
        return self.__name

    def get_description(self): 
        return self.__description

    def get_size_mana(self): 
        return self.__size_mana
    
    def cast(self, target): pass