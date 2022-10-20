#CS152 Fall 2022
#Lilou Sicard-Noel
#014122082
#Homework assignment 1
#Exercise 4


def multiple_factorials(n):
	dict = [1]
	if n<1:
		return -1
	answer = 1
	for i in range(2,n+1):
		answer*=i
		dict.append(answer)
	dict.reverse()
	for x in dict:
		print(x)

if __name__ == '__main__':
	multiple_factorials(10)
