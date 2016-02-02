import random

def main():
	pname=str(input('Please choose your choice from rock,paper,scissor,lizard and spock:'))
	try:
		pno=rank(pname)
		cno=random.randint(0,4)
		cname=name(cno)
		print('Players choice= {0} \nComputers choice= {1}'.format(pno,cno))
		print('Players choice= {0} \nComputers choice= {1}'.format(pname,cname))
		ans=result(pno,cno)
		if ans==1:
			print('Player Wins!!')
		elif ans==0:
			print('Its a tie!!')
		else:
			print('Computer Wins!!')
	except Exception as e:
		print('Error : {0}'.format(e))

def rank(pname):
	if pname=="rock":
		pno=0
	elif pname=="paper":
		pno=1
	elif pname=="scissor":
		pno=2
	elif pname=="lizard":
		pno=3
	elif pname=="spock":
		pno=4
	return pno

def name(cno):
	if cno==0:
		cname="rock"
	elif cno==1:
		cname="paper"
	elif cno==2:
		cname="scissor"
	elif cno==3:
		cname="lizard"
	elif cno==4:
		cname="spock"
	return cname

def result(pno,cno):
	if pno==cno:
		return 0
	elif pno==2 and cno==1 or pno==2 and cno==3:
		return 1
	elif pno==1 and cno==0 or pno==1 and cno==4:
		return 1
	elif pno==0 and cno==3 or pno==0 and cno==2:
		return 1
	elif pno==3 and cno==4 or pno==3 and cno==1:
		return 1
	elif pno==4 and cno==2 or pno==4 and cno==0:
		return 1
	else:
		return -1

main()