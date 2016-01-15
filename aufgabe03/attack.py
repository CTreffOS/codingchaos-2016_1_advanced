import subprocess
import string
import time

def timingAttack():
	alphabet = string.ascii_uppercase
	length = 100
	exit_code = 2
	while exit_code == 2:
		exit_code = subprocess.call(['crypto' , ' ' * length])
		length = length -1

	length = length + 1

	correct = ''
	for i in range(1, 6):
		t = []
		for letter in alphabet:
			password = correct + letter + '' * (5-i)
			start = time.time()
			subprocess.call(['crypto' , password])
			end = time.time()
			t.append(start-end)
		correct = correct + alphabet[t.index(min(t))]	

	print(correct)

timingAttack()
