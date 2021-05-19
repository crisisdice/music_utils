#import Tkinter
import time
from random import randrange

def main():
	chords = ["A", "C", "D", "E", "G", "Am", "Dm", "Em"]
	cg = ChordGenerator(chords)

	generatedChords = [ cg.display_random_chord() for i in range(100)]
	i = 0
	
	print("starting")

	while(True):
		time.sleep(5)
		print(generatedChords[i])
		i+=1

class ChordGenerator:
	def __init__(self, chords):
		self.chords = chords
		self.lastIndex = 0
		self.nchords = len(chords)
	
	def display_random_chord(self):
		index = randrange(self.nchords)
		
		if(index == self.lastIndex):
			return self.display_random_chord()

		self.lastIndex = index

		return self.chords[index]
