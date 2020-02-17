def DecToBin(d):
	
	out = []

	if d == 0 or d == 1:
		out.append(d)
		return out

	else:
		while d >= 1:
			if d % 2 == 0:
				out.insert(0, 0)
				d = d / 2
				continue

			else:
				out.insert(0, 1)
				d = (d - 1) / 2

	return out


sample = DecToBin(241)
print(sample)