"""Split Inversions"""

def splitinversions(alist):
        sortedlist=[]
        i=0
        j=0
        k=0
        inversioncount=0
        if len(alist)==0:
            return 0
        else:
            left=mergesort(alist[0:len(alist)/2)])
            right=mergesort(alist[len(alist)/2:])
            while i<len(left) and j< len(right):
                if left[i]<right[j]:
                    sortedlist[k]=left[i]
                    i+=1
                else:
                    sortedlist=right[j]
                    j+=1
                    inversioncount=len(left)-i
                k+=1

            while i<len(left):
                sortedlist[k]=left[i]
                i+=1
                k+=1

            while j<len(right):
                sortedlist[k]=right[j]
                j+=1
                k+=1
                
        return inversioncount

