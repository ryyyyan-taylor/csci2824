def ABCs(letters, numbers):

	vowels = ['A','E','I','O','U']

	for letter, number in zip(letters, numbers):
		even = False
		vowel = False

		if letter in vowels: vowel = True
		if number % 2 == 0: even = True

		if even == True and vowel == False:
			return False

	return True