from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.letter = ""
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    root = Node()
    
    for word in ordliste:
        
        temp_node = root
        for ch in range(0, len(word[0])):
            
            add_node = Node()
            add_node.letter = word[0][ch]
            
            temp_node.barn[add_node.letter] = add_node
            temp_node = add_node
            if(ch == len(word[0])-1):
                temp_node.posi.append(word[1])
        
            #print ch
            #print temp_node.barn.keys()
            #print temp_node.posi



def posisjoner(ord, indeks, node):
    d = []
    return d
    # SKRIV DIN KODE HER


try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)