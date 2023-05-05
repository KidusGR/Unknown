#!/usr/bin/python3
#Just a test

from spellchecker import SpellChecker
import os
import time
from rich.console import Console
from rich.text import Text


console = Console()
spell = SpellChecker()
alpha = "abcdefghijklmnopqrstuvwxyz"
check = 0
username = open("./username").readlines()[0].strip()


def printBanner():
	banner = Text(("-"*40)+"\n\tUNKNOWN WORD BARN\n"+("-"*40))
	commands = Text("\n'exit()' -- exit\n'print()' -- print words(db)\n")
	banner.stylize("bold magenta")
	commands.stylize("bold blue")
	console.print(banner+commands)


def spellcheck(word):
	line = Text("\tWord Unknown\n")
	line1 = Text(f"suggestions : {spell.candidates(word)}\n")
	line1.stylize("bold yellow")
	line.stylize("bold red")
	os.system('clear')
	if word in spell:
		adder(word)
	else:
		console.print(line,line1)


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
		addedLine = Text("\tWord added to the DB\n")
		addedLine.stylize("bold green")
		console.print(addedLine)
	else:
		os.system('clear')
		alreadyLine = Text("\tWord already in the DB\n")
		alreadyLine.stylize("bold yellow")
		console.print(alreadyLine)


def exit():
	os.system('clear')
	line = Text(("-"*30)+"\n\tG00D-!3Y3\n"+("-"*30))
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
	consoleLine = Text("Enter the Word >> ")
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
	for w in word:
		if w.upper() in alpha.upper():
			pass
		else:
			printInvalid()
			check = 1
	if check:
		continue
	
	
	spellcheck(word)
