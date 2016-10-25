import numpy as np
import itertools


FILE_LOC = "/usr/share/dict/words"

class Anagram:

	def __init__(self, minLength = 4) :
		self.minLength = minLength
		
	def loadFile(self):
		self.words = np.loadtxt(FILE_LOC,dtype = 'str')
		self.words = [x.lower() for x in self.words if x.isalpha()]
		#print len(self.words)


	def formAnagram(self):
		data = [x for x in self.words if len(x)==self.minLength]
		for ele in data:
			anagramWords = list(map("".join,itertools.permutations(ele,self.minLength)))
			anagramWords = set(anagramWords);
			self.checkAnagram(anagramWords,data);

	def checkAnagram(self,wordlist,dictionary):
		anagramList = []
		for entry in wordlist:
			if entry in dictionary:
				anagramList.append(entry)
		if len(anagramList) >= self.minLength:
			print anagramList

	def main(self):
		self.loadFile()
		#print len(self.words)
		maxLen = len(max(self.words,key = len))
		#print maxLen
		while(self.minLength <= maxLen):
			print "---------------"+str(self.minLength)+"----------------------"
			self.formAnagram()
			self.minLength += 1
			#break


if __name__=='__main__' :
	anagramObj = Anagram()
	anagramObj.main()
    
