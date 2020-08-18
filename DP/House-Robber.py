'''
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
'''
'''
The idea is the store the max sum we can get for each house use it to calculate the following houses until we get the final result.

In the path that the robber chose to rob with max money, it is guaranteed that either the last house (num[-1]) or the 2nd last house (num[-2]) will be robbed. So we can compare the max sum path that includes num[-1] with the max sum path that includes num[-2] and return the larger one.

To get the sums of the two paths, we scan from left to right. A sliding window of size 4, [max_3_house_before, max_2_house_before, adjacent, cur], is used to calculate the max sum till the current house. The last element, cur, of the window is the money of the current house we are scanning. The 1st element, max_3_house_before, stores the max sum till the house that is 3 steps before the current one. The 2nd element, max_2_house_before, stores the max sum till the house that is 2 steps before the current one. The 3rd element, adjacent, stores the max sum till the house that are one step before the current one. To reach the current house, we either came from the house that is 3 steps before or from the one that is 2 steps before because visiting two adjacent houses is not allowed. So we can get the max sum till the current house by max(cur+max_3_house_before, cur+max_2_house_before).

Before scanning the next house we update the window by moving one house forward: max_3_house_before, max_2_house_before, adjacent = max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur).

When we finished the scanning, the max sum exists in either max_2_house_before or adjacent. So we return max(max_2_house_before, adjacent).

For example: num = [1,7,9,4], at the beginning, max_3_house_before, max_2_house_before, adjacent are initialized to 0, so it is like putting 3 zeros before the input list [0, 0, 0, 1, 7, 9, 4]. Here are steps for calculating the max sum for each house(the sliding window is marked by parentheses):

[(0, 0, 0, 1), 7, 9, 4], cur = max(0+1, 0+1)

-> [ (0, 0, 1, 7), 9, 4], cur = max(0+7, 0+7)

-> [(0, 1, 7, 9), 4], cur = max(0+9, 1+9)

-> [(1, 7, 10, 4)], cur = max(1+4, 7+4)

-> [7, 10, 11], 10 is the max sum of path that includes num[-2], 11 is the max sum of path that includes num[-1], so return max(10, 11)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        [#sliding](https://leetcode.com/problems/sliding-window-maximum) window of size 4
        [#add](https://leetcode.com/problems/add-two-numbers) 3 zeros in the front
        nums = [0, 0, 0] + nums
        for i in range(3, len(nums)):
            b3 = nums[i-3] + nums[i]
            b2 = nums[i-2] + nums[i]
            nums[i] = max(b3, b2)
        return max(nums)