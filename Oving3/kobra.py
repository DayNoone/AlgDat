from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.letter = ""
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    rot = Node()
    for o in ordliste:
        word = o[0]
        pos = o[1]
        curNode = rot
        while word:
            l = word[0]
            word = word[1:]
            nextNode = None
            if l in curNode.barn.keys():
                nextNode = curNode.barn[l]
            else:
                nextNode = Node()
                curNode.barn[l] = nextNode
            curNode = nextNode
        curNode.posi.append(pos)
    return rot



    # root = Node()
    # root.letter = "R"
    
    # for word in ordliste:
        
    #     temp_node = root
    #     for ch in range(0, len(word[0])):
    #         if(word[0][ch] not in temp_node.barn.keys()):
    #             add_node = Node()
    #             add_node.letter = word[0][ch]
    #         else:
    #             add_node = temp_node.barn[word[0][ch]]

    #         temp_node.barn[add_node.letter] = add_node
                    
    #         temp_node = add_node
    #         if(ch == len(word[0])-1):
    #             temp_node.posi.append(word[1])
    # return root


def posisjoner(ord, indeks, node):
    # pos = []
    # while word:
    #     l = word[0]
    #     word = word[1:]
    #     if l == "?":
    #         for ch in node.barn.keys():
    #             pos.extend(posisjoner(word,indeks,node.barn[ch]))
    #     try:
    #         node = node.barn[l]
    #     except Exception, e:
    #         return pos
    # return node.posi

    posi = []
    for i in ord:
        if i not in node.barn.keys():
            return []
        elif i == "?":
            for ch in node.barn.keys():
                posi.extend(posisjoner(ord[indeks:], indeks, node.barn[ch]))
        node = node.barn[i]
    
    return node.posi



  



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