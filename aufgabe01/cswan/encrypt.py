import sys


KEY = 'chaostreffosnabrueck'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(msg):
    encrpyted = []
    index = 0

    for c in msg:
        count = ALPHABET.find(c.lower())

        if count != -1: # if -1 not supported
            count += ALPHABET.find(KEY[index])

            count %= len(ALPHABET)

            encrpyted.append(ALPHABET[count])
            index += 1

            if index == len(KEY):
                index = 0
        else:
            encrpyted.append(c)

    return "".join(encrpyted)


def main():
    print(encrypt(sys.argv[1]))


if __name__ == '__main__':
    main()
