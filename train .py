from os import path
def partition(text):
    sentences = []
    simbEndSent = ['?', '!']
    simbols = [',', '"', '\'', '/', '\\', '-', ')', '(', '[', ']', '{', '}']
    text = text.lower()
    for i in simbols:
        text = text.replace(i, ' ')
    for i in simbEndSent:
        text = text.replace(i, '.')
    for i in text.split('.'):
        sentences += [[i]]
    while [''] in sentences:
        sentences.remove([''])
    for i in range(len(sentences)):
        sentences[i] = sentences[i][0].split(' ')
    for i in range(len(sentences)):
        while '' in sentences[i]:
            sentences[i].remove('')
    return sentences


def learn(address, model_name):
    while not path.isfile(address):
            address = input("Введите корректный адрес: ")
    f = open(address, encoding="utf-8")
    text = f.read()
    count_prefixes = 2
    dict_prefixes = {}  # (prefix 1, ..., prefixN) : [count of of meetings, [next word1, p1], ..., [next wordN, pN]]
    count = 0
    words = partition(text)
    for i in range(len(words)):
        for j in range(len(words[i]) - count_prefixes):
            count += 1
            if (words[i][j], words[i][j + 1]) in dict_prefixes.keys():
                dict_prefixes[(words[i][j], words[i][j + 1])][0] += 1
                for k in range(1, len(dict_prefixes[(words[i][j], words[i][j + 1])])):
                    if dict_prefixes[(words[i][j], words[i][j + 1])][k][0] == words[i][j + 2]:
                        dict_prefixes[(words[i][j], words[i][j + 1])][k][1] += 1
                        break
                    elif k == len(dict_prefixes[(words[i][j], words[i][j + 1])]) - 1:
                        dict_prefixes[words[i][j], words[i][j + 1]].append([words[i][j + 2], 1])
            else:
                dict_prefixes[(words[i][j], words[i][j + 1])] = [1, [words[i][j + 2], 1]]
    for i in dict_prefixes.keys():
        for j in range(1, len(dict_prefixes[i])):
            dict_prefixes[i][j][1] = dict_prefixes[i][j][1] / dict_prefixes[i][0]
    for i in dict_prefixes.keys():
        dict_prefixes[i][0] = dict_prefixes[i][0] / count
    f.close()
    return dict_prefixes

