import os
import sys
from termcolor import colored, cprint
import colorama
from colorama import Fore
import random
import time
import pyperclip as pc
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


#1
if word[0] == first:
  letter1 = "GREEN" 
  slot_1 = "🟩"
  color1 = colored(word[0], 'green')
elif word[0] in wordle:
  letter1 = "LIGHTYELLOW_EX"
  slot_1 = "🟨"
  color1 = colored(word[0], 'yellow')
else:
  letter1 = "LIGHTBLACK_EX"
  slot_1 = "⬛"
  color1 = colored(word[0], 'grey')
if word[1] == second:
  letter2 = "GREEN"
  slot_2 = "🟩"
  color2 = colored(word[1], 'green')
elif word[1] in wordle:
  letter2 = "LIGHTYELLOW_EX"
  slot_2 = "🟨"
  color2 = colored(word[1], 'yellow')
else:
  letter2 = "LIGHTBLACK_EX"
  slot_2 = "⬛"
  color2 = colored(word[1], 'grey')
if word[2] == third:
  letter3 = "GREEN"
  slot_3 = "🟩"
  color3 = colored(word[2], 'green')
elif word[2] in wordle:
  letter3 = "LIGHTYELLOW_EX"
  slot_3 = "🟨"
  color3 = colored(word[2], 'yellow')
else:
  letter3 = "LIGHTBLACK_EX"
  slot_3 = "⬛"
  color3 = colored(word[2], 'grey')
if word[3] == fourth:
  letter4 = "GREEN"
  slot_4 = "🟩"
  color4 = colored(word[3], 'green')
elif word[3] in wordle:
  letter4 = "LIGHTYELLOW_EX"
  slot_4 = "🟨"
  color4 = colored(word[3], 'yellow')
else:
  letter4 = "LIGHTBLACK_EX"
  slot_4 = "⬛"
  color4 = colored(word[3], 'grey')
if word[4] == fifth:
  letter5 = "GREEN"
  slot_5 = "🟩"
  color5 = colored(word[4], 'green')
elif word[4] in wordle:
  letter5 = "LIGHTYELLOW_EX"
  slot_5 = "🟨"
  color5 = colored(word[4], 'yellow')
else:
  letter5 = "LIGHTBLACK_EX"
  slot_5 = "⬛"
  color5 = colored(word[4], 'grey')
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
realword1 = word[0] + word[1] + word[2] + word[3] + word[4]
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
  #2
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
  slot_10 = "⬛"
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
    copy = str(input(Fore.WHITE + "Copy the results? "))
    if "yes" in copy or "Yes" in copy:
      print(slot_1 + slot_2 + slot_3 + slot_4 + slot_5)
      time.sleep(0.25)
      print(slot_6 + slot_7 + slot_8 + slot_9 + slot_10)
      time.sleep(0.25)
      sys.exit()
    else:
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
#3
if word[0] == first:
  letter1 = "GREEN"
  slot_11 = "🟩"
elif word[0] in wordle:
  letter1 = "LIGHTYELLOW_EX"
  slot_11 = "🟨"
else:
  letter1 = "LIGHTBLACK_EX"
  slot_11 = "⬛"
if word[1] == second:
  letter2 = "GREEN"
  slot_12 = "🟩"
elif word[1] in wordle:
  letter2 = "LIGHTYELLOW_EX"
  slot_12 = "🟨"
else:
  letter2 = "LIGHTBLACK_EX"
  slot_12 = "⬛"
if word[2] == third:
  letter3 = "GREEN"
  slot_13 = "🟩"
elif word[2] in wordle:
  letter3 = "LIGHTYELLOW_EX"
  slot_13 = "🟨"
else:
  letter3 = "LIGHTBLACK_EX"
  slot_13 = "⬛"
if word[3] == fourth:
  letter4 = "GREEN"
  slot_14 = "🟩"
elif word[3] in wordle:
  letter4 = "LIGHTYELLOW_EX"
  slot_14 = "🟨"
else:
  letter4 = "LIGHTBLACK_EX"
  slot_14 = "⬛"
if word[4] == fifth:
  letter5 = "GREEN"
  slot_15 = "🟩"
elif word[4] in wordle:
  letter5 = "LIGHTYELLOW_EX"
  slot_15 = "🟨"
else:
  letter5 = "LIGHTBLACK_EX"
  slot_15 = "⬛"
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
    copy = str(input(Fore.WHITE + "Copy the results? "))
    if "yes" in copy or "Yes" in copy:
      print(slot_1 + slot_2 + slot_3 + slot_4 + slot_5)
      time.sleep(0.25)
      print(slot_6 + slot_7 + slot_8 + slot_9 + slot_10)
      time.sleep(0.25)
      print(slot_11 + slot_12 + slot_13 + slot_14 + slot_15)
      time.sleep(0.25)
      sys.exit()
    else:
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

cls()

#4
if word[0] == first:
  letter1 = "GREEN"
  slot_16 = "🟩"
elif word[0] in wordle:
  letter1 = "LIGHTYELLOW_EX"
  slot_16 = "🟨"
else:
  letter1 = "LIGHTBLACK_EX"
  slot_16 = "⬛"
if word[1] == second:
  letter2 = "GREEN"
  slot_17 = "🟩"
elif word[1] in wordle:
  letter2 = "LIGHTYELLOW_EX"
  slot_17 = "🟨"
else:
  letter2 = "LIGHTBLACK_EX"
  slot_17 = "⬛"
if word[2] == third:
  letter3 = "GREEN"
  slot_18 = "🟩"
elif word[2] in wordle:
  letter3 = "LIGHTYELLOW_EX"
  slot_18 = "🟨"
else:
  letter3 = "LIGHTBLACK_EX"
  slot_18 = "⬛"
if word[3] == fourth:
  letter4 = "GREEN"
  slot_19 = "🟩"
elif word[3] in wordle:
  letter4 = "LIGHTYELLOW_EX"
  slot_19 = "🟨"
else:
  letter4 = "LIGHTBLACK_EX"
  slot_19 = "⬛"
if word[4] == fifth:
  letter5 = "GREEN"
  slot_20 = "🟩"
elif word[4] in wordle:
  letter5 = "LIGHTYELLOW_EX"
  slot_20 = "🟨"
else:
  letter5 = "LIGHTBLACK_EX"
  slot_20 = "⬛"
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
    copy = str(input(Fore.WHITE + "Copy the results? "))
    if "yes" in copy or "Yes" in copy:
      print(slot_1 + slot_2 + slot_3 + slot_4 + slot_5)
      time.sleep(0.25)
      print(slot_6 + slot_7 + slot_8 + slot_9 + slot_10)
      time.sleep(0.25)
      print(slot_11 + slot_12 + slot_13 + slot_14 + slot_15)
      time.sleep(0.25)
      print(slot_16 + slot_17 + slot_18 + slot_19 + slot_20)
      time.sleep(0.25)
      sys.exit()
    else:
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
cls()
#5
if word[0] == first:
  letter1 = "GREEN"
  slot_21 = "🟩"
elif word[0] in wordle:
  letter1 = "LIGHTYELLOW_EX"
  slot_21 = "🟨"
else:
  letter1 = "LIGHTBLACK_EX"
  slot_21 = "⬛"
if word[1] == second:
  letter2 = "GREEN"
  slot_22 = "🟩"
elif word[1] in wordle:
  letter2 = "LIGHTYELLOW_EX"
  slot_22 = "🟨"
else:
  letter2 = "LIGHTBLACK_EX"
  slot_22 = "⬛"
if word[2] == third:
  letter3 = "GREEN"
  slot_23 = "🟩"
elif word[2] in wordle:
  letter3 = "LIGHTYELLOW_EX"
  slot_23 = "🟨"
else:
  letter3 = "LIGHTBLACK_EX"
  slot_23 = "⬛"
if word[3] == fourth:
  letter4 = "GREEN"
  slot_24 = "🟩"
elif word[3] in wordle:
  letter4 = "LIGHTYELLOW_EX"
  slot_24 = "🟨"
else:
  letter4 = "LIGHTBLACK_EX"
  slot_24 = "⬛"
if word[4] == fifth:
  letter5 = "GREEN"
  slot_25 = "🟩"
elif word[4] in wordle:
  letter5 = "LIGHTYELLOW_EX"
  slot_25 = "🟨"
else:
  letter5 = "LIGHTBLACK_EX"
  slot_25 = "⬛"
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
    copy = str(input(Fore.WHITE + "Copy the results? "))
    if "yes" in copy or "Yes" in copy:
      print(slot_1 + slot_2 + slot_3 + slot_4 + slot_5)
      time.sleep(0.25)
      print(slot_6 + slot_7 + slot_8 + slot_9 + slot_10)
      time.sleep(0.25)
      print(slot_11 + slot_12 + slot_13 + slot_14 + slot_15)
      time.sleep(0.25)
      print(slot_16 + slot_17 + slot_18 + slot_19 + slot_20)
      time.sleep(0.25)
      print(slot_21 + slot_22 + slot_23 + slot_24 + slot_25)
      time.sleep(0.25)
      sys.exit()
    else:
      sys.exit()
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
  slot_26 = "🟩"
elif word[0] in wordle:
  letter1 = "LIGHTYELLOW_EX"
  slot_26 = "🟨"
else:
  letter1 = "LIGHTBLACK_EX"
  slot_26 = "⬛"
if word[1] == second:
  letter2 = "GREEN"
  slot_27 = "🟩"
elif word[1] in wordle:
  letter2 = "LIGHTYELLOW_EX"
  slot_27 = "🟨"
else:
  letter2 = "LIGHTBLACK_EX"
  slot_27 = "⬛"
if word[2] == third:
  letter3 = "GREEN"
  slot_28 = "🟩"
elif word[2] in wordle:
  letter3 = "LIGHTYELLOW_EX"
  slot_28 = "🟨"
else:
  letter3 = "LIGHTBLACK_EX"
  slot_28 = "⬛"
if word[3] == fourth:
  letter4 = "GREEN"
  slot_29 = "🟩"
elif word[3] in wordle:
  letter4 = "LIGHTYELLOW_EX"
  slot_29 = "🟨"
else:
  letter4 = "LIGHTBLACK_EX"
  slot_29 = "⬛"
if word[4] == fifth:
  letter5 = "GREEN"
  slot_30 = "🟩"
elif word[4] in wordle:
  letter5 = "LIGHTYELLOW_EX"
  slot_30 = "🟨"
else:
  letter5 = "LIGHTBLACK_EX"
  slot_30 = "⬛"
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
if word == wordle:
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
    copy = str(input(Fore.WHITE + "Copy the results? "))
    if "yes" in copy or "Yes" in copy:
      print(slot_1 + slot_2 + slot_3 + slot_4 + slot_5)
      time.sleep(0.25)
      print(slot_6 + slot_7 + slot_8 + slot_9 + slot_10)
      time.sleep(0.25)
      print(slot_11 + slot_12 + slot_13 + slot_14 + slot_15)
      time.sleep(0.25)
      print(slot_16 + slot_17 + slot_18 + slot_19 + slot_20)
      time.sleep(0.25)
      print(slot_21 + slot_22 + slot_23 + slot_24 + slot_25)
      time.sleep(0.25)
      print(slot_26 + slot_27 + slot_28 + slot_29 + slot_30)
      results = slot_1 + slot_2 + slot_3 + slot_4 + slot_5 + "\n" + slot_6 + slot_7 + slot_8 + slot_9 + slot_10 + "\n" + slot_11 + slot_12 + slot_13 + slot_14 + slot_15 + "\n" + slot_16 + slot_17 + slot_18 + slot_19 + slot_20 + "\n" + slot_21 + slot_22 + slot_23 + slot_24 + slot_25 + "\n" + slot_26 + slot_27 + slot_28 + slot_29 + slot_30
      print("Sadly, REPLIT does not allow the system to directly copy the results, so you will have to do it manually. Select all of the emojis, then right click. After that, hit copy and you should be good to go.")
      pc.copy(results)
    else:
      print("Type Ctrl + Enter")
    
    sys.exit()
else:
    print(word1)
    print(word2)
    print(word3)
    print(word4)
    print(word5)
    print(word6)
    print(Fore.RED + "Uh oh. " + wordle + " was the word")
