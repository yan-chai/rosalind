import glob
import re
txt = glob.glob('./*.txt')
with open (txt[0]) as f:
    out = f.readlines()
seq = out[0].strip('\n')
motif = out[1].strip(' ').strip('\n')
index = [i.start()+1 for i in re.finditer('(?=(%s))'%motif,seq)]
for i in index:
    print(i, end=' ')