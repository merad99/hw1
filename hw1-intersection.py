import sys
dfa = {0:{'A':1, 'B':1, 'C':1, 'a':1, 'b':1, 'c':1, '1':1, '2':1, '3':1, '!':1},
       1:{'A':1, 'B':1, 'C':1, 'a':1, 'b':1, 'c':1, '1':1, '2':1, '3':1, '!':1}}

def accepts(transitions,initial,accepting,s):
    state = initial
    if (len(s) >= 3 and any(x.isupper() for x in s) and any(x.isdigit() for x in s) and any(not x.isalnum() for x in s)):
        for c in s:
            state = transitions[state][c]
        if (state in accepting) == True:
            print('good')
        else:
            print('bad')
    else:
        print('bad') 
try:
    inp = sys.stdin.readline()
    accepts(dfa,0,{1},inp.replace(" ", ""))
except:
    pass