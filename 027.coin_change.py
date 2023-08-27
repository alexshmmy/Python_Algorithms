# Given coins of different denominations and a total amount of money. From that, you need to write a function to compute the fewest 
# number of coins that you need to make up that amount, and which combination of coins is needed to make up the amount. If you can’t reach the given amount 
# of money with any combination of the coins, you return -1. 
# Solve it with bottom-up dynamic programming with tabularization solution in Python. Comment for the time and space complexity of your suggested solution.
#
# Time complexity: O(amount * len(coins)), as we iterate through the coins and 
# the target amount.
# Space complexity: O(amount+1), as we use a table to store the fewest number of 
# coins needed for each amount. 

from typing import List

def coinChange(coins: List[int], amount: int) -> List[int]:
    # Initialize a table to store the fewest number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)

    # The fewest number of coins needed to make 0 amount is 0
    dp[0] = 0
    
    # Initialize a table to store the combination of coins needed for each amount
    combination = [[] for _ in range(amount + 1)]

    # Iterate through each coin denomination
    for coin in coins:
        # Iterate through each amount from 1 to amount
        for i in range(1, amount + 1):
            # If the coin is less than or equal to the amount
            if coin <= i:
                # Update the fewest number of coins needed for i
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    combination[i] = combination[i - coin] + [coin]
                elif dp[i - coin] + 1 == dp[i]:
                    combination[i].append(coin)
    
    # If the fewest number of coins needed for the given amount is greater than the amount itself, return -1
    if dp[amount] == float('inf'):
        return [-1]
    
    # Otherwise, return the combination of coins needed
    return combination[amount]

if __name__ == "__main__":
    # Example usage:
    coins = [1, 2, 5]
    amount = 121
    res = coinChange(coins, amount)
    print(f"Number of coins needed: {len(res)}.\nThe coins needed: {res}")
