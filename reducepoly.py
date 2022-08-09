import pandas as pd
import numpy as np

#from tkinter import filedialog as fd
#filename = fd.askopenfilename()

def parseInputs(pos,tolerance ):
    defaultTolerance = 0.001
    a = np.min(pos ,axis=0 );
    b = np.max(pos ,axis=0 )
    scaling = np.linalg.norm(b-a)
    tolerance = tolerance * scaling
    return tolerance



def  douglasPeucker(ptList, n, tolerance):
    if n <= 2:
        posreduced = ptList.copy()
        return posreduced
    startEnd =  ptList[[0,n-1],:]
    dNode = np.sqrt((startEnd[1,1] - startEnd[0,1] )** 2 + (startEnd[1,0] - startEnd[0,0] )** 2)
    d = np.zeros([n-1])
    eps = 2.220446049250313e-16
    for k in range(1,n-1):
        if dNode > eps:
            mat123 = np.array([ [1,startEnd[0,0],startEnd[0,1]] , [1,startEnd[1,0], startEnd[1,1]] , [1, ptList[k,0], ptList[k,1]] ])
            d[k] =  np.abs(np.linalg.det( mat123 ))/dNode;
        else:
            d[k] = np.sqrt((ptList[k,0]-startEnd[0,0] )** 2 + (ptList[k,1]-startEnd[0,1] )** 2)
    idx = np.where(d == np.max(d) )[0]+1
    dmax = d[idx - 1]
    farthestIdx = idx[0]
    if dmax > tolerance:
        recList1 = douglasPeucker(ptList[0:farthestIdx,:], farthestIdx, tolerance)
        recList2 = douglasPeucker(ptList[farthestIdx-1:n,:], n-farthestIdx+1, tolerance)
        
        posreduced = np.vstack([recList1 , recList2[1:,:] ])
    else:
        posreduced = startEnd.copy()
        
        
    return posreduced








def reducepoly(pos,tolerance):
    tolerance = parseInputs(pos,tolerance )
    n = pos.shape[0]
    if n <= 1:
        posreduced = pos.copy()
    else:
        posreduced = douglasPeucker(pos, n, tolerance)


    return posreduced.astype(float)
