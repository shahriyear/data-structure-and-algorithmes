
### Non-Constructible Change

#   Given an array of positive integers representing the values of coins in your
#   possession, write a function that returns the minimum amount of change (the
#   minimum sum of money) that you cannot create. The given coins can have any
#   positive integer value and aren't necessarily unique (i.e., you can have
#   multiple coins of the same value).
  
#   For example, if you're given coins = [1, 2, 5], the minimum amount of change
#   that you can't create is 4. If you're given no coins, the minimum amount of 
#   change that you can't create is 1.


#   Sample Input 
#   coins = [5, 7, 1, 1, 2, 3, 22]

#   Sample Output 
#   20


coins = [5, 7, 1, 1, 2, 3, 22]

### Solution 1
#   O(nLog(n)) time | O(1) space

def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1 :
            break
        currentChange += coin
    
    return currentChange + 1            



print(nonConstructibleChange(coins))




