import string 
import random
import xml.etree.ElementTree as ET

inp = input()

tree = ET.parse(inp)
root = tree.getroot()

dfa={}
states=set()
alphabet=set()
accept_state=set()
From=list()
To=list()
Read=list()


for state in root.iter('state'):
    states.add(state.get('id'))
    for ChildState in state.iter():
        if ChildState.tag == 'initial':
            q0 = state.get('id')
        elif ChildState.tag == 'final':
            accept_state.add(state.get('id'))

for transition in root.iter('transition'):
    for ChildFrom in transition.iter('from'):
        From.append(ChildFrom.text)
    for ChildTo in transition.iter('to'):
        To.append(ChildTo.text)
    for ChildRead in transition.iter('read'):
        Read.append(ChildRead.text)
        alphabet.add(ChildRead.text)


for j in range(len(From)):
    dfa.setdefault(int(From[j]), {})[Read[j]] = int(To[j])

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

def printAll(set, k):

    n = len(set)
    printAllRec(set, "", n, k)

def printAllRec(set, prefix, n, k):
    # Base case: k is 0,
    if (k == 0):
        if accepts(dfa,int(q0),{0},prefix) == True:
            print(prefix)
        return

    # call for k equals to k-1
    for i in range(n):

        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased
        printAllRec(set, newPrefix, n, k - 1)

for i in range(5, 0, -1):
        printAll(''.join(alphabet), i)

