'''
Created on Jan 4, 2017

@author: anand
'''

points = [[0,0],[1,0],[2,0]]

res = 0
for p in points:
    cmap = {}
    for q in points:
        f = p[0]-q[0]
        s = p[1]-q[1]
        cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
    for k in cmap:
        print cmap[k]
        res += cmap[k] * (cmap[k] -1)

print res