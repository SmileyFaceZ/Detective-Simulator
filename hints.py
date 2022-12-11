import csv
import random
from game import Game


class Hints(Game):

    def __init__(self):
        super().__init__()
        self.__hint = []
        self.__random_num = []
        self.__attempt = 0
        self.__answer_time = 0

    def show_hints(self, lastname):
        """ Take the hint of the person you want to retrieve from the “hints.csv” file and add it to “self.hints”

        :param lastname: murderer lastname
        :return: list of all hints real murderer
        :rtype: list
        """
        with open('hints.csv', mode='r', encoding='utf-8-sig') as hint_file:
            hint = csv.DictReader(hint_file)
            for _dict in hint:
                if _dict['lastname'] == lastname:
                    self.__hint.append(_dict['hint1'])
                    self.__hint.append(_dict['hint2'])
                    self.__hint.append(_dict['hint3'])
                    self.__hint.append(_dict['hint4'])
                    self.__hint.append(_dict['hint5'])
                    return self.__hint

    def increase_answer_time(self):
        """
        increase attribute answer_time
        """
        self.__answer_time += 1

    def to_hint(self):
        """ When the player needs a hint, it will be shown. and collect random numbers to enter into
            "self.random_num" (the numbers are hints. It won't take this hint again.)

        :return: Detective assistant dialogue for each event
        :rtype: str
        """
        count = 0

        if self.__attempt == 0:
            self.__attempt += 1
            count = 1
        elif self.__attempt == 1:
            self.__attempt += 1
            count = 2
        elif self.__attempt == 2:
            if self.__answer_time == 0:
                return self.effect('💬Detective\'s Assistant 🕵🏼: ❗You must guess one person to get one hints!.\n')

            elif self.__answer_time == 1:
                self.__attempt += 1
                count = 3
        elif self.__attempt > 2:
            return self.effect('💬Detective\'s Assistant 🕵🏼: ❗️You can get for 3 hints❕.\n')

        while True:
            random_num = random.randint(0, 4)

            if random_num not in self.__random_num:
                self.__random_num.append(random_num)
                self.effect(f"💬Detective\'s Assistant 🕵🏼: 💡Hint ({count}/3): {self.__hint[random_num]}.")
                self.effect("💬Detective\'s Assistant 🕵🏼: ❗ will be shown only once (must remember)")
                print()
                break
