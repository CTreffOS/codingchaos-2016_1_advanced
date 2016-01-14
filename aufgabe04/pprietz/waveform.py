import sys, struct
import numpy as np

inputfile = sys.argv[1]
outputfile = sys.argv[2]

data = []

with open(inputfile) as f:
	f.seek(0,2)
	size = f.tell()/2
	f.seek(0)
	data = struct.unpack("<{}h".format(size),f.read()) # thanks basti

data = np.abs( list(data) )
idx = np.floor( np.linspace(0,len(data),1002) ).astype(int)
scaled = [None]*len(idx)
for i in range(1,len(idx)-1):
	scaled[i] = np.max( data[ idx[i]:idx[i+1] ] )

scaled = np.array(scaled[1:-1]).astype(float)
max_val = np.max(scaled)
scaled = (scaled/max_val*256).astype(int)

pixels = np.zeros((256,len(scaled)))
for i in range(len(scaled)):
	val = scaled[i]
	pixels[:val,i] = 1

with open(outputfile,'w') as f:
	f.write("P1\n")
	f.write("1000 256\n")
	for i in range(256):
		f.write(pixels[i,:].tostring()+"\n")