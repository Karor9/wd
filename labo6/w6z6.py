import numpy as np 

def diag(s1, s2, s3):
    d = np.empty((3, 3), dtype='str')
    for x in range(0, 3):
        d[0][x] = s1[x]
        d[x][0] = s2[x]
        d[x][x] = s3[-1+(-1)*x]
    d[1][2] = 'a'
    d[2][1] = 'u'
    return d

s1 = "tak"
s2 = "tam"
s3 = "set"

a = diag(s1, s2, s3)
print(a)