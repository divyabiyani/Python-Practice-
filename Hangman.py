import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def pickwords():
	return words[random.randint(0, len(words) - 1)]
	
hang = []
hang.append(' +---+')
hang.append(' |   |')
hang.append('     |')
hang.append('     |')
hang.append('     |')
hang.append('     |')
hang.append('=======')

man = {}
man[0] = [' 0   |']
man[1] = [' 0   |', ' |   |']
man[2] = [' 0   |', '/|   |']
man[3] = [' 0   |', '/|\\  |']
man[4] = [' 0   |', '/|\\  |', '/    |']
man[5] = [' 0   |', '/|\\  |', '/ \\  |']

pics = []

def AllPictures():
	pics.append(hang[:])
	for ls in man.values():
		pic=hang[:]
		j=0
		for m in ls:
			pic[2+j]=m
			j+=1
		pics.append(pic[:])

def print_encrypted_word(word_choosen):
	return list('*'*len(word_choosen))

def printRequiredPic(id):
    for l in pics[id]:
        print(l)
	
def askAndEvaluate(word_choosen, result, missed):
	guess = input()
	if guess==None or len(guess)!=1 or (guess in result) or (guess in missed):
	    return None,False
	i=0
	right=guess in word_choosen
	for c in word_choosen:
		if c==guess:
			result[i]=c
		i+=1
	return guess,right

def main():
	print('Welcome to the Hangman game!')
	word_choosen=list(pickwords())
	result=print_encrypted_word(word_choosen)
	print('The word that you have chosen is of length {0} and it is'.format(len(word_choosen)))
	print(result)
	AllPictures()
	missed=[]
	success=False
	i=0
	printRequiredPic(i)
	while i<len(pics)-1:
		print('Guess The word:')
		guess,right = askAndEvaluate(word_choosen, result, missed)
		if guess==None:
			print('You have already made this choice')
			continue
		print()
		print(result)
		if result==word_choosen:
			print('Congratulations! You have just saved a life.')
			success=True 
			break
		if not right:
			missed.append(guess)
			i+=1
			print('OOPS!Wrong guess {0}'.format(guess))
			printRequiredPic(i)
	if not success:
		print('You are a killer!!')

main()