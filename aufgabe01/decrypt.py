import sys
import string

key = [ord(i)-97 for i in 'chaostreffosnabrueck']
word = sys.stdin.readline()[0:-1]
val = [ord(i)-97 for i in word]
out = [string.ascii_lowercase[(val[i]-key[i%len(key)])%26] for i in range(len(word))]
print(out)
