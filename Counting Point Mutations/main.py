import glob
txt = glob.glob('./*.txt')
with open(txt[0]) as f:
    out = f.readlines()
mutant = 0
index = 0
for i in out[0].strip('\n'):
    if i != out[1][index]:
        mutant +=1
    else:
        pass
    index+=1
print(mutant)
