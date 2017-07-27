# This is just an example template. You can change this all you like.

import sys
import os

class ansi:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	ORANGE = '\033[93m'
	RED = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def Orange(text):
	return ansi.ORANGE+text+ansi.ENDC
def Green(text):
	return ansi.GREEN+text+ansi.ENDC
def Red(text):
	return ansi.RED+text+ansi.ENDC

def main(sargs):
	DCOUNT = 0
	dir_path = os.getcwd()
	TOTAL = 0
	for item in os.listdir(dir_path):
		if os.path.isfile(dir_path+"/"+item):
			ask = input("Delete "+Orange(item)+"? (y,n): ")
			if ask.lower() == "y":
				print(Red("Deleting..."))
				os.remove(item)
				DCOUNT += 1
			elif ask.lower() == "n":
				pass
			else:
				print("Unknown command, skipping...")
			TOTAL += 1
				
	print(Red(str(DCOUNT))+"/"+Orange(str(TOTAL))+" deleted ("+str((DCOUNT/TOTAL)*100)+"%)")

if __name__ == '__main__':
	main(sys.argv[1:])