#author = Dipayan Dutta

array = [1,2,3,4,5,-9,0,100,201]

def main():
    displayArray(array)

def displayArray(array):
    count = 0

    print "Here is the unsorted array"
    print "=========================="

    for values in xrange(len(array)):
        print str(values)+ " th element is "+ str(array[values])
    count = len(array)
    print "Total number of elements in this array --> "+str(count)
    bubblesort(count,array)
    
def bubblesort(count,array):
    tempArray = 0
    limit     = count-1
    checkFlag = False

    for outerCounter in array:
        for innerCounter in xrange(limit):
            if (array[innerCounter]>array[innerCounter+1]):
                tempArray           = array[innerCounter]
                array[innerCounter] = array[innerCounter+1]
                array[innerCounter+1] = tempArray
                checkFlag           = True
        if (checkFlag == False):
            break
        else:
            checkFlag = False
    displaySortedArray(array)
    cluster(array)

def displaySortedArray(array):
    print "Here is the sorted array"
    print "========================"
    for number in xrange(len(array)):
        print str(number) +" th Element is " +str(array[number])

def cluster(array):

    positiveArray = []
    negetiveArray = []

    for number in xrange(len(array)):
        if array[number]>=0:
            positiveArray.append(array[number])
        else:
            negetiveArray.append(array[number])
    displayPositive(positiveArray)
    displayNegative(negetiveArray)

def displayPositive(positiveArray):
    total = len(positiveArray)
    print "Here is the positive arrays "
    print "Total count " +str(total)
    print "========================"
    
    for posValues in xrange(len(positiveArray)):
        print str(posValues)+" th Element "+str(positiveArray[posValues])

def displayNegative(negetiveArray):
    total = len(negetiveArray)
    print "Here is the negatice arrays "
    print "Total count " +str(total)
    print "========================"
    
    for posValues in xrange(len(negetiveArray)):
        print str(posValues)+" th Element "+str(negetiveArray[posValues])
            
if __name__ == '__main__':
    main()
