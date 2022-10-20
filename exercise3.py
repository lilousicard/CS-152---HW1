#CS152 Fall 2022
#Lilou Sicard-Noel
#014122082
#Homework assignment 1
#Exercise 3

def factorial(n):
	if n < 1:
		return -1
	result = 1
	for i in range(1,n+1):
		result*=i
	return result

if __name__ == '__main__':
	print(factorial(5))
	print(factorial(1))
	print(factorial(3))
	print(factorial(-7))

