import random
import time
import copy


MIN_RANGE = 10000
MAX_RANGE = 50000
MIN_VALUE = -1000
MAX_VALUE = 1000
TEST_NUM = 10


def insertionSort(arr):
    
    start_time = time.time()
    
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    print("insertionSort: %s s" % (time.time() - start_time))

def shellSort(arr, n):
    
    start_time = time.time()
    
    gap=n//2
     
    while gap>0:
        j=gap
        while j<n:
            i=j-gap
             
            while i>=0:

                if arr[i+gap]>arr[i]:
                    break
                
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
 
                i=i-gap
            j+=1
        gap=gap//2
        
    print("shellSort: %s s" % (time.time() - start_time))

def randArray():
    n = random.randint(MIN_RANGE, MAX_RANGE)
    arr = []
    for i in range(n):
        arr.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    return arr

def halfSortArray():
    n = random.randint(MIN_RANGE, MAX_RANGE)
    arr = []
    for i in range(n):
        arr.append(random.randint(MIN_VALUE, MAX_VALUE))

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-2
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        
    return arr

def duom1():
    arr = randArray()
    
    print("Aibes dydis: " + str(len(arr)))
    
    for i in range(TEST_NUM):
        
        print(str(i+1) + ": ")
        arrInsert = copy.copy(arr)
        arrShell = copy.copy(arr)
        
        insertionSort(arrInsert)
        shellSort(arrShell, len(arrShell))
    
def duom2():
    arr = halfSortArray()
    
    print("Aibes dydis: " + str(len(arr)))
    
    for i in range(TEST_NUM):
        
        print(str(i+1) + ": ")
        arrInsert = copy.copy(arr)
        arrShell = copy.copy(arr)
        
        insertionSort(arrInsert)
        shellSort(arrShell, len(arrShell))





if __name__=="__main__":
    
    duom1()
    #duom2()
