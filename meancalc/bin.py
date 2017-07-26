# An average (mean) calculator.

import sys

def main(numbers):
	total = 0
	for number in numbers:
		total += int(number)
	mean = total / len(numbers)
	print(mean)

if __name__ == '__main__':
	main(sys.argv[1:])
