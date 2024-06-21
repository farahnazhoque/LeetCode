from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Understanding
        # if all the cars intersect before meeting at the target position, car fleet will be 1
        # otherwise, depending on which one meets which one, the count will increase


        # Matching
        # stacks and arrays


        # Planning
        """
        1. create an array to store pairs of position and speed using list comprehension: zip
        2. create a empty stack array to count how many car fleets
        3. loop through the sorted pairs within the pair list in reverse order
        4. calculate the time it takes to reach the target: (target - position) / speed
        5. append the time to the stack
        6. if the stack has 2 or more cars, compare the times of the last 2
        7. if the last one (recent) reaches the target before the one before, we combine the two in the stack by popping the recent one
        8. we return the length of the stack
        """


        # Implementing
        pair_list = [[p, s] for p, s in zip(position, speed)]
        carfleets = []

        for p, s in sorted(pair_list)[::-1]:
            time = (target - p) / s
            carfleets.append(time)
            if len(carfleets) >= 2 and carfleets[-1] <= carfleets[-2]:
                carfleets.pop()

        return len(carfleets)


        # Reviewing: Correct


        # Evaluating:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)