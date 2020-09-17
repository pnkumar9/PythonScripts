'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
TrapRainWater.png

'''
'''
Best explained here https://www.youtube.com/watch?v=bPv7tqz2cdU&ab_channel=BrennanFradelis
This LeetCode problem states we need to find the amount of rain water that can be trapped in this grid. And this grid is represented as an array where each value is the height of one of the blocks at position i.

To solve this problem we will use 2 arrays that track the max height up to a certain point when iterating from left to right and right to left.

We will then use these arrays to calculate the water amount at each point using the formula

water amount at index i = min(left_to_right[i], right_to_left[i]) - height at index i
'''

def trap(height):

    left_to_right = [0] * len(height)
    right_to_left = [0] * len(height)

    #find out max height on left side ith container
    for i, h in enumerate(height):
        if i == 0:
            left_to_right[i] = h
        else:
            left_to_right[i] = max(h, left_to_right[i-1])
    #find out max height on right side of ith container
    for i in range(len(height)-1, -1, -1):
        h =height[i]

        if i == len(height)-1:
            right_to_left[i] = h
        else:
            right_to_left[i] = max(h, right_to_left[i+1])

    #final solution
    water_sum = 0
    for i,h in enumerate(height):

        water_sum += min(left_to_right[i], right_to_left[i]) - h

    return water_sum

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))    