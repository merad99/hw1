import sys
dfa1 = {0:{'1':1, '2':1, '3':1, 'a':1, 'b':1, 'c':1, '!':1, 'A':1, 'B':1, 'C':1},
       1:{'1':2, '2':2, '3':2, 'a':2, 'b':2, 'c':2, '!':2, 'A':2, 'B':2, 'C':2},
       2:{'1':3, '2':3, '3':3, 'a':3, 'b':3, 'c':3, '!':3, 'A':3, 'B':3, 'C':3},
       3:{'1':3, '2':3, '3':3, 'a':3, 'b':3, 'c':3, '!':3, 'A':3, 'B':3, 'C':3}}

dfa2 = {4:{'1':4, '2':4, '3':4, 'a':4, 'b':4, 'c':4, '!':4, 'A':5, 'B':5, 'C':5},
       5:{'1':5, '2':5, '3':5, 'a':5, 'b':5, 'c':5, '!':5, 'A':5, 'B':5, 'C':5}}

dfa3 = {6:{'1':7, '2':7, '3':7, 'a':6, 'b':6, 'c':6, '!':6, 'A':6, 'B':6, 'C':6},
       7:{'1':7, '2':7, '3':7, 'a':7, 'b':7, 'c':7, '!':7, 'A':7, 'B':7, 'C':7}}

dfa4 = {8:{'1':8, '2':8, '3':8, 'a':8, 'b':8, 'c':8, '!':9, 'A':8, 'B':8, 'C':8},
       9:{'1':9, '2':9, '3':9, 'a':9, 'b':9, 'c':9, '!':9, 'A':9, 'B':9, 'C':9}}

dfa = {0:dict(set(dfa1[0].items()).intersection(set(dfa1[0].items()))),
       1:dict(set(dfa1[1].items()).intersection(set(dfa1[1].items()))),
       2:dict(set(dfa1[2].items()).intersection(set(dfa1[2].items()))),
       3:dict(set(dfa1[3].items()).intersection(set(dfa1[3].items()))),
       4:dict(set(dfa2[4].items()).intersection(set(dfa2[4].items()))),
       5:dict(set(dfa2[5].items()).intersection(set(dfa2[5].items()))),
       6:dict(set(dfa3[6].items()).intersection(set(dfa3[6].items()))),
       7:dict(set(dfa3[7].items()).intersection(set(dfa3[7].items()))),
       8:dict(set(dfa4[8].items()).intersection(set(dfa4[8].items()))),
       9:dict(set(dfa4[9].items()).intersection(set(dfa4[9].items())))}

def accepts(transitions,initial,accepting,s):
    List=list()
    for i in initial:
       state = i
       for c in s:
           state = transitions[state][c]
       List.append(state in accepting)
    return all(elem == True for elem in List)
    

try:
    inp = sys.stdin.readline()
    if(accepts(dfa,(0,4,6,8),{3,5,7,9},inp)==True):
        print('good')
    else:
        print('bad')
except:
    pass