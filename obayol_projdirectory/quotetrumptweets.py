import sys

lines = sys.stdin.readlines()

for line in lines:
	i = 0
	num = ""

	while i < len(line) and line[i] != ',':
		num = num + line[i]
		i = i + 1

	i = i + 1

	tweet = line[i:].rstrip("\n")

	print(num + "," + "\"" + tweet + "\"") 
