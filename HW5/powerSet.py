def powerSet(input):
	if (len(input) == 0):
		return [[]]
	else:
		main_subset = [ ]
		for small_subset in powerSet(input[1:]):
			main_subset += [small_subset]
			main_subset += [[input[0]] + small_subset]
		return main_subset