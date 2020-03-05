def check_subset(set_a, set_b):
	
	a, b = [], []

	if len(set_a) > len(set_b):
		a, b = set_a, set_b
	else:
		a, b = set_b, set_a

	c = 0
	for i in a:
		for j in b:
			if i == j: c += 1

	if c == len(b): return True
	else: return False

A = [0, 2, 4, 6]
B = [1]
print(check_subset(B, A))