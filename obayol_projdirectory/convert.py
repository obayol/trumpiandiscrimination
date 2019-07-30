import sys

lines = sys.stdin.readlines()

for line in lines:
	id = ""

	i = len(line) - 1

	while i >= 0:
		if line[i] != ',':
			id = id + line[i]
		else: 
			break
		i = i - 1

	id = id.replace("\n", "")

	reversed = ""

	j = len(id) - 1

	while j >= 0:
		reversed = reversed + id[j]
		j = j - 1

	print(reversed + "," + line[0:i])