import sys

KEY = 'chaostreffosnabrueck'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def decrypt(msg):
    decrypted = []
    index = 0

    for c in msg:
        count = ALPHABET.find(c.lower())

        if count != -1: # if -1 not supported
            count -= ALPHABET.find(KEY[index])

            count %= len(ALPHABET)

            decrypted.append(ALPHABET[count])
            index += 1

            if index == len(KEY):
                index = 0
        else:
            decrypted.append(c)

    return "".join(decrypted)


def main():
    print(decrypt(sys.argv[1]))


if __name__ == '__main__':
    main()
