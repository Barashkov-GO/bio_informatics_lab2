import sys


def max_3(a, b, c):
    # Максимум из трех элементов
    res = a
    if b > res:
        res = b
    if c > res:
        res = c
    return res


def fill(a, b, g, match, mismatch):
    # Заполнение всей матрицы, но хранятся 2 массива (предыдущая и текущая строки)
    # data = []
    print(a, b, g, match, mismatch)
    res = [0] * (len(b) + 1)
    prev = [-float('inf')] * (len(b) + 1)
    for i in range(len(a) + 1):
        res[0] = i * g
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                res[j] = max_3(prev[j - 1] + match, prev[j] + g, res[j - 1] + g)
            else:
                res[j] = max_3(prev[j - 1] + mismatch, prev[j] + g, res[j - 1] + g)
        # data.append([])
        for k in range(len(prev)):
            prev[k] = res[k]
            # data[-1].append(res[k])
    return res[-1]


def fill_k(a, b, g, match, mismatch, k):
    # Заполнение по одной полосе ширины k, хранятся 2 массива
    # print(a, b, g, match, mismatch, k)
    res = [0] * (len(b) + 1)
    prev = [-float('inf')] * (len(b) + 1)
    for i in range(len(a) + 1):
        res[0] = i * g
        for j in range(i - k if i >= k else 1, i + k + 1 if i + k < len(b) + 1 else len(b) + 1):
            # идем циклом только по заданной полосе
            if a[i - 1] == b[j - 1]:
                res[j] = max_3(prev[j - 1] + match, prev[j] + g, res[j - 1] + g)
            else:
                res[j] = max_3(prev[j - 1] + mismatch, prev[j] + g, res[j - 1] + g)
        # data.append([])
        for k in range(len(prev)):
            # копирование списков
            prev[k] = res[k]
            # data[-1].append(res[k])

    return res[-1]


def read(path):
    # чтение из файла
    res = []
    f = open(path, 'r')
    lines = f.readlines()

    res_2 = []
    for line in lines:
        if len(res_2) < 2:
            res_2.append(line.replace("\n", ''))
        if len(res_2) == 2:
            res.append(res_2)
            res_2 = []

    f.close()
    return res


def read_args():
    # обработка аргументов командной строки
    path = ''
    gap = 3
    match = 4
    mismatch = 5
    k = 3
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-i':
            path = sys.argv[i + 1]
        elif sys.argv[i] == '-g':
            gap = float(sys.argv[i + 1])
        elif sys.argv[i][0:5] == '--gap':
            gap = float(sys.argv[i][6:])
        elif sys.argv[i] == '-m':
            match = float(sys.argv[i + 1])
        elif sys.argv[i] == '-mm':
            mismatch = float(sys.argv[i + 1])
        elif sys.argv[i] == '-k':
            k = int(sys.argv[i + 1])
    return path, gap, match, mismatch, k


# Примеры запусков
#   python3 main.py -i 1.fasta --gap=-6 -m 5 -mm -1 -k 3
#   python3 main.py -i 2.fasta -g -6 -m 5 -mm -1 -k 3
def main():
    test_fasta_path, gap, match, mismatch, k = read_args()
    pairs = read('tests/' + test_fasta_path)

    for pair in pairs:
        # проход по всем парам строк
        print('TESTING...')
        d0 = fill(pair[0], pair[1], gap, match, mismatch)
        print('Full matrix filling', d0, sep='\n')
        d1 = fill_k(pair[0], pair[1], gap, match, mismatch, k)
        d2 = fill_k(pair[0], pair[1], gap, match, mismatch, k + 1)
        if d1 < d2:
            # если для полосы ширины k + 1 показывает лучший результат,
            # то выводится предупреждение о том, что ширина полосы k
            # недостаточная для правильного результата
            print("k={} is not enough, {} preforms better: {}, {}".format(k, k + 1, d1, d2))
        else:
            print('Filling stripe of width {}\n{}'.format(k, d1))


if __name__ == "__main__":
    main()
