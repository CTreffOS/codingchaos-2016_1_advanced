import sys
import struct
import numpy as np
import scipy
import math


with open(sys.argv[1]) as file:
	data = file.read()
	file.seek(0,2)
	size = file.tell()
	converted = struct.unpack("<{}h".format(int(size/2)), data)


arr = np.array(converted)

padding = math.ceil(float(arr.size)/45)*45 - arr.size
arr = np.append(arr, np.zeros(padding)*np.NaN)
reshaped = scipy.nanmean(arr.reshape(-1,45), axis=1)

reshaped = reshaped / (2.0**16)
reshaped = reshaped * 255

pbm = np.zeros((1000,255))
for i in range(1000):
	for j in range(255):
		if np.abs(reshaped[i]) < j:
			pbm[i][j] = 1

with open('test.pbm','w') as file:
	file.write('P1\n')
	file.write('255 1000\n')
	for i in range(1000):
		file.write(str(pbm[i,:]) + '\n')



