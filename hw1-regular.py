import sys
dfa = {0:{'0':1, '1':1},
       1:{'0':2, '1':2},
       2:{'0':3, '1':3},
       3:{'0':3, '1':3}}

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    if (state in accepting) == True:
        print('accept')
    else:
        print('reject')
try:
    inp = sys.stdin.readline()
    accepts(dfa,0,{3},inp.replace(" ", ""))
except:
    pass

