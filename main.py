# This is a sample Python script.
import urllib.request, chardet


def print_table_1(array):
    print("-" * 20)
    print("Символ |" + " " * 5 + " Частота " + " " * 5)
    print("-" * 20)
    for i in range(len(array)):
        if array[i] != 0:
            print(bytes([i]), " |" + " " * 10, array[i])


def program_ru(filename):
    print("--" * 10 + "Определение руссчкоязычного текста: " + filename + "--" * 10)
    file = open(filename, 'rb')
    data = file.read()
    file.close()
    print(chardet.detect(data))
    if chardet.detect(data).get('language') == '':
        count = [0 for i in range(176)]
        f = 0
        for i in data:
            if i < 176:
                count[i] = i

        v = count.copy()

        for i in range(176):
            if not ((v[i] >= 0 | v[i] < 64) or (v[i] >= 91 | v[i] <= 95) or v[i] >= 123):
                f = 1
                print("Символ не принадлежит русскоязычному алфавиту, код символа: ", i)
                break

        if f == 0:
            print("Текст является простым русскоязычным текстом.")
        else:
            print("Текст не  является простым русскоязычным текстом.")


def program3(filename):
    print("--" * 10 + "Определение наиболее частых октетов: " + filename + "--" * 10)
    file = open(filename, 'rb')
    data = file.read()
    file.close()
    count = [0 for i in range(128)]
    for i in data:
        if i < 128:
            count[i] = count[i] + 1
    print_table_1(count)
    v = count.copy()
    print("4 наиболее частых октета : ")
    for i in range(4):
        print("Символ: ", bytes([v.index(max(v))]), "--> Номер символа в таблице ASCII: ", v.index(max(v)))
        v[v.index(max(v))] = 0
    v = count.copy()
    print("4 частых октета, не являющихся кодами печатных символов ASCII: ")
    for i in range(128):
        if not str(bytes([v.index(max(v))])).isprintable():
            print("ds")
            print(bytes([v.index(max(v))]))
            print(v.index(max(v)))
            v[v.index(max(v))] -= max(v)


if __name__ == '__main__':
    program3("Льюис Кэрролл. Охота на Снарка — Кружков — utf8.txt")
    program_ru("Льюис Кэрролл. Охота на Снарка — Кружков — koi8r.txt")
    program_ru("4.txt")
    program_ru("1.txt")
    program_ru("Михаил Лермонтов. Герой нашего времени — utf8.txt")
    program_ru("0.txt")
