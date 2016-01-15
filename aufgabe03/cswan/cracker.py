import subprocess
import time

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    pw = ''
    rc = -1
    cracked = False
    last_run = -1

    while not cracked:
        cur_char = ''
        for c in ALPHABET:
            start = time.time()
            rc = subprocess.call(['./crypto', pw + c])
            end = time.time()

            cur_run = (end - start) * 1000
            if cur_run > last_run:
                last_run = cur_run
                cur_char = c

            if rc == 0:
                cracked = True
                break

        pw += cur_char
        print("cracking: " + pw)

    print(pw)


if __name__ == '__main__':
    main()