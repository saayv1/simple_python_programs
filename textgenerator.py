"""This is a text generator which can generate 3 alphabet words with or without any meaning to it"""

#@author Vyaas N Shenoy


import string,random

vowels = "aeiou"

consonants = string.ascii_lowercase

vlist = list(vowels)

for c in vlist:
	consonants = consonants.replace(c,"")

ip1 = raw_input("If you want a vowel for the first letter, enter v. If you want a consonant for the first letter enter c and if you want any letter insert \\ then the letter you want\t")

ip2 = raw_input("If you want a vowel for the first letter, enter v. If you want a consonant for the first letter enter c and if you want any letter insert \\ then the letter you want\t")

ip3 = raw_input("If you want a vowel for the first letter, enter v. If you want a consonant for the first letter enter c and if you want any letter insert \\ then the letter you want\t")

#vowels = "aeiou"
def generator():
	if ip1 == 'c':
		letter1 = random.choice(consonants)
	elif ip1=='v':
		letter1 = random.choice(vowels)
	elif "\\" in ip1:
		letter1 = ip1[1]
	if ip2 == 'c':
		letter2 = random.choice(consonants)
	elif ip2 == 'v':
		letter2 = random.choice(vowels)
	elif "\\" in ip2:
		letter2 = ip2[1]
	else :
		letter2 = ip2

	if ip3=='c':
		letter3 = random.choice(consonants)
	elif ip3=='v':
		letter3 = random.choice(vowels)
	elif "\\"  in ip3:
		letter3 = ip3[1]
	else:
		letter3 = ip3
	name = letter1+letter2+letter3
	return(name)

name = generator()


for i in range(20):
	print(generator())
