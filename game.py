import random
import sys
import subprocess
import time


class Game:

    def __init__(self):
        self.__name = None
        self.__answer = None
        self.__inter = None
        self.__count_answer = 0
        self.__days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.__places = ['Club', 'Crosswalk', 'Overpass', 'Toilet', 'Dormitory',
                         'Home', 'Hotel', 'Bathroom', 'Living room', 'Kitchen']

    def entry_name(self):
        """
        Enter Detective's name and print out.
        """
        random_day = random.choice(self.__days)
        random_place = random.choice(self.__places)
        self.__name = input('Please enter 🕵🏻‍ detective name! : ').upper()
        self.effect(f'💬Detective\'s Assistant 🕵🏼: Hello detective "{self.__name}" today there '
                    f'was a murder at a {random_place}. The body was found on {random_day}.\n')

    def to_information(self):
        """ Change history for information and print out.

        :return: index for list or True
        :rtype: int or boolean
        """

        while True:
            self.__inter = input("Go back (B) | Enter the suspect's code for interrogation : ").upper()
            subprocess.run('clear', shell=True)  # run in terminal
            print()
            if self.__inter == 'B':
                return True
            elif self.__inter == 'A01':
                return 0
            elif self.__inter == 'A02':
                return 1
            elif self.__inter == 'A03':
                return 2
            elif self.__inter == 'A04':
                return 3
            elif self.__inter == 'A05':
                return 4
            elif self.__inter == 'A06':
                return 5
            elif self.__inter == 'A07':
                return 6
            else:
                self.effect("💬Detective\'s Assistant 🕵🏼: That's it not code for the suspect ❌ \n")

    def to_answer(self, resume_list, murderer_lastname, murderer_firstname, code):
        """ Answer for the murder and when guess 2 times, game is end and show real murderer

        :param resume_list: random resume from resume class (list)
        :param murderer_lastname: real murderer lastname (str)
        :param murderer_firstname: real murderer firstname (str)
        :param code: code list for the suspect (list)
        :return: boolean
        """
        index = ''
        while True:
            self.__answer = input("Go back (B) | Enter the suspect's code : ").upper()
            subprocess.run('clear', shell=True)  # run in terminal
            if self.__answer == "B":
                break
            elif self.__answer == 'A01':
                index = 0
                break
            elif self.__answer == 'A02':
                index = 1
                break
            elif self.__answer == 'A03':
                index = 2
                break
            elif self.__answer == 'A04':
                index = 3
                break
            elif self.__answer == 'A05':
                index = 4
                break
            elif self.__answer == 'A06':
                index = 5
                break
            elif self.__answer == 'A07':
                index = 6
                break
            else:
                self.effect("💬Detective\'s Assistant 🕵🏼: That's it not code for the suspect ❌ \n")

        if self.__answer == "B":
            return None

        if resume_list[index]['lastname'] == murderer_lastname:
            self.effect("💬Detective\'s Assistant 🕵🏼: Congratulation 👏, this person is the killer.")
            return self.__play_again()

        elif resume_list[index]['lastname'] == '':
            print('❗️This code has already been answered. Please enter another code.\n')

        else:
            self.__count_answer += 1
            if self.__count_answer == 1:
                self.effect("💬Detective\'s Assistant 🕵🏼:❗️This is not a real murderer. "
                            "You can guess only (1) more time!.\n")
                resume_list[index]['firstname'] = ''
                resume_list[index]['lastname'] = ''
                code[index] = ''
                return False

            elif self.__count_answer == 2:
                self.effect(f"💬Detective\'s Assistant 🕵🏼: You lose!. The murderer "
                            f"is \"{murderer_firstname} {murderer_lastname}\".\n")
                return self.__play_again()

    def __play_again(self):
        """ Method ask if you want to play again or not.

        :return: str
        """
        while True:
            play_again = input("Play again? (R) | Quit (Q): ").upper()
            if play_again == "R":
                subprocess.run('clear', shell=True)  # run in terminal
                return "R"
            elif play_again == "Q":
                return "Q"
            else:
                print("Not have option!.")

    def effect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.04)
        print()
