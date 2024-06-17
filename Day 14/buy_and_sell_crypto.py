from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Understanding
        # questions to ask: what if there is only one day
        # if there is no profit, return 0


        # Matching
        # two pointers


        # Planning
        """
        def maxProfit(self, prices: List[int]) -> int:
            output = 0
            for i in range(len(prices)):
                for j in range(i+1, len(prices)):
                    if prices[i] >= prices[j]:
                        continue
                    elif prices[i] < prices[j]:
                        output = max(output, (prices[j] - prices[i]))

            return output

        """


        # Implementing
        output = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    continue
                elif prices[i] < prices[j]:
                    output = max(output, (prices[j] - prices[i]))

        return output

        # Reviewing: Correct
        """
        For time: O(n)
        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        """


        # Evaluating:
        # Time comp: O(n^2)
        # Space comp: O(1)

        