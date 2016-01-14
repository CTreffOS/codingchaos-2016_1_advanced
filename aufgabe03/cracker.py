from subprocess import call
import time

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    pw = ''
    rc = -1
    last_run = -1

    while True:
        cur_char = ''
        for c in ALPHABET:
            start = time.time()
            rc = call(['./crypto', pw + c])
            end = time.time()

            if rc == 0:
                return

            cur_run = (end - start) * 1000
            if cur_run > last_run:
                last_run = cur_run
                cur_char = c

        pw += cur_char
        print("PW: " + pw)


if __name__ == '__main__':
    main()