import sys, urllib2, json, base64, textwrap


baseurl = " https://api.github.com/"
repoapi = lambda owner, repo: baseurl+"repos/"+owner+"/"+repo+"/pulls?state=open"

token = "adc0b0cb90e62ea1a966c17671dbdd1895e7c28c"
user = sys.argv[1]
repo = sys.argv[2]


req  = urllib2.Request(repoapi(user,repo))

base64string = base64.encodestring('%s:%s' % (user, token))[:-1]
req.add_header("Authorization", "Basic %s" % base64string)

resp = urllib2.urlopen( req ).read()
data = json.loads(resp)

for pullreq in data:
	msg = textwrap.wrap(pullreq["body"], 80)
	if len(msg) > 1:
		for (i,m) in enumerate(msg):
			if i == 0:
				print u'{:>0}  {:>15}  {:>15}'.format(str(pullreq["id"]), pullreq["user"]["login"], m)
			else:
				print u'{:>0}  {:>23}  {:>20}'.format("","",m)
	else:
		print u'{:>0}  {:>15}'.format(str(pullreq["id"]), pullreq["user"]["login"])

