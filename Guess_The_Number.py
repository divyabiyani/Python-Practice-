import random

def main():
	nochoosen=random.randint(1,20)
	print('The number selected is between 1 and 20')
	noofguesses=0
	a=-1
	while a!=nochoosen:
		a=int(input('Take a guess!!'))
		if a<nochoosen:
			print('OOPSIE!!Your guess is too low')
			noofguesses+=1;
		elif a>nochoosen:
			print('OOPSIE!!Your guess is too high')
			noofguesses+=1;
		else:
			print('Woopie!! Correct Answer')
			print('It took you {0} attempts to guess the number'.format(noofguesses))

main()