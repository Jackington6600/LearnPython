banner = input('Give an input: ')
length = len(banner)

for n in range(0, length + 4):
	print ('#', end="")

print ()
print ("# " + banner + " #")

for n in range(0, length + 4):
	print ('#', end="")