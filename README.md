# Detective-Simulator

- Project title

	=> Detective Simulator

- Project overview and features

	This game lets you try yourself as a detective. with a total of 7 suspects In which we can choose whether to view information, ask for a hint, or guess the culprit, which those hints will match the particular culprit There may be suspects whose history is similar to the hint, so you have to guess it correctly. You can guess 2 times and have 3 hints.

- Required libraries and tools

	* Python 3.10.8
	* Module
		-> import time : To set the character to be displayed on the screen later than the time we set.
		-> import sys : Use to make characters appear one by one, and use a “for loop”.
		-> import subprocess : Used for clearing the screen on the console (must be run on terminal only).

- Program design

	* Class  Game:
			-> This class will be rendered at the start of the game in the console.
	* Class Resume:
			-> Show suspect history extracted from “resume.csv” file.
	* Class Hints:
			-> will show the hint (When players want) a total of two hints from a total of five hints are randomly drawn. Extracted from “hints.csv” file

- Code structure

	* criminal.csv : It is a file that stores crimes committed by people. (There may or may not be a crime).

	* hints.csv : It's a clue file for each murderer.

	* personality.csv : It is a file that stores personality of people. It may contain all 3 habits.

	* resume.csv : It is a file that stores the history of people.

	* detective-simulator.py : Is a file that is specifically intended for running the game.

	* logo.py
		-> ASCII art (WELCOME_LOGO) from https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 
		-> ASCII art (DETECTIVE_LOGO) from https://ascii.co.uk/art/detective

- GitHub Link : https://github.com/SmileyFaceZ/Detective-Simulator

<< Kantaphat 6510545268 >>
