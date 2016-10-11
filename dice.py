running = True;
from random import randint

print("Welcome to Dice Roller!")
print("Type 'quit' to quit.")
print("Type 'ydx' where x and y are integers")

while running:
	
	i = input()
	
	if "d" in i:
		diceQuant = int(i.split('d', 1)[0])
		diceType = int(i.rsplit('d', 1)[1])
		
		n=0
		
		for x in range(0, diceQuant):
			n = n + randint(1, diceType)
		
		print(n)
		
	if i == "quit":
		running = False
		