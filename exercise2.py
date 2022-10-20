#CS152 Fall 2022
#Lilou Sicard-Noel
#014122082
#Homework assignment 1
#Exercise 2

def cum_sum(lst, limit=0):
	sum = 0
	if limit > 0:
		for x in range(limit):
			sum += x
	else:
		for x in lst:
			sum+=x	
	return sum		
