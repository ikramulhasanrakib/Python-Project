import random

print("Hi! What's your name?")
name = input()
print(f"Hello {name}!  Let's play a game")
secret_num = random.randint(1,20)
for i in range(0,6):
	print("Guess a number from 1 to 20 : ")
	try:
		num = int(input())
		if num > secret_num:
			print("Huh! Your guess is too high.")
		elif num < secret_num:
			print("Huh! Your guess is too low.")
		else:
			print("Well Done! You are right.")
			break
	except:
		print("Invalid number.Please try again")

if num == secret_num:
	print(f"You guessed the correct answer with {i+1} attempts")
else:
	print(f"You missed it! The number was {secret_num}")
print("Thanks for playing")
	