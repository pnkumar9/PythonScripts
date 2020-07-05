#!/usr/bin/env python3.6

'''
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
determine if a person could attend all meetings.

Input:[[0,30],[5,10],[15,20]]
Output: false

Input:[[7,10],[2,4]]
Output:true

concept:

input is list of tupples
list of tuples can be sorted by inbuild function

Please see this link for different methods of list of tuples sorting
https://algocoding.wordpress.com/2015/04/14/how-to-sort-a-list-of-tuples-in-python-3-4/

1. by default sort() sorts by first element, if two tuples have same first element, then they are sorted
   by their second element.

Sort by first elements ONLY. this is needed for meeting rooms problem

import operator
my_list = [ ('John', 40), ('Dana', 35), ('Betty', 10), ('Robby', 8), ('John', 20) ]
my_list.sort(key = operator.itemgetter(0))
print(my_list)

Sort by second element in the tuple:
my_list.sort(key = operator.itemgetter(1))
'''
import operator
def canAttendMeetings(arr):

    print(f"input intervals are: {arr}")
    arr.sort(key = operator.itemgetter(0))
    print(f"input intervals after sort based on key=start are: {arr}")

    # this is crucial step.
    # enumerate gives counter, and list item (which is a tuple in our case)
    # note we start from item 1 and compare with item 0
    # i default start at 0
    for i, next_interval in enumerate(arr[1:]):
        #next_interval[0] = start of next interval
        #  arr[i][1] =  end of prior interval
        #print(f"first interval {arr[i]}")
        #print(f"next interval {next_interval}")
        if next_interval[0] < arr[i][1]:
            return False

    return True            

#This is simple solution

def canAttendMeetings_simple(intervals):

    intervals.sort()
    meeting_num = len(intervals)

    for i in range(1,meeting_num):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True            


#print(canAttendMeetings([[0,30],[15,20],[5,10],[5,15]]))
#print(canAttendMeetings([[7,10],[2,4]]))

print(canAttendMeetings_simple([[0,30],[15,20],[5,10],[5,15]]))
print(canAttendMeetings_simple([[7,10],[2,4]]))
