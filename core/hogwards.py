class Hogwards:
    def __init__(self, students=[], spells=[]):
        self.__students = students
        self.__spells = spells

    def enroll_student(self, student): pass

    def teach_spell(self, spell): pass

    def simulate_duel(self):
        student1, student2 = self.__select_two_students()
        can_cast_one_student = __is_cast_one_student()

        while student1.get_mana() != 0 and student2.get_mana() != 0:
            if can_cast_one_student:
                student1.cast_spell(student2)
                can_cast_one_student = False
            else:
                student2.cast_spell(student1)
                can_cast_one_student = True

    def __is_cast_one_student(self) -> bool:
        import random
        w = random.randint(0, 10)
        if w > 5:
            return = True
        else:
            return = False


    def __select_two_students(self):
        import random

        index_one_student = random.randint(0, len(self.__students) - 1) 
        student1 = self.__students[index_one_student]

        index_two_student = random.randint(0, len(self.__students) - 1) 
        
        while index_one_student == index_two_student:
            index_two_student = random.randint(0, len(self.__students) - 1) 

        return student1, student2