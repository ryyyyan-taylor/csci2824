def WhoWins(Jedi, LSColors, Heights):
	if len(Jedi) != len(LSColors) or len(Jedi) != len(Heights) or len(Heights) != len(LSColors):
		print("Error! Vector Length mismatch")
		return

	for i in range(len(Jedi)):
		for j in range(len(Jedi)):
			winner = 'a tie'

			if LSColors[i] == 'Purple' or Heights[i] > Heights[j]:
				winner = Jedi[i]
			if LSColors[j] == 'Purple' or Heights[j] > Heights[i]:
				winner = Jedi[j]

			# only 4 comparisons in each loop
			print('For', Jedi[i], ' against', Jedi[j], ', the winner is', winner)