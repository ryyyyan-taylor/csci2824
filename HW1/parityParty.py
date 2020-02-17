def ParityParty(d):
	out = []
	if d % 2 == 0: 
		out.append(0)
		out.append(int(d / 2))
	else:
		out.append(1)
		out.append(int((d - 1) / 2))

	return out

sample = ParityParty(9)
print(sample)