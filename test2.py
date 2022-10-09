
def fix(word):
    s = set()
    list = []
    for ch in word:
        if ch not in s:
            s.add(ch)
            list.append(ch)
    return ''.join(list)        
word = input("")
wordl = fix(word)
# initialize lists
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letters = list(wordl)
res = [ ele for ele in alphabet ]
for a in letters:
  if a in alphabet:
	  res.remove(a)
complete = res + [word[0], word[1], word[2], word[3],word[4]]
complete.sort()
def listToString(complete):
	str1 = " "
	return (str1.join(s))
s = complete
print(listToString(complete))
