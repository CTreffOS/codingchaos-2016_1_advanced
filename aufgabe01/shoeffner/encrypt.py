import sys
import string

key = [ord(i)-97 for i in 'chaostreffosnabrueck']
word = sys.stdin.readline()[0:-1]
val = [ord(i)-97 for i in word]
out = [string.ascii_lowercase[(key[i%len(key)]+val[i])%26] for i in range(len(word))]

print("".join(out))
