def maxType(a,b):
    return a > b
    
def minType(a,b):
    return b > a

class BinHeap:
    #typeHeap specifies whether the BinHeap object will sort itself with the maximum or smallest value at the head
    
    
    def __init__(self,typeHeap):        
        self.heapType = typeHeap
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapType(self.heapList[i],self.heapList[i // 2]):
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            fc = self.focusChild(i)
            if self.heapType(self.heapList[fc],self.heapList[i]):
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[fc]
                self.heapList[fc] = tmp
            i = fc
    
    #focus child is the min/max child of the parent
    def focusChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapType(self.heapList[i*2], self.heapList[i*2+1]):
                return i * 2
            else:
                return i * 2 + 1

    def root(self):
        return self.heapList[1]
    
    def delete(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

#Test max heap
bh = BinHeap(maxType)
bh.buildHeap([9,5,6,2,3])

print(bh.delete())
print(bh.delete())
print(bh.delete())
print(bh.delete())
print(bh.delete())
