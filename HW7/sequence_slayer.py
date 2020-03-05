def sequence_slayer(n):
	if n == 0: return 1
	elif n == 1: return 2

	else: return ((n*n*(sequence_slayer(n-1))) - sequence_slayer(n-2))