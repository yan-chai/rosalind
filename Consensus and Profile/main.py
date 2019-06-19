from glob import glob
import numpy as np
import re
with open (glob('./*.txt')[0]) as f:
    out = f.readlines()
lenth = 0
dna = np.array([])
string = ''
for i in out:
    if re.search(r'Rosalind_[0-9]*', i):
        string += ','
        lenth += 1
    else:
        string = string + i.strip('\n')
        dna = np.append(dna, list(i.strip('\n')))
mun = len(dna[0].strip('\n'))
dna = dna.reshape((lenth, -1)).T
con_list = []
for i in dna:
    string = "".join([str(x) for x in i])
    con_list.append(string)
A = []
C = []
T = []
G = []
max_list = []
for i in dna:
    a = A.append(list(i).count("A"))
    c = C.append(list(i).count("C"))
    t = T.append(list(i).count("T"))
    g = G.append(list(i).count("G"))
    a = [list(i).count("A"), list(i).count("C"), list(i).count("T"), list(i).count("G")]
    index = a.index(max(a))
    max_list.append(['A', 'C', 'T', 'G'][index])
print( ''.join([x for x in max_list]))
print ('A:',''.join(['%d '%x for x in A]).strip())
print ('C:',''.join(['%d '%x for x in C]).strip())
print ('T:',''.join(['%d '%x for x in T]).strip())
print ('G:',''.join(['%d '%x for x in G]).strip())