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


def picture():
    j=0
    self.pics.append(self.hang[:])
    for ls in self.man.values():
        pic, j = self.hang[:], 0
        for m in ls:
            pic[2 + j] = m
            j += 1
    self.pics.append(pic)


def print_encrypted_word(word_choosen):
	return list('*'*len(word_choosen))
	

def main():
	print('Welcome to the Hangman game!')
	word_choosen=list(pickwords())
	result=print_encrypted_word(word_choosen)
	print('The word that you have chosen is of length {0} and it is'.format(len(word_choosen)))
	print(result)

main()