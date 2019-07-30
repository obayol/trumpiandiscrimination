import sys

with open("results/naivebayes.csv") as nb:
	nbLines = nb.readlines()

with open("results/randomforest.csv") as rf:
	rfLines = rf.readlines()

with open("results/svm.csv") as svm:
	svmLines = svm.readlines()

with open("results/1layerneuralnet.csv") as nn:
	nnLines = nn.readlines()

with open("trumptweets.txt") as tweets:
	tweetLines = tweets.readlines()

while True:
	phrase = raw_input("Enter phrase to look for: ")

	nbPos = 0
	nbNeg = 0
	rfPos = 0
	rfNeg = 0
	svmPos = 0
	svmNeg = 0
	nnPos = 0
	nnNeg = 0

	for i in range(len(tweetLines)):
		if phrase in tweetLines[i]:
			if int(nbLines[i].split(",")[1]) == 1:
				nbPos = nbPos + 1
			else:
				nbNeg = nbNeg + 1

			if int(rfLines[i].split(",")[1]) == 1:
				rfPos = rfPos + 1
			else:
				rfNeg = rfNeg + 1

			if int(svmLines[i].split(",")[1]) == 1:
				svmPos = svmPos + 1
			else:
				svmNeg = svmNeg + 1

			if int(nnLines[i].split(",")[1]) == 1:
				nnPos = nnPos + 1
			else:
				nnNeg = nnNeg + 1

	print("Naive Bayes: " + str((float(nbPos)/float(nbPos + nbNeg))*100) + "% " + "Positive, " + str((float(nbNeg)/float(nbPos + nbNeg))*100) + "% Negative")
	print("Random Forest : " + str((float(rfPos)/float(rfPos + rfNeg))*100) + "% " + "Positive, " + str((float(rfNeg)/float(rfPos + rfNeg))*100) + "% Negative")
	print("SVM: " + str((float(svmPos)/float(svmPos + svmNeg))*100) + "% " + "Positive, " + str((float(svmNeg)/float(svmPos + svmNeg))*100) + "% Negative")
	print("Multi-Layer Perceptron: " + str((float(nnPos)/float(nnPos + nnNeg))*100) + "% " + "Positive, " + str((float(nnNeg)/float(nnPos + nnNeg))*100) + "% Negative")
	print