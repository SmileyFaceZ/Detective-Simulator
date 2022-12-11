import csv
import random


class Resume:

    def __init__(self):
        """
        Read resume from resume.csv
        """
        with open('resume.csv', encoding='utf-8-sig') as data_file:
            data = csv.DictReader(data_file)
            self.__all_resume = [_dict for _dict in data]
        self.__random_resume = []
        self.__history = None
        self.__round = 0

    def change_history(self, index):
        """ Change profile when you want to ask someone else.

        :param index: index to choose dictionary (int)
        :return: dictionary for information
        """
        self.__history = self.random_resume[index]
        self.__round += 1
        return self.__history

    @property
    def all_resume(self):
        """ It is an attribute (property) that retrieves all the history in the csv file into a list format.

        :return: all resume from resume.csv
        :rtype: list
        """
        return self.__all_resume

    @property
    def random_resume(self):
        """ that stores the profiles of 7 randomly selected suspects in a list format.

        :return: random resume
        :rtype: list
        """
        while len(self.__random_resume) < 7:
            resume = random.choice(self.__all_resume)
            if resume not in self.__random_resume:
                self.__random_resume.append(resume)

        return self.__random_resume

    def show_decease(self):
        while True:
            decease = random.choice(self.__all_resume)
            if decease not in self.random_resume:
                self.__history = decease
                break

    def show_murderer(self):
        """ random 1 of random_resume and this is a murderer.

        :return: murderer
        :rtype: dict
        """
        return random.choice(self.random_resume)

    def show_criminal(self, lastname):
        """ Show the criminal history of the suspect who wants information.

        :param lastname: murderer lastname
        :type: str
        """
        print(f"=============== Criminal History ==============")
        with open('criminal.csv', encoding='utf-8-sig') as criminal_file:
            criminal = csv.DictReader(criminal_file)
            for crime in criminal:
                if crime['lastname'] == lastname:
                    for i in range(2):
                        if crime[f"criminal{i + 1}"] != '':
                            print(f'• {crime[f"criminal{i + 1}"]}.')
        print()

    def show_personality(self, lastname):
        """ Show the personality history of the suspect who wants information.

        :param lastname: murderer lastname
        :type: str
        """
        print("=============== Personality ==============")
        with open('personality.csv', encoding='utf-8-sig') as person_file:
            personal = csv.DictReader(person_file)
            for person in personal:
                if person['lastname'] == lastname:
                    for i in range(2):
                        if person[f"personality{i + 1}"] != '':
                            print(f'• {person[f"personality{i + 1}"]}.')
        print()

    def __str__(self):  # resume for decease
        if self.__round == 0:
            return f"=============== History of the deceased ===============\n" \
                   f"• Name          : {self.__history['firstname']} {self.__history['lastname']}.\n" \
                   f"• Gender        : {self.__history['gender']}.\n" \
                   f"• Age           : {self.__history['age']} years old.\n" \
                   f"• Height        : {self.__history['height']} cm.\n" \
                   f"• Weight        : {self.__history['weight']} kg.\n" \
                   f"• Skin          : {self.__history['skin']}.\n" \
                   f"• Hair color    : {self.__history['hair_color']}.\n" \
                   f"• Career        : {self.__history['career']}.\n" \
                   f"• Tattoos       : {self.__history['tattoos']}.\n" \
                   f"• Glasses       : {self.__history['glasses']}.\n" \
                   f"• Drink alcohol : {self.__history['alcohol']}.\n" \
                   f"• Vehicle       : {self.__history['vehicle']}.\n"
        else:
            return f"=============== History of {self.__history['firstname']} " \
                   f"{self.__history['lastname']} ===============\n" \
                   f"• Gender        : {self.__history['gender']}.\n" \
                   f"• Age           : {self.__history['age']} years old.\n" \
                   f"• Height        : {self.__history['height']} cm.\n" \
                   f"• Weight        : {self.__history['weight']} kg.\n" \
                   f"• Skin          : {self.__history['skin']}.\n" \
                   f"• Hair color    : {self.__history['hair_color']}.\n" \
                   f"• Career        : {self.__history['career']}.\n" \
                   f"• Tattoos       : {self.__history['tattoos']}.\n" \
                   f"• Glasses       : {self.__history['glasses']}.\n" \
                   f"• Drink alcohol : {self.__history['alcohol']}.\n" \
                   f"• Vehicle       : {self.__history['vehicle']}.\n"
