import glob
txt = glob.glob('./*txt')
with open(txt[0], 'r') as f:
    data = f.read().strip('\n')
print(data.replace("T", "U"))