"""Karatsuba Multiplication"""
import sys
sys.setrecursionlimit(5000)
def openfile(fname):
        f=open(fname, "r")
        allnum=[]
        for line in f:
                allnum.append(int(f.readline()))
        return splitinversions(allnum)

def splitinversions(alist):
        sortedlist=[]
        i=0
        j=0
        inversioncount=0
        if len(alist)==0:
            return 0
        else:
            left= splitinversions(alist[0:int(len(alist)/2)])
            right=splitinversions(alist[int(len(alist)/2):])
            while i<len(left) and j< len(right):
                if left[i]<right[j]:
                    sortedlist.append(left[i])
                    i+=1
                else:
                    sortedlist.append(right[j])
                    j+=1
                    inversioncount=len(left)-i

            if len(left)!=0:
                sortedlist+=left[i:]

            if len(right)!=0:
                sortedlist+=right[i:]
                
            return inversioncount

print(openfile("IntegerArray.txt"))




