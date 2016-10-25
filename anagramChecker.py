import numpy as np


FILE_LOC = "/usr/share/dict/words"

class Anagram:

	def __init__(self, minLength = 4) :
		self.minLength = minLength
		
	def loadFile(self):
		self.words = np.loadtxt(FILE_LOC,dtype = 'str')
		self.words = [x.lower() for x in self.words if x.isalpha()]
		print len(self.words)

	def main(self):
		self.loadFile();


if __name__=='__main__' :
	anagramObj = Anagram();
	anagramObj.main();	
    
