#!/usr/bin/python3
#Just a test

from spellchecker import SpellChecker
import os
import time


spell = SpellChecker()
alpha = "abcdefghijklmnopqrstuvwxyz"
check = 0

def spellcheck(word):
	global spell
	'''print(spell.candidates(word))
	print(spell.unknown(word))
	print(spell[word])'''
	os.system('clear')
	if word in spell:
		adder(word)
	else:
		print(f"spelling incorrect\nsuggestions : {spell.candidates(word)}\n")

def adder(word):
	if word.lower() not in words:
		with open("./Data/words", "a") as file:
			file.write(f"{word.lower()}\n")
		os.system('clear')
		print("word added to db\n")
	else:
		os.system('clear')
		print("word already in db\n")

def exit():
	os.system('clear')
	print("G00D-!3Y3")
	time.sleep(1)

def printer():
	os.system('clear')
	print(f"db : {words}\n")

while True:
	words = [d.strip() for d in open("./Data/words", "r").readlines()]
	
	print("'exit()' -- exit\n'print()' -- print words(db)\n")
	check = 0
	word = input("Enter the Word: ")
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
			os.system('clear')
			print("invalid input!\n")
			check = 1
	if check:
		continue
	
	
	spellcheck(word)
