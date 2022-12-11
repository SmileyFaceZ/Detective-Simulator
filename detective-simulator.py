from logo import *
from game import Game
from resume import Resume
from hints import Hints
import subprocess


QUIT_GAME = ''
print(WELCOME_LOGO)
while True:
    GAME_RUN = False

    print(DETECTIVE_LOGO)

    game = Game()
    hint = Hints()
    code_list = ['[A01]', '[A02]', '[A03]', '[A04]', '[A05]', '[A06]', '[A07]']
    resume = Resume()

    murderer = resume.show_murderer()
    option = input(f'Start game (S) | Quit (Q) : ').upper()

    if option == "S":
        subprocess.run('clear', shell=True)  # run in terminal
        game.entry_name()
        resume.show_decease()
        print(resume)
        while True:
            count_code = [code for code in code_list if code != '']
            game.effect(text=f"💬Detective's Assistant: There are {len(count_code)} suspects in total.")
            print(f"1. {resume.random_resume[0]['firstname']} {resume.random_resume[0]['lastname']} {code_list[0]}\n"
                  f"2. {resume.random_resume[1]['firstname']} {resume.random_resume[1]['lastname']} {code_list[1]}\n"
                  f"3. {resume.random_resume[2]['firstname']} {resume.random_resume[2]['lastname']} {code_list[2]}\n"
                  f"4. {resume.random_resume[3]['firstname']} {resume.random_resume[3]['lastname']} {code_list[3]}\n"
                  f"5. {resume.random_resume[4]['firstname']} {resume.random_resume[4]['lastname']} {code_list[4]}\n"
                  f"6. {resume.random_resume[5]['firstname']} {resume.random_resume[5]['lastname']} {code_list[5]}\n"
                  f"7. {resume.random_resume[6]['firstname']} {resume.random_resume[6]['lastname']} {code_list[6]}\n")

            while True:
                menu = input("View suspect information (I) | Get a hints (H) | Guess the killer (A) : ").upper()
                if menu == "I":
                    code_check = game.to_information()
                    if code_check is not True:
                        dict_suspect = resume.change_history(index=code_check)
                        print(resume)
                        resume.show_personality(lastname=dict_suspect['lastname'])
                        resume.show_criminal(lastname=dict_suspect['lastname'])
                        break

                elif menu == "H":
                    hint.show_hints(lastname=murderer['lastname'])
                    hint.to_hint()

                elif menu == "A":
                    answer_correct = game.to_answer(resume_list=resume.random_resume,
                                                    murderer_lastname=murderer['lastname'],
                                                    murderer_firstname=murderer['firstname'],
                                                    code=code_list)
                    hint.increase_answer_time()
                    if answer_correct == "R":  # game finished
                        GAME_RUN = True
                        break

                    elif answer_correct == "Q":
                        GAME_RUN = True
                        QUIT_GAME = "Q"
                        break

                else:
                    print('Not have option!.')

                if menu == 'A':
                    break

            if GAME_RUN:
                break

        if QUIT_GAME == "Q":
            break

    elif option == "Q":
        break

    else:
        print("Not have option!.")
