
### Validate Subsequence

#   Given two non-empty arrays of integers, write a function that determines
#   whether the second array is a subsequence of the first one.

#   A subsequence of an array is a set of numbers that aren't necessarily adjacent
#   in the array but that are in the same order as they appear in the array. For
#   instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4]
#   and so do the numbers   [2, 4] . Note that a single number in an array and the 
#   array itself are both valid subsequences of the array.

#   Sample Input 
#   array = [5, 1, 22, 25, 6, -1, 8, 10]
#   targetSum = [1, 6, -1, 10]

#   Sample Output 
#   true


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

### Solution 1
#   O(n) time | O(1) space

def isValidSubsequence1(array, sequence):
    arrayIndex = 0
    sequenceIndex = 0
    arrayLength = len(array)
    sequenceLength = len(sequence)

    while arrayIndex < arrayLength and sequenceIndex < sequenceLength:
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrayIndex += 1
    return sequenceIndex == sequenceLength



print(isValidSubsequence1(array,sequence))


### Solution 2
#   O(n) time | O(1) space

def isValidSubsequence2(array, sequence):
    sequenceIndex = 0
    sequenceLength = len(sequence)

    for value in array:
        if sequenceIndex == sequenceLength:
            break
        if value == sequence[sequenceIndex]:
            sequenceIndex += 1
        
    return sequenceIndex == sequenceLength



print(isValidSubsequence2(array,sequence))

