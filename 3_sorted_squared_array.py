
### Sorted Squared Array

#   Write a function that takes in a non-empty array of integers that are sorted
#   in ascending order and returns a new array of the same length with the squares
#   of the original integers also sorted in ascending order.

#   Sample Input 
#   array = [1, 2, 3, 5, 6, 8, 9]

#   Sample Output 
#   [1, 4, 9, 25, 36, 64, 81]


array = [1, 2, 3, 5, 6, 8, 9]

### Solution 1 [Brute force]
#   O(nLog(n)) time | O(n) space

def sortedSquaredArray1(array):
    sortedArray = [0 for _ in array] 
    for i in range(0,len(array)):
        sortedArray[i] = array[i] * array[i] 

    sortedArray.sort()
    return sortedArray

print(sortedSquaredArray1(array))


### Solution 2 [if required in liner time]
#   O(n) time | O(n) space

def sortedSquaredArray2(array):
    sortedArray = [0 for _ in array]
    arrayLength = len(array)
    smallerValueIndex = 0
    largerValueIndex =  arrayLength - 1
	
    for index in reversed(range(arrayLength)):
        smallerValue = array[smallerValueIndex] 
        largerValue = array[largerValueIndex]
        
        if abs(smallerValue) > abs(largerValue):
            sortedArray[index] = smallerValue * smallerValue
            smallerValueIndex += 1
        else:
            sortedArray[index] = largerValue * largerValue
            largerValueIndex -= 1

    return sortedArray


print(sortedSquaredArray2(array))
 