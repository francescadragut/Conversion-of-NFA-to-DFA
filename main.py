print("Enter the data for the NFA:")
print("Enter list of states: ")
states_char = input()
states = []
for i in range(len(states_char)):
    if states_char[i] != ',' and states_char[i] != ' ' and states_char[i] != '[' and states_char[i] != ']':
        states.append(states_char[i])

print("Enter alphabet: ")
alphabet_char = input()
alphabet = []
for i in range(len(alphabet_char)):
    if alphabet_char[i] != ',' and alphabet_char[i] != ' ' and alphabet_char[i] != '[' and alphabet_char[i] != ']':
        alphabet.append(alphabet_char[i])

print("Enter starting state: ")
start = input()

print("Enter ending states: ")
end_char = input()
end = []
for i in range(len(end_char)):
    if end_char[i] != ',' and end_char[i] != ' ' and end_char[i] != '[' and end_char[i] != ']':
        end.append(end_char[i])

print("Enter transitions (for empty transition, press enter): ")
table = {}
for i in states:
    row = {}
    for j in alphabet:
        y = input("Enter transition (" + i + "," + j + "): ")
        for it in y:
            if it == ' ' or it == ',' or it == '{' or it == '}' or it == '[' or it == ']':
                y = y.replace(it, '')
        row[j] = y
    table[i] = row

dfa_table = {}
for key, value in table.items():
    if key == start:
        dfa_table[key] = value

new = [start]
new1 = [start]

auxdict = table[start].values()
for i in auxdict:
    if i != start:
        new1.append(i)

n = len(new1)

from collections import OrderedDict

def order(s):
    sorted_characters = sorted(s)
    s = "".join(sorted_characters)
    return s

def delete_duplicates(s):
    return "".join(OrderedDict.fromkeys(s))

i = 0
while n > 0:
    if new1[i] not in new:
        new.append(new1[i])
        cnt = 0
        dict = {}
        for j in alphabet:
            string = ''
            for k in new1[i]:
                for keyy, vall in table.items():
                    if keyy == k:
                        for key1, val1 in vall.items():
                            if key1 == j and val1 not in string:
                                string += val1
            string = order(string)
            string = delete_duplicates(string)
            dict[j] = string
            new1.append(string)
            cnt += 1
        n += cnt
        dfa_table[new1[i]] = dict
    new1.pop(0)
    n -= 1

dfa_states = []
for key in dfa_table.keys():
    dfa_states.append(key)
dfa_states1 = []
for item in dfa_states:
    if item == '':
        dfa_states1.append('err')
    else: dfa_states1.append(item)

def search_end(string):
    for i in string:
        if i in end:
            return 1
    return 0

dfa_final = []
for item in dfa_states:
    if search_end(item) == 1:
        dfa_final.append(item)

print("\n\nDFA alphabet: ",alphabet)
print("DFA states: ",dfa_states1)
print("DFA starting state: ",start)
print("DFA final states: ",dfa_final)
print("DFA transition table:")

header = 'delta_DFA     '
for item in alphabet:
    header = header + item + '        '
lines = len(header)*'-'

print('\n',header)
print(lines)

row = ''
for key, val in dfa_table.items():
    if key == '':
        row = row + '      err      '
    elif key == start:
        row = row + '   -> ' + key + (9-len(key))*' '
    elif key == end or search_end(key) == 1:
        row = row + '    * ' + key + (9-len(key))*' '
    else: row = row + '      ' + key + (9-len(key))*' '

    for key1, val1 in val.items():
        if val1 == '':
            row = row + 'err      '
        else: row = row + val1 + (9-len(val1))*' '
    print(row)
    row = ''
