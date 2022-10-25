import random
import time

def progress_bar(current=0, total=55, width=25):
	# bar = chr(9608)
	bar = '='
	current = total if current > total else current
	percentComplete = round(current / total * 100)
	
	barCount = int(current / total * width)
	barStr = f'[ {bar * barCount} {" " * (width-barCount)}] {str(percentComplete)}% ({str(current)} of {str(total)})'
	print(barStr, end='', flush=True)
	print('\b' * len(barStr), end='', flush=True)


if __name__ == '__main__':
	current = 0
	total = 100
	width = 35
	while current < total:
		current += random.randint(1, 3)
		progress_bar(current, total, width)
		time.sleep(0.3)