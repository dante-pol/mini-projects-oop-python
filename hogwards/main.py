class Program:

    @staticmethod
    def main():
        from studenthogwards import StudentHogwards
        from spells import Spell
        from hogwards import Hogwards

        spell1 = Spell("Liza", "Liza", -1)
        spell2 = Spell("Max", "Max", 1)
        spell3 = Spell("Kara", "Kara", 101)
        spell4 = Spell("Oks", "Oks", 1)

        student1 = StudentHogwards("A", "SES")
        student2 = StudentHogwards("B", "SES")
        student3 = StudentHogwards("C", "SES")
        student4 = StudentHogwards("D", "SES")
        student5 = StudentHogwards("F", "SES")

        student_zero = StudentHogwards("Dmitry Rak", "Java/C++/C#/Python/Dart", mana=1000)

        hogwards = Hogwards([student_zero], [spell3])
        hogwards.simulate_duel()



if __name__ == "__main__":
    Program.main()