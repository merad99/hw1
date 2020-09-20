import xml.etree.ElementTree as ET
from xml.dom import minidom

inp1, inp2 = input().split()

tree1 = ET.parse(inp1)
root1 = tree1.getroot()

transition_function1={}
states1=set()
alphabet1=set()
accept_state1=set()
From1=list()
To1=list()
Read1=list()


for state in root1.iter('state'):
    states1.add(state.get('id'))
    for ChildState in state.iter():
        if ChildState.tag == 'initial':
            start_state1 = state.get('id')
        elif ChildState.tag == 'final':
            accept_state1.add(state.get('id'))

for transition in root1.iter('transition'):
    for ChildFrom in transition.iter('from'):
        From1.append(ChildFrom.text)
    for ChildTo in transition.iter('to'):
        To1.append(ChildTo.text)
    for ChildRead in transition.iter('read'):
        Read1.append(ChildRead.text)
        alphabet1.add(ChildRead.text)


for j in range(len(From1)):
    transition_function1.setdefault(int(From1[j]), {})[Read1[j]] = int(To1[j])


tree2 = ET.parse(inp2)
root2 = tree2.getroot()

transition_function2={}
states2=set()
alphabet2=set()
accept_state2=set()
From2=list()
To2=list()
Read2=list()


for state in root2.iter('state'):
    states2.add(state.get('id'))
    for ChildState in state.iter():
        if ChildState.tag == 'initial':
            start_state2 = state.get('id')
        elif ChildState.tag == 'final':
            accept_state2.add(state.get('id'))

for transition in root2.iter('transition'):
    for ChildFrom in transition.iter('from'):
        From2.append(ChildFrom.text)
    for ChildTo in transition.iter('to'):
        To2.append(ChildTo.text)
    for ChildRead in transition.iter('read'):
        Read2.append(ChildRead.text)
        alphabet2.add(ChildRead.text)


for j in range(len(From2)):
    transition_function2.setdefault(int(From2[j]), {})[Read2[j]] = int(To2[j])


def GenerateXML() : 
      
    root = ET.Element("automaton") 

    for i in states1:
        for j in states2:
            state = ET.Element("state") 
            root.append(state)
            state.set('id', '(' + i + ' ' + j + ')')
            state.set('name', '(' + i + ' ' + j + ')')
            if (int(start_state1) == int(i) and int(start_state2) == int(j)):
                ET.SubElement(state, "initial")
            if (i in accept_state1 or j in accept_state2):
                ET.SubElement(state, "final")

    for i in transition_function1:
        for l in transition_function2:
            for j, k in zip(transition_function1[i].values(), transition_function1[i].keys()):
                for m, n in zip(transition_function2[l].values(), transition_function2[l].keys()):
                    if (k == n):
                        transition = ET.Element("transition") 
                        root.append(transition)
                        From = ET.SubElement(transition, "from") 
                        From.text = ('(' + str(i) + ' ' + str(l) + ')')
                        To = ET.SubElement(transition, "to") 
                        To.text = ('(' + str(j) + ' ' + str(m) + ')')
                        Read = ET.SubElement(transition, "read") 
                        Read.text = str(k)
                    
    #tree = ET.ElementTree(root) 
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    print(xmlstr)
  
 
GenerateXML()