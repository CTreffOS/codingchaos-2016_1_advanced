import subprocess, time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def timing(known,letter,pos):
	test = list(known)
	test[pos] = letter
	test = "".join(test)
	start = time.time()
	subprocess.call(["../crypto", test])
	t = time.time() - start
	return t

# check password length
rc = 0
checkstr = ""
while rc < 2:
	checkstr += " "
	rc = subprocess.call(["../crypto", checkstr])

pwlen = len(checkstr)-1

# timingattack
test = [" "]*pwlen
for i in range(0,pwlen):
	run = [None]*len(alphabet)
	for (j,c) in enumerate(alphabet):
		run[j] = timing("".join(test),c,i)
	#print run
	charindex = run.index(max(run))
	test[i] = alphabet[charindex]

print "".join(test)