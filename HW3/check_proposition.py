def check_proposition(nums):
	
	for x in nums:
		
		if x % 2 == 0:
			status = False
			
			for y in nums:
				
				if y * 2 == x:
					status = True
					break

			if status == False : return False
	return True