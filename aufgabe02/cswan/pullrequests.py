import json
import sys
import urllib.request
import codecs

BASEURL = 'https://api.github.com/repos/$USER/$REPO/pulls?access_token=$TOKEN'
TOKEN = '9d049b7c35bcf4159f7f7a184551f6998545893f'


def main():
    user = sys.argv[1]
    repo = sys.argv[2]

    url = BASEURL.replace('$USER', user).replace('$REPO', repo).replace('$TOKEN', TOKEN)

    reader = codecs.getreader("utf-8")
    res = urllib.request.urlopen(url)
    json_res = json.load(reader(res))

    for row in json_res:
        print("%10d %20s - %s" % (row['id'], row['user']['login'], row['title']))

    return

if __name__ == '__main__':
    main()