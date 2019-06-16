import glob
cnts = {c:0 for c in 'ATCG'}
txt = glob.glob('./*txt')
for line in open(txt[0], 'r'):
    for c in line.rstrip():
        cnts[c] += 1
print(cnts)