res = [ ele for ele in alphabet ]
for a in letters:
  if a in alphabet:
	  res.remove(a)
listToStr = ' '.join([str(elem) for elem in res])
  
print(Fore.WHITE + listToStr) 
print(word1)
if word != wordle: