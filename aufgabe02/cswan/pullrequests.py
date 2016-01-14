import json
import sys
import urllib.request
import codecs
import configparser

BASEURL = 'https://api.github.com/repos/$USER/$REPO/pulls?access_token=$TOKEN'


def main():
    user = sys.argv[1]
    repo = sys.argv[2]

    config = configparser.RawConfigParser(allow_no_value=True)
    config.read('config.cfg')
    url = BASEURL.replace('$USER', user).replace('$REPO', repo).replace('$TOKEN', config['default']['token'])

    reader = codecs.getreader("utf-8")
    res = urllib.request.urlopen(url)
    json_res = json.load(reader(res))

    for row in json_res:
        print("%10d %20s - %s" % (row['id'], row['user']['login'], row['title']))

    return

if __name__ == '__main__':
    main()