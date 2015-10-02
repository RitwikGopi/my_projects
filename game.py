import random

hand = ['R','P','S']
win = { 'R':'S','S':'P','P':'R'}
score = {'U':0,'C':0}

while True:
	x = random.randint(0,1000)
	C = hand[x%3]
	U = str(raw_input("RPS! : "))
	print C
	winner = ''
	if win[U] == C:
		score['U'] += 1
	elif win[C] == U:
		score['C'] += 1
	print "USER : ",score['U']," COMPUTER : ",score['C']

