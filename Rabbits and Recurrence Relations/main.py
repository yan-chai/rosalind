import glob
import re
txt = glob.glob('./*txt')
with open(txt[0], 'r') as f:
    data = f.read().strip('\n')
data = re.findall('[0-9][0-9]*',data)

rabbit = [1, 1]
for i in range(2, int(data[0])):
    rabbit.append(rabbit[i-2]*int(data[1]) + rabbit[i-1])
print(rabbit[int(data[0])-1])