from sys import *
import traceback

def utelukk_noder(nabomatrise, startnode, kanter, noder, l):

    n = len(nabomatrise)
    for j in range(n):
        if nabomatrise[startnode][j]:
            kanter.append(0)
            if j not in l:
                l.append(j)
                utelukk_noder(nabomatrise, j, kanter, noder, l)
    return l



def subgraftetthet(nabomatrise, startnode, kanter, noder, l):
    ut = []
    noder = utelukk_noder(nabomatrise, startnode, kanter, noder, l)
    for i in range(len(nabomatrise)):
        if i not in noder:
            ut.append(i)

    kant = 0
    for j in ut:
        for k in range(len(nabomatrise[j])):
            if nabomatrise[j][k] and k in ut:
                kant +=1

    noder = n-len(l)

    if noder == 0:
        return 0.0
    else:
       return float(kant) / float(noder**2)
    return 1
try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start, [], 0, [start]) + 1E-12)
except:
    traceback.print_exc(file=stderr)

