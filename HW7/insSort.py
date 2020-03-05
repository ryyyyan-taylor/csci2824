def insSort(arr):
	count = 0

	for i in range(1, len(arr)):
		currentNum = arr[i]
		j = i - 1
		while j >= 0:
			count += 1
			if arr[j] > currentNum:
				arr[j+1] = arr[j]
				j -= 1
			else: break
		arr[j+1] = currentNum

	return arr, count