# Simple utility to encode files in base64.

import sys
import argparse
import base64

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
	parser = argparse.ArgumentParser()
	parser.add_argument('file', help='The path to the file you want to manipulate')
	parser.add_argument('method', help='What to do with the file (encode, decode)')
	args = parser.parse_args(sargs)
	
	try:
		opened = open(args.file, "r")
	except:
		print(Red("FATAL") + ": File does not exist!")
		sys.exit()
		
	content = opened.read()
	opened.close()
	
	if args.method == "encode":
		converted = str(base64.b64encode(bytes(content.encode("utf-8"))))[2:-1]
	elif args.method == "decode":
		converted = str(base64.b64decode(bytes(content.encode("utf-8"))))[2:-1]
	else:
		print(Red("ERROR") + ": Unrecognized method '"+Orange(args.method)+"'")
		sys.exit()
	
	opened = open(args.file, "w")
	opened.write(converted)
	opened.close()
	
	print(Green("SUCCESS") + ": File "+args.method+"d!")

if __name__ == '__main__':
	main(sys.argv[1:])