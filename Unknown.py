#!/usr/bin/python3
#Just a test

from spellchecker import SpellChecker
import os
import time
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
import readline


console = Console()
spell = SpellChecker()
alpha = "abcdefghijklmnopqrstuvwxyz"
check = 0
username = open("./username").readlines()[0].strip()


def printBanner():
	banner = Text(("-"*40)+"\n\tUNKNOWN WORD BARN\n"+("-"*40))
	wordNum = Text(f"\n\nYour Words - ( {len(words)} )\n")
	wordNum.stylize("bold yellow")
	wordNum.stylize("bold green", str(wordNum).index('(')+1, -2)
	commands = Text("\n'exit()' -- exit Unknown\n'print()' -- Print words(DB)\n")
	banner.stylize("bold magenta")
	commands.stylize("bold blue")
	console.print(banner+wordNum+commands)


def spellcheck(word):
	misspelled = Text(f'{word}')
	misspelled.stylize("bold green")
	line = Text("\tWord Unknown\n")
	line1 = Text(f"suggestions for \"")
	line2 = Text(f"\" : {spell.candidates(word)}\n")
	line1.stylize("bold yellow")
	line2.stylize("bold yellow")
	line.stylize("bold red")
	os.system('clear')
	if word in spell:
		adder(word)
	else:
		console.print(line,line1,misspelled,line2)


def printInvalid():
	line = Text("\tINVALID INPUT!\n")
	line.stylize("bold red")
	os.system('clear')
	console.print(line)
	

def adder(word):
	if word.lower() not in words:
		with open(f"/home/{username}/.UnknownData/words", "a") as file:
			file.write(f"{word.lower()}\n")
		os.system('clear')
		line = Text(f'{word}')
		line.stylize("bold yellow")
		addedLine = Text("Word \"")
		addedLine1 = Text("\" added to the DB\n")
		addedLine.stylize("bold green")
		addedLine1.stylize("bold green")
		console.print(addedLine,line,addedLine1)
	else:
		os.system('clear')
		line = Text(f'{word}')
		line.stylize("bold green")
		alreadyLine = Text("Word \"")
		alreadyLine1 = Text("\" already in the DB\n")
		alreadyLine.stylize("bold yellow")
		alreadyLine1.stylize("bold yellow")
		console.print(alreadyLine,line,alreadyLine1)


def exit():
	os.system('clear')
	line = Text(("-"*30)+"\n\tG00D-BY3\n"+("-"*30))
	line.stylize("bold magenta")
	console.print(line)
	time.sleep(1)


def printer():
	os.system('clear')
	line = Text(f"db : {words}\n")
	line.stylize("bold yellow")
	console.print(line)


while True:
	words = [d.strip() for d in open(f"/home/{username}/.UnknownData/words", "r").readlines()]
	
	printBanner()
	check = 0
	consoleLine = Text("Enter Word >> ")
	consoleLine.stylize("blue")
	consoleLine.stylize("bold yellow", 0, -3)
	
	console.print(consoleLine, end="")
	word = input()
	
	if word == 'exit()':
		exit()
		break
	elif word == 'print()':
		printer()
		continue
	elif word == "":
		printInvalid()
		continue
	for w in word:
		if w.upper() in alpha.upper():
			pass
		else:
			printInvalid()
			check = 1
	if check:
		continue
	
	
	spellcheck(word)
