from glob import glob
with open(glob('./*txt')[0]) as f:
    out = f.read().strip('\n').split(' ')
f = [0,1,1]
def fibo(month, mortal):
    for i in range(3,month+1):
        if i <= mortal:
            total = f[i-1] + f[i-2]
        elif i == mortal+1:
            total = f[i-1] + f[i-2] - 1
        else:
            total = f[i-1] + f[i-2] - f[i-mortal-1]
        f.append(total)
    return(f[month])

print(fibo(int(out[0]), int(out[1])))

