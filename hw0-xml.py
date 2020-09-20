import xml.etree.ElementTree as ET

transition_function = {0:{'0':0, '1':1},
                       1:{'0':2, '1':1},
                       2:{'0':1, '1':1}}

states=set(["0", "1", "2"])
alphabet=set(["0","1"])
start_state = 0
accept_state=set(["1"])

dfa = (states, alphabet, transition_function, start_state, accept_state)

def GenerateXML(fileName) : 
      
    root = ET.Element("automaton") 

    for i in states:
        state = ET.Element("state") 
        root.append(state)
        state.set('id', i)
        #state.set('name', str(dfa[3]))
        if (start_state == int(i)):{
            ET.SubElement(state, "initial")
        }
        if (i in accept_state):{
            ET.SubElement(state, "final")
        }  

    for i in transition_function:
        for j, k in zip(transition_function[i].values(), transition_function[i].keys()):
            transition = ET.Element("transition") 
            root.append(transition)
            From = ET.SubElement(transition, "from") 
            From.text = str(i)
            To = ET.SubElement(transition, "to") 
            To.text = str(j)
            Read = ET.SubElement(transition, "read") 
            Read.text = str(k)
    
    tree = ET.ElementTree(root) 
      
    with open (fileName, "wb") as files : 
        tree.write(files) 
  
if __name__ == "__main__":  
    GenerateXML("dfa.xml")
