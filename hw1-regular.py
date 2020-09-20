import sys
dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':1},
       2:{'0':1, '1':1}}

def accepts(transitions,initial,accepting,s):
    state = initial
    if len(s)>2:
        for c in s:
            state = transitions[state][c]
        if (state in accepting) == True:
            print('accept')
        else:
            print('reject')
    else:
        print('reject') 
try:
    inp = sys.stdin.readline()
    accepts(dfa,0,{1},inp.replace(" ", ""))
except:
    pass

