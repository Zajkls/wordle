import os
import sys
from termcolor import colored, cprint
import colorama
from colorama import Fore
# Python code to pick a random
# word from a text file
import random
import time

def verify(target, xlist, low, high):
  if high >= low: 
    mid = (low + high) // 2
    if xlist[mid] == target:
      return True
    elif xlist[mid] < target:
      return verify(target, xlist, mid + 1, high)
    elif xlist[mid] > target:
      return verify(target, xlist, low, mid - 1)
  
  else:
    return False


# Open the file in read mode
with open("Valid_Words.txt", "r") as file:
	allText = file.read()
	words = list(map(str, allText.split()))
wordle = random.choice(words)
with open("answers.txt", "a") as a_file:
  a_file.write("\n")
  a_file.write(wordle)

first = wordle[0]
second = wordle[1]
third = wordle[2]
fourth = wordle[3]
fifth = wordle[4]
print("⬛⬛⬛⬛⬛")
print("⬛⬛⬛⬛⬛")
print("⬛⬛⬛⬛⬛")
print("⬛⬛⬛⬛⬛")
print("⬛⬛⬛⬛⬛")
print("⬛⬛⬛⬛⬛")
print("-----")
with open("words.txt","r") as file:
  allText = file.read()
  valid = list(map(str, allText.split()))
while True:
  word = input("")
  if word == "amogus":
    break
  elif not verify(word, valid, 0, len(valid) - 1):
    print("That is not a valid word. ")   
  else:
    break

import os
'''

⬛🟩⬛🟨⬛
🟩🟩🟩🟩🟩
'''

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()
if word[0] == first:
  letter1 = "GREEN"
  slot_1 = "🟩"
elif word[0] in wordle:
  letter1 = "LIGHTYELLOW_EX"
  slot_1 = "🟨"
else:
  letter1 = "LIGHTBLACK_EX"
  slot_1 = "⬛"
if word[1] == second:
  letter2 = "GREEN"
  slot_2 = "🟩"
elif word[1] in wordle:
  letter2 = "LIGHTYELLOW_EX"
  slot_2 = "🟨"
else:
  letter2 = "LIGHTBLACK_EX"
  slot_2 = "⬛"
if word[2] == third:
  letter3 = "GREEN"
  slot_3 = "🟩"
elif word[2] in wordle:
  letter3 = "LIGHTYELLOW_EX"
  slot_3 = "🟨"
else:
  letter3 = "LIGHTBLACK_EX"
  slot_3 = "⬛"
if word[3] == fourth:
  letter4 = "GREEN"
  slot_4 = "🟩"
elif word[3] in wordle:
  letter4 = "LIGHTYELLOW_EX"
  slot_4 = "🟨"
else:
  letter4 = "LIGHTBLACK_EX"
  slot_4 = "⬛"
if word[4] == fifth:
  letter5 = "GREEN"
  slot_4 = "🟩"
elif word[4] in wordle:
  letter5 = "LIGHTYELLOW_EX"
  slot_5 = "🟨"
else:
  letter5 = "LIGHTBLACK_EX"
  slot_5 = "⬛"
letters1 = getattr(Fore, letter1)
let1 = letters1 + word[0]
letters2 = getattr(Fore, letter2)
let2 = letters2 + word[1]
letters3 = getattr(Fore, letter3)
let3 = letters3 + word[2]
letters4 = getattr(Fore, letter4)
let4 = letters4 + word[3]
letters5 = getattr(Fore, letter5)
let5 = letters5 + word[4]
word1 = let1 + let2 + let3 + let4 + let5
if word == wordle:
  print("🟩🟩🟩🟩🟩")
  for i in range(5):
    print("⬛⬛⬛⬛⬛")
  print("Genius. ")
  sys.exit()
else:
  print(word1)
  print(Fore.WHITE + "⬛⬛⬛⬛⬛")
  print("⬛⬛⬛⬛⬛")
  print("⬛⬛⬛⬛⬛")
  print("⬛⬛⬛⬛⬛")
  print("⬛⬛⬛⬛⬛")
  print("-----")
  if word != wordle:
    with open("words.txt","r") as file:
      allText = file.read()
      valid = list(map(str, allText.split()))
    while True:
      word = input("")
      if not verify(word, valid, 0, len(valid) - 1):
        print("That is not a valid word. ")   
      else:
        break
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    # now, to clear the screen
    cls()
    if word[0] == first:
    letter1 = "GREEN"
    slot_6 = "🟩"
  elif word[0] in wordle:
    letter1 = "LIGHTYELLOW_EX"
    slot_6 = "🟨"
  else:
    letter1 = "LIGHTBLACK_EX"
    slot_6 = "⬛"
  if word[1] == second:
    letter2 = "GREEN"
    slot_7 = "🟩"
  elif word[1] in wordle:
    letter2 = "LIGHTYELLOW_EX"
    slot_7 = "🟨"
  else:
    letter2 = "LIGHTBLACK_EX"
    slot_7 = "⬛"
  if word[2] == third:
    letter3 = "GREEN"
    slot_8 = "🟩"
  elif word[2] in wordle:
    letter3 = "LIGHTYELLOW_EX"
    slot_8 = "🟨"
  else:
    letter3 = "LIGHTBLACK_EX"
    slot_8 = "⬛"
  if word[3] == fourth:
    letter4 = "GREEN"
    slot_9 = "🟩"
  elif word[3] in wordle:
    letter4 = "LIGHTYELLOW_EX"
    slot_9 = "🟨"
  else:
    letter4 = "LIGHTBLACK_EX"
    slot_9 = "⬛"
  if word[4] == fifth:
    letter5 = "GREEN"
    slot_10 = "🟩"
  elif word[4] in wordle:
    letter5 = "LIGHTYELLOW_EX"
    slot_10 = "🟨"
  else:
    letter5 = "LIGHTBLACK_EX"
    slot_5 = "⬛"
    word2 = let1 + let2 + let3 + let4 + let5
    if word == wordle:
      print(word1)
      print(let1)
      time.sleep(0.5)
      print(let2)
      time.sleep(0.5)
      print(let3)
      time.sleep(0.5)
      print(let4)
      time.sleep(0.5)
      print(let5)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("Magnificent. ")
      sys.exit()
    else:
      print(word1)
      print(word2)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("⬛⬛⬛⬛⬛")
      print("⬛⬛⬛⬛⬛")
      print("⬛⬛⬛⬛⬛")
      print("-----")
  
  if word != wordle:
    with open("words.txt","r") as file:
      allText = file.read()
      valid = list(map(str, allText.split()))
    while True:
      word = input("")
      if not verify(word, valid, 0, len(valid) - 1):
        print("That is not a valid word. ")   
      else:
        break
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    # now, to clear the screen
    cls()
  if word[0] == first:
    letter1 = "GREEN"
    slot_1 = "🟩"
  elif word[0] in wordle:
    letter1 = "LIGHTYELLOW_EX"
    slot_1 = "🟨"
  else:
    letter1 = "LIGHTBLACK_EX"
    slot_1 = "⬛"
  if word[1] == second:
    letter2 = "GREEN"
    slot_2 = "🟩"
  elif word[1] in wordle:
    letter2 = "LIGHTYELLOW_EX"
    slot_2 = "🟨"
  else:
    letter2 = "LIGHTBLACK_EX"
    slot_2 = "⬛"
  if word[2] == third:
    letter3 = "GREEN"
    slot_3 = "🟩"
  elif word[2] in wordle:
    letter3 = "LIGHTYELLOW_EX"
    slot_3 = "🟨"
  else:
    letter3 = "LIGHTBLACK_EX"
    slot_3 = "⬛"
  if word[3] == fourth:
    letter4 = "GREEN"
    slot_4 = "🟩"
  elif word[3] in wordle:
    letter4 = "LIGHTYELLOW_EX"
    slot_4 = "🟨"
  else:
    letter4 = "LIGHTBLACK_EX"
    slot_4 = "⬛"
  if word[4] == fifth:
    letter5 = "GREEN"
    slot_4 = "🟩"
  elif word[4] in wordle:
    letter5 = "LIGHTYELLOW_EX"
    slot_5 = "🟨"
  else:
    letter5 = "LIGHTBLACK_EX"
    slot_5 = "⬛"
    letters1 = getattr(Fore, letter1)
    let1 = letters1 + word[0]
    letters2 = getattr(Fore, letter2)
    let2 = letters2 + word[1]
    letters3 = getattr(Fore, letter3)
    let3 = letters3 + word[2]
    letters4 = getattr(Fore, letter4)
    let4 = letters4 + word[3]
    letters5 = getattr(Fore, letter5)
    let5 = letters5 + word[4]
    word3 = let1 + let2 + let3 + let4 + let5
    if word == wordle:
      print(word1)
      print(word2)
      print(let1)
      time.sleep(0.5)
      print(let2)
      time.sleep(0.5)
      print(let3)
      time.sleep(0.5)
      print(let4)
      time.sleep(0.5)
      print(let5)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("Impressive.")
      sys.exit()
    else:
      print(word1)
      print(word2)
      print(word3)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("⬛⬛⬛⬛⬛")
      print("⬛⬛⬛⬛⬛")
      print("-----")
  
  if word != wordle:
    with open("words.txt","r") as file:
      allText = file.read()
      valid = list(map(str, allText.split()))
    while True:
      word = input("")
      if not verify(word, valid, 0, len(valid) - 1):
        print("That is not a valid word. ")   
      else:
        break
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    # now, to clear the screen
    cls()
    if word[0] == first:
      letter1 = "GREEN"
    elif word[0] in wordle:
      letter1 = "LIGHTYELLOW_EX"
    else:
      letter1 = "LIGHTBLACK_EX"
    if word[1] == second:
      letter2 = "GREEN"
    elif word[1] in wordle:
      letter2 = "LIGHTYELLOW_EX"
    else:
      letter2 = "LIGHTBLACK_EX"
    if word[2] == third:
      letter3 = "GREEN"
    elif word[2] in wordle:
      letter3 = "LIGHTYELLOW_EX"
    else:
      letter3 = "LIGHTBLACK_EX"
    if word[3] == fourth:
      letter4 = "GREEN"
    elif word[3] in wordle:
      letter4 = "LIGHTYELLOW_EX"
    else:
      letter4 = "LIGHTBLACK_EX"
    if word[4] == fifth:
      letter5 = "GREEN"
    elif word[4] in wordle:
      letter5 = "LIGHTYELLOW_EX"
    else:
      letter5 = "LIGHTBLACK_EX"
    letters1 = getattr(Fore, letter1)
    let1 = letters1 + word[0]
    letters2 = getattr(Fore, letter2)
    let2 = letters2 + word[1]
    letters3 = getattr(Fore, letter3)
    let3 = letters3 + word[2]
    letters4 = getattr(Fore, letter4)
    let4 = letters4 + word[3]
    letters5 = getattr(Fore, letter5)
    let5 = letters5 + word[4]
    word4 = let1 + let2 + let3 + let4 + let5
    if word == wordle:
      print(word1)
      print(word2)
      print(word3)
      print(let1)
      time.sleep(0.5)
      print(let2)
      time.sleep(0.5)
      print(let3)
      time.sleep(0.5)
      print(let4)
      time.sleep(0.5)
      print(let5)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("Splendid. ")
      sys.exit()
    else:
      print(word1)
      print(word2)
      print(word3)
      print(word4)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("⬛⬛⬛⬛⬛")
      print("-----")
  
  if word != wordle:
    with open("words.txt","r") as file:
      allText = file.read()
      valid = list(map(str, allText.split()))
    while True:
      word = input("")
      if not verify(word, valid, 0, len(valid) - 1):
        print("That is not a valid word. ")   
      else:
        break
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    # now, to clear the screen
    cls()
    if word[0] == first:
      letter1 = "GREEN"
    elif word[0] in wordle:
      letter1 = "LIGHTYELLOW_EX"
    else:
      letter1 = "LIGHTBLACK_EX"
    if word[1] == second:
      letter2 = "GREEN"
    elif word[1] in wordle:
      letter2 = "LIGHTYELLOW_EX"
    else:
      letter2 = "LIGHTBLACK_EX"
    if word[2] == third:
      letter3 = "GREEN"
    elif word[2] in wordle:
      letter3 = "LIGHTYELLOW_EX"
    else:
      letter3 = "LIGHTBLACK_EX"
    if word[3] == fourth:
      letter4 = "GREEN"
    elif word[3] in wordle:
      letter4 = "LIGHTYELLOW_EX"
    else:
      letter4 = "LIGHTBLACK_EX"
    if word[4] == fifth:
      letter5 = "GREEN"
    elif word[4] in wordle:
      letter5 = "LIGHTYELLOW_EX"
    else:
      letter5 = "LIGHTBLACK_EX"
    letters1 = getattr(Fore, letter1)
    let1 = letters1 + word[0]
    letters2 = getattr(Fore, letter2)
    let2 = letters2 + word[1]
    letters3 = getattr(Fore, letter3)
    let3 = letters3 + word[2]
    letters4 = getattr(Fore, letter4)
    let4 = letters4 + word[3]
    letters5 = getattr(Fore, letter5)
    let5 = letters5 + word[4]
    word5 = let1 + let2 + let3 + let4 + let5
    if word == wordle:
      print(word1)
      print(word2)
      print(word3)
      print(word4)
      print(let1)
      time.sleep(0.5)
      print(let2)
      time.sleep(0.5)
      print(let3)
      time.sleep(0.5)
      print(let4)
      time.sleep(0.5)
      print(let5)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("Great. ")
    else: 
      print(word1)
      print(word2)
      print(word3)
      print(word4)
      print(word5)
      print(Fore.WHITE + "⬛⬛⬛⬛⬛")
      print("-----")
    
  if word != wordle:
    with open("words.txt","r") as file:
      allText = file.read()
      valid = list(map(str, allText.split()))
    while True:
      word = input("")
      if not verify(word, valid, 0, len(valid) - 1):
        print("That is not a valid word. ")   
      else:
        break
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    # now, to clear the screen
    cls()
    if word[0] == first:
      letter1 = "GREEN"
    elif word[0] in wordle:
      letter1 = "LIGHTYELLOW_EX"
    else:
      letter1 = "LIGHTBLACK_EX"
    if word[1] == second:
      letter2 = "GREEN"
    elif word[1] in wordle:
      letter2 = "LIGHTYELLOW_EX"
    else:
      letter2 = "LIGHTBLACK_EX"
    if word[2] == third:
      letter3 = "GREEN"
    elif word[2] in wordle:
      letter3 = "LIGHTYELLOW_EX"
    else:
      letter3 = "LIGHTBLACK_EX"
    if word[3] == fourth:
      letter4 = "GREEN"
    elif word[3] in wordle:
      letter4 = "LIGHTYELLOW_EX"
    else:
      letter4 = "LIGHTBLACK_EX"
    if word[4] == fifth:
      letter5 = "GREEN"
    elif word[4] in wordle:
      letter5 = "LIGHTYELLOW_EX"
    else:
      letter5 = "LIGHTBLACK_EX"
    letters1 = getattr(Fore, letter1)
    let1 = letters1 + word[0]
    letters2 = getattr(Fore, letter2)
    let2 = letters2 + word[1]
    letters3 = getattr(Fore, letter3)
    let3 = letters3 + word[2]
    letters4 = getattr(Fore, letter4)
    let4 = letters4 + word[3]
    letters5 = getattr(Fore, letter5)
    let5 = letters5 + word[4]
    word6 = let1 + let2 + let3 + let4 + let5
'''    if word == wordle:
      print(word1)
      print(word2)
      print(word3)
      print(word4)
      print(word5)
      print(let1)
      time.sleep(0.5)
      print(let2)
      time.sleep(0.5)
      print(let3)
      time.sleep(0.5)
      print(let4)
      time.sleep(0.5)
      print(let5)
      print(Fore.WHITE + "Phew. ")
    else:
      print(word1)
      print(word2)
      print(word3)
      print(word4)
      print(word5)
      print(word6)
      print(Fore.RED + "Uh oh. " + wordle + " was the word")
'''