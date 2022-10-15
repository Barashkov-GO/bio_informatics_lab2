import random

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'


def generate_test(n):
    global alphabet
    str1 = ''
    str2 = ''
    for i in range(n):
        str1 += alphabet[random.randint(0, len(alphabet) - 1)]
        str2 += alphabet[random.randint(0, len(alphabet) - 1)]

    return str1, str2


def main():
    f = open('tests/2.fasta', 'w')
    for i in range(1, 100):
        t1, t2 = generate_test(i * 10)
        f.write(t1 + '\n')
        f.write(t2 + '\n')

    f.close()


if __name__ == '__main__':
    main()
