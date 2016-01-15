''' Usage: python ex01-decode.py message '''

import sys, math

alphabet = "abcdefghijklmnopqrstuvwxyz"

def validChar(c):
	return c in alphabet

def numForChar(c):
	return alphabet.find(c)

def charForNum(n):
	return alphabet[n]

message = sys.argv[1]
key = "chaostreffosnabrueck"
key *= int( math.ceil( float(len(message)) / len(key) ))
cipher = ""

for (i,c) in enumerate(message):
	if not validChar(c):
		cipher += c
		continue
	M_i = numForChar(c)
	K_i = numForChar(key[i])
	C_i = (M_i + K_i) % 26
	cipher += charForNum(C_i)

print cipher
