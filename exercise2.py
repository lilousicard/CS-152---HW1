#CS152 Fall 2022
#Lilou Sicard-Noel
#014122082
#Homework assignment 1
#Exercise 2

def cum_sum(lst, limit=0):
	sum = 0
	index = 0
	if limit > 0:
		for x in lst:
			if(index >= limit):
				break
			sum += x
			index+=1
	else:
		for x in lst:
			sum+=x	
	return sum		
