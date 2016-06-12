import os
import itertools
perm = itertools.permutations("abcdefghijklmnopqrstuvwxyz1234567890",
                              int(input("Depth of maze?: ")))
dircount = 0
for items in perm:
    dircount+=1
    #print(items)
    d = "/".join(items)
    #print(d)
    if not os.path.exists("C:\\PornMaze\\"+d):
        os.makedirs("C:\\PornMaze\\"+d)
        
print('PORN MAZE COMPLETE!\nDIRECTORIES: ',dircount)
