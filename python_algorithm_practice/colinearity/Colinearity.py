#--------------------------------
# colinearity
#---------------------------------

from itertools import combinations
# Q2: detect colinearity


def DetectCollinearity(n, pts):

    comb = combinations([i for i in range(n)], 3)
    output = False

    for indices in list(comb):
        i,j,k = indices[0], indices[1], indices[2]
        pt1 = pts[i]
        pt2 = pts[j]
        pt3 = pts[k]
        print(pt1)
        print(pt2)
        print(pt3)

        if pt1[0] != pt2[0] and pt2[0]!=pt3[0] and (pt2[1]-pt1[1])*(pt3[0]-pt2[0]) == (pt2[0]-pt1[0])*(pt3[1]-pt2[1]):
            output = True
            break
        elif pt1[0] == pt2[0] and pt2[0] == pt3[0]:
            output = True
            break
        else:continue
    return output