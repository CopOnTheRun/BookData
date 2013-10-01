import re

wordex = re.compile(r"\b\w+[’']?\w*\b") #note the difference between ’ and '.

def wordList(string):
	return re.findall(wordex,string)

def wordSet(string):
	return set(re.findall(wordex,string))

def uWordSet(string):
	return {word.lower() for word in wordSet(string)}


def wordCount(wList):
	wordDict = {}
	for word in wList:
		if word.lower() in wordDict:
			wordDict[word.lower()]+=1
		else:
			wordDict[word.lower()]=1
	return wordDict

def toTSV(wDict,fileName):
	with open(fileName,'w') as f:
		f.write('Word\tFrequency\n')
		for word in wDict:
			f.write('{}\t{}\n'.format(word,wDict[word]))
