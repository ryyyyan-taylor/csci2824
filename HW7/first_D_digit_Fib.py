def first_D_digit_Fib(d):
	numCur = 1
	numPre = 1
	while True:
		if len(str(numCur)) >= d: return numCur
		numCur, numPre = numCur + numPre, numCur