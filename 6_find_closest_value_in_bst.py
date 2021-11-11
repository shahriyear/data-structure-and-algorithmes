
### Find Closest Value In BST

#   Write a function that takes in a Binary Search Tree (BST) and a target integer
#   value and returns the closest value to that target value contained in the BST.
  
#   You can assume that there will only be one closest value.

#   Each BST node has an integer value, a left child node, and a right child node.
#   A node is said to be a valid BST node if and only if it satisfies the BST property: its
#   value is strictly greater than the values of every node to its left; its value is
#   less than or equal to the values of every node to its right; and its children nodes 
#   are either valid BST nodes themselves or None / null.


#   Sample Input 
#   tree =      10
#             /    \
#            5      15
#          /   \   /  \ 
#         2     5 13   22
#        /          \
#       1           14
#
#   target = 12

#   Sample Output 
#   13


# {
#   "tree": {
#     "nodes": [
#       {"id": "10", "left": "5", "right": "15", "value": 10},
#       {"id": "15", "left": "13", "right": "22", "value": 15},
#       {"id": "22", "left": null, "right": null, "value": 22},
#       {"id": "13", "left": null, "right": "14", "value": 13},
#       {"id": "14", "left": null, "right": null, "value": 14},
#       {"id": "5", "left": "2", "right": "5-2", "value": 5},
#       {"id": "5-2", "left": null, "right": null, "value": 5},
#       {"id": "2", "left": "1", "right": null, "value": 2},
#       {"id": "1", "left": null, "right": null, "value": 1}
#     ],
#     "root": "10"
#   },
#   "target": 12
# }


### Solution 1 [using recursive]
#   Avarage: O(Log(n)) time | O(Log(n)) space
#   Worst: O(n) time | O(n) space

def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree,target,tree.value)
	
def findClosestValueInBstHelper(tree,target,closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left,target,closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right,target,closest)
	else:
		return closest
	
 
### Solution 2 [using iterative]
#   Avarage: O(Log(n)) time | O(1) space
#   Worst: O(n) time | O(1) space

def findClosestValueInBst(tree, target):
    closest = tree.value
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest



# NOTE: can not be run without BST 