import re
with open('./table.txt') as f:
    out = f.read()
coden = re.findall('[A-Z]{3}', out)
pro = re.findall(r'\s[A-Z]\s|\sStop\s', out)
table = {}
index = 0
for i in coden:
    dic = {i:pro[index]}
    table[i] = pro[index].strip(' ').strip('\n')
    index  += 1
with open('./rosalind_prot.txt') as f:
    out = f.read()
    out = re.findall(r'.{3}', out)
pro_str = "".join(list(map(lambda x: table[x], out)))
result = pro_str.split('Stop')
for i in result:
    print(i)