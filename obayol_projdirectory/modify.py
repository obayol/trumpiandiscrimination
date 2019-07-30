import sys

lines = sys.stdin.readlines()

for line in lines:
	a = line.replace('“', '').replace('”', '').lower()
	tokens = a.split()

	if len(tokens) < 1:
		print()
	else:
		print(" " + tokens[0].lstrip(".") + a[len(tokens[0]):].rstrip("\n").rstrip(".").rstrip("?").rstrip("!") + " ")