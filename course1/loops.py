# Infinitive loop:
while True:
	userInput = input("Please input positive number: ")
	if float(userInput) > 0:
		print("Your number is: %s" %userInput)
		break
	else: 
		print("%s is wrong nnumber." %userinput)
		continue