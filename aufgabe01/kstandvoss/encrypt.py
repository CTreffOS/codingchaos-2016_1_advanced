
import sys

def encrypt(text):
	key = 'chaostreffosnabrueck'
	alphabet = {0 : 'a', 1 : 'b',2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11:'l' , 12:'m', 13:'n' ,14:'o' ,15:'p' , 16:'q' , 17:'r' , 18:'s' , 19:'t' , 20:'u' , 21:'v', 22:'w', 23:'x' ,24:'y', 25:'z'}
	reverse =  {value: key for key, value in alphabet.items()}
	code = ''
	for i,letter in enumerate(text):
		offset = reverse[key[i % len(key)]]
		if not letter in reverse:
			code = code + letter
		else:	
			place = reverse[letter]
			code = code + alphabet[(offset+place) % 26]
	return code
	

text = sys.argv[1]
print(encrypt(text))		 