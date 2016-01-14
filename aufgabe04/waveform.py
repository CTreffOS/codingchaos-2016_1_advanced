import sys
import os
import struct
from numpy import *

audio = sys.argv[1]
bild = sys.argv[2]

with open(audio, 'rb') as f:
    totalBytes = os.path.getsize(audio)
    print(totalBytes)
    values = empty(totalBytes/2)
    for i in range(len(values)):
        values[i] = struct.unpack('<h', f.read(2))[0]

print(len(values))

x = len(values) / (1000)
print(x)

newvalues = empty(1000)

k = 0
for i in range(0,len(values)):
    if values[i] < 0:
         values[i] *= -1


for i in values:
    if i < 0:
        print(i)

print(values)

for i in range(0,1000):
    newvalues[i] = mean(values[x * i:x * (i+1)])

text_file = open("Output.pbm", "w")

text_file.write('P1\n')
text_file.write('1000 255\n')
for i in range(0,255):
    for j in range(0,1000):
        # print("newvalue",  newvalues[j])
        # print("i: ",  i * 65536 / 255)
        scale = 255.0 / 65536.0
        if newvalues[j] > (i * 65536 / 255):
            text_file.write('1 ')
        else:
            text_file.write('0 ')

text_file.close()



