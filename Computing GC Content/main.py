import glob
import re
txt = glob.glob('./*.txt')
with open(txt[0], 'r') as f:
    out = f.readlines()
name = []
content = []
a = -1
string = ''
for i in out:
    if re.search(r'Rosalind_[0-9]*', i):
        content.append(string)
        string = ''
        name.append(re.search(r'>Rosalind_[0-9]*', i).group().strip('>'))
    else:
        string = string + i.strip('\n')
content.append(string)
del content[0]
num_con = []
max_per = 0
index = 0
for i in content:
    i_len = len(i)
    cg = i.count('C')+i.count('G')
    if max_per< cg/i_len:
        max_per = cg/i_len
        max_index = index
    a = cg/i_len*100
    put = ("%.6f" %a)
    num_con.append(put)
    index +=1
print (name[max_index]+'\n'+str(num_con[max_index]))
