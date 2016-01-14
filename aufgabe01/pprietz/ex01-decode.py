''' Usage: python ex01-decode.py ciphertext '''

import sys, math

alphabet = "abcdefghijklmnopqrstuvwxyz"

def validChar(c):
	return c in alphabet

def numForChar(c):
	return alphabet.find(c)

def charForNum(n):
	return alphabet[n]

cipher = sys.argv[1]
key = "chaostreffosnabrueck"
key *= int( math.ceil( float(len(cipher)) / len(key) ))
message = ""

for (i,c) in enumerate(cipher):
	if not validChar(c):
		message += c
		continue
	C_i = numForChar(c)
	K_i = numForChar(key[i])
	M_i = (C_i - K_i) % 26
	message += charForNum(M_i)

print message
