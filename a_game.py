import random

hand = ['R','P','S']
win = { 'R':'S','S':'P','P':'R'}
lose = { 'R':'P','P':'S','S': 'R' }
score = {'U':0,'C':0}
hand_freq = { 'R' : 0.0,'P' : 0.0,'S' : 0.0}
hand_R = hand_freq.copy()
hand_P = hand_freq.copy()
hand_S = hand_freq.copy()
hand_dummy = hand_freq.copy()
hand_RPS = {'R' : hand_R, 'P' : hand_P, 'S' : hand_S, 'D' : hand_dummy}

w_RPS = hand_freq.copy()

x = random.randint(0,1000)
C = hand[x%3]
U_p = 'D'
print """
	++++++++      ++++++++     ++++++
	++     ++     ++     ++   ++     
	+++++++       +++++++      ++++++
	++     ++     ++                ++
	++      ++    ++           ++++++
	   ROCK		PAPER 	  SCISSORS
	"""
print "PLEASE TURN ON CAPSLOCK FOR BETTER GAMING EXPERIANCE"
print "ENTER R FOR ROCK, P FOR PAPER, S FOR SCISSORS\n\n\n"
while True:
	#print '   ',hand_freq,"\n"
	#for i in hand:
	#	print i,':',hand_RPS[i],"\n"
	#print '   ',w_RPS,"\n"
	while True:
		U = str(raw_input("YOU  :  "))
		if U in hand:
			break
	print "CPU  : ", C
	hand_RPS[U_p][U] += 1
	U_p = U
	hand_freq[U] += 1
	if win[U] == C:
		score['U'] += 1
	elif win[C] == U:
		score['C'] += 1
	print "USER : ",score['U']," COMPUTER : ",score['C']
	w_RPS = hand_freq.copy()
	w_max =  max( w_RPS.values())
	hand_max =  max(hand_RPS[U_p].values())
	if w_max == 0:
		w_max = 1
	if hand_max == 0:
		hand_max = 1
	for i in hand:
		w_RPS[i] /= w_max
		w_RPS[i] *= 1
		w_RPS[i] +=1 *hand_RPS[U_p][i]/hand_max
	C = lose[max(w_RPS, key = w_RPS.get)]

