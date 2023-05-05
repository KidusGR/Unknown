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

def printBanner():
	banner = Text(("-"*40)+"\n\tUNKNOWN WORD BARN\n"+("-"*40))
	commands = Text("\n'exit()' -- exit\n'print()' -- print words(db)\n")
	banner.stylize("bold magenta")
	commands.stylize("bold blue")
	console.print(banner+commands)

def spellcheck(word):
	line = Text(f"spelling incorrect\nsuggestions : {spell.candidates(word)}\n")
	line.stylize("bold red")
	os.system('clear')
	if word in spell:
		adder(word)
	else:
		console.print(line)

def printInvalid():
	line = Text("invalid input!\n")
	line.stylize("bold red")
	os.system('clear')
	console.print(line)
	

def adder(word):
	if word.lower() not in words:
		with open("./Data/words", "a") as file:
			file.write(f"{word.lower()}\n")
		os.system('clear')
		addedLine = Text("word added to db\n")
		addedLine.stylize("bold green")
		console.print(addedLine)
	else:
		os.system('clear')
		alreadyLine = Text("word already in db\n")
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
	words = [d.strip() for d in open("./Data/words", "r").readlines()]
	
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
