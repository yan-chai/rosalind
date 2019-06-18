import glob
txt = glob.glob('./*txt')
with open(txt[0]) as f:
    out = f.read()
    out = out.split(' ')
    print(out)
k = int(out[0])
m = int(out[1])
n = int(out[2])
num = k+m+n
dom_per = k/num
dom_per += (m/num)*(m-1)/(num-1)*0.75
dom_per += (m/num)*k/(num-1)
dom_per += (m/num)*n/(num-1)*0.5
dom_per += (n/num)*k/(num-1)
dom_per += (n/num)*m/(num-1)*0.5
print(dom_per)