import numpy as np
from train import learn

def generation():
    adr = "data\\" + input("Enter source file name")
    mname = input("Enter output file name")
    n = int(input("Enter the output sequence length"))
    dict_prefixes = learn(address=adr)
    text = []
    d_keys = [i for i in dict_prefixes.keys()]
    prefix_probabilities = [dict_prefixes[i][0] for i in d_keys]
    for i in d_keys[np.random.choice(range(len(d_keys)), p=prefix_probabilities)]:
        text += [i]
    for k in range(n - 2):
        if (text[-2], text[-1]) in dict_prefixes.keys():
            text += [np.random.choice([dict_prefixes[(text[-2], text[-1])][i][0] for i in range(1, len(dict_prefixes[(text[-2], text[-1])]))],
                                    p=[dict_prefixes[(text[-2], text[-1])][i][1] for i in range(1, len(dict_prefixes[(text[-2], text[-1])]))])]
        else:
            for i in dict_prefixes.keys():
                if i[1] == text[-1]:
                    text += [np.random.choice([dict_prefixes[i][j][0] for j in range(1, len(dict_prefixes[i]))],
                                              p=[dict_prefixes[i][j][1] for j in range(1, len(dict_prefixes[i]))])]
                    break
        if len(text) != k + 3:
            text += [d_keys[np.random.choice(range(len(d_keys)), p=prefix_probabilities)][0]]
    file = open(mname, 'w')
    for word in text:
        file.write(word + " ")
    file.close()
generation()
