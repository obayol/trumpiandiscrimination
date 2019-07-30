import sys

lines = sys.stdin.readlines()

arr = []

for line in lines:
	number = ""
	sentiment = ""

	i = 0

	while line[i] != ',':
		number = number + line[i]
		i = i + 1

	i = i + 1

	while line[i] != ',':
		sentiment = sentiment + line[i]
		i = i + 1

	i = i + 1	


	tweet = line[i:].lstrip().rstrip("\n").rstrip().rstrip(",").rstrip(".").rstrip("?").rstrip("!")

	print(number + "," + sentiment + "," + "\"" + tweet + "\"")