import glob
txt = glob.glob('./*txt')
pairs = {'A':'T','T':'A','C':'G','G':'C'}
with open(txt[0], 'r') as f:
    dna = f.read().strip('\n')[::-1]

print(''.join([pairs[x] for x in dna]))