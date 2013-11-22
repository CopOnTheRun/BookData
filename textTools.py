#!/usr/bin/python3

import re
import os
import sys

wordex = re.compile(r"\w+[’']?\w*") #note the difference between ’ and '.
sWords = {'a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your'}

"""Creates an ordered list of the words in a string of text"""
def wordList(string):
	return [match.group().lower() for match in re.finditer(wordex,string)]

"""Creates a set from a string. """
def wordSet(string):
	return set(wordList(string))

"""Creates a dictionary from a word list. The key to each entry is a unique word, and the value is a list of occurences of the key."""
def wordDict(wList):
	wordDict = {}
	for num,word in enumerate(wList,1):
		if word in wordDict:
			wordDict[word].append(num)
		else:
			wordDict[word]=[num]
	return wordDict

def toTSV(wDict,fileName,stopWords={}):
	with open(os.path.join('Data',fileName+'.tsv'),'w') as f: #output goes in "Data" directory
		f.write('Word\tFrequency\tLocation(s)\n')
		for word in wDict:
			if word not in stopWords:
				f.write('{0}\t{1}\t{2}\n'.format(word,len(wDict[word]),wDict[word]))

def textToTSV(fileName,stopWords={}):
	with open(fileName) as inF:
		wDict = wordDict(wordList(inF.read()))
	outFile = os.path.split(fileName)[1]
	toTSV(wDict,outFile,stopWords)

def main():
	import argparse

	parser = argparse.ArgumentParser(description="Turn a text file into a tab delimited file containg the words and position in which they appeared in the original file.")

	parser.add_argument(
		"InFile",
		help="file to be read",
		type=str)

	parser.add_argument(
		"-s",
		"--stopwords",
		help="setting this flag will remove common stopwords",
		action="store_true")

	args=parser.parse_args()

	if args.stopwords:
		textToTSV(args.InFile,sWords)
		print("Stopwords used")
	else:
		textToTSV(args.InFile)
		print("Stopwords not used")

if __name__ == '__main__':
	main()
