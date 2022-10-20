#CS152 Fall 2022
#Lilou Sicard-Noel
#014122082
#Homework assignment 1
#Exercise 1 

def select_company(state, salary):
	if state == "Texas" or state == "New Mexico" or state == "Arizona":
		return False
	if state == "California" or state == "Oregon" or state == "Washington":
		return salary >= 80000
	else:
		return salary >= 100000

if __name__ == '__main__':
	print(select_company("California",90000))
	print(select_company("Texas",190000))
	print(select_company("Caa",90000))
