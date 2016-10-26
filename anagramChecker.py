import numpy as np
import itertools
import string
import collections
import time

FILE_LOC = "/usr/share/dict/words"


class Anagram:
	"""An implementation to check anagrams in a dictionary"""

	def __init__(self, minLength = 4) :
		self.minLength = minLength

	def hashmap(self):
		"""
		A hashmap function where each aplhabet is mapped to a prime number.

		hashFn is a dictionary with the aplhabets as key and the prime number as value

		"""
		primeVal = [2]
		ele = 3
		while len(primeVal) < 26:
			result = []
			for n in primeVal:
				result.append(ele % n)
			if 0 not in result:
				primeVal.append(ele)
			ele += 2
		#print primeVal
		charVals = list(string.ascii_lowercase)
		self.hashFn = dict(zip(charVals,primeVal));
		#print self.hashFn

	def getHashVal(self,word):
		"""
		Method to return the hash value of a word. returns the product of hash value of the each 
		characters in the word.

		Parameters:
		----------
		word : a string with only aplhabets

		"""
		chars = list(word)
		keyval = 1
		for c in chars:
			keyval *= self.hashFn[c]
		return keyval

	def loadFile(self):
		"""
		Load dictionary from the location specified in FILE_LOC

		"""
		self.words = np.loadtxt(FILE_LOC,dtype = 'str')
		self.words = [x.lower() for x in self.words if x.isalpha()]
		#print len(self.words)


	def formAnagram(self):
		"""
		Method to check anagrams

		"""
		data = [x for x in self.words if len(x)==self.minLength]
		data = np.unique(data)
		#hashedData = map(lambda x:[x,self.getHashVal(x)],data)
		hashedData = map(lambda x: self.getHashVal(x),data)
		#hashVals = [x[1] for x in hashedData]
		hashedData, data = zip(*sorted(zip(hashedData, data)))
		sortedHash = np.unique((hashedData))
		#sortedHash = np.unique((hashVals))
		hashedData = list(hashedData)
		data = list(data)
		for ele in sortedHash:
			ans = []
			while ele in hashedData:
				index = hashedData.index(ele)
				ans.append(data[index])
				hashedData.remove(ele)
				data.remove(data[index])
			if len(ans) >= self.minLength :
				 for p in ans: print p + ',',
				 print
		
		'''x = []
		for ele in hashedData:
			if hashedData.count(ele) >= self.minLength:
				x.append(ele)'''
		#print hashedData
		'''print len(hashedData)
		l = list(hashedData[1])
		for ele in sortedHash:
			l = [ x for x in hashedData if x[1] == ele  ]
			if len(l) >= self.minLength:
				for p in l: print p[0] + ',',
				print
		'''


	def main(self):
		self.loadFile()
		self.hashmap()
		print len(self.words)
		maxLen = len(max(self.words,key = len))
		print maxLen
		while(self.minLength <= maxLen):
			#print "---------------"+str(self.minLength)+"----------------------"
			self.formAnagram()
			self.minLength += 1
			#break




if __name__=='__main__' :
	#start_time = time.time()
	anagramObj = Anagram()
	anagramObj.main()
	#print("--- %s seconds ---" % (time.time() - start_time))    
