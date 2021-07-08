import random
file = open("words.txt", 'r')
k = file.read()

words = k.split(' ')

# If you put in more words try this to remove any duplicate words.
# k = k.replace("\n",' ')
# k = list(set(k.split(" ")))
# k = " ".join(k)

def search():
	search = []
	for m in range(random.randint(1,4)):
		search.append(words[random.randint(0,len(words)-1)])
	return " ".join(search)

