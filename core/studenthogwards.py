class StudentHogwards:
    def __init__(self, name, home_hogwards=None, mana=100, spells=[]):
        self.__name = name
        self.__home_hogwards = home_hogwards
        self.__mana = mana
        self.__spells = spells


    def get_name(self): return self.__name
    
    def get_home_hogwards(self): return self.__home_hogwards

    def get_mana(self): return self.__mana

    def learn_spell(self, spell): pass

    def cast_spell(self): pass