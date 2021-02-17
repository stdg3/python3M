import random

randInt = random.randint(0,100)
while True:
	guess = int(input("guess [0,100]"))
	if(guess < randInt):
		print("daha büyük dene")
	elif(guess > randInt):
		print("daha küçük dene")
	elif(guess == randInt):
		print("Correct!!!!!!!")
		break
	else:
		print("input num 0-100")
