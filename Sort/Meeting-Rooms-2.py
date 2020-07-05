#!/usr/bin/env python3.6

'''
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
find the minimum number of conference rooms required.

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output:1

'''
def minMeetingRooms(intervals):
    
    starts, ends = [0]*len(intervals), [0]*len(intervals)

    for i in range(len(intervals)):
        starts.append(intervals[i][0])
        ends.append(intervals[i][1])

    starts.sort()
    ends.sort()

    s, e = 0, 0
    min_rooms, cnt_rooms = 0, 0
    while s < len(starts):
        if starts[s] < ends[e]:
            cnt_rooms += 1  # Acquire a room.
            # Update the min number of rooms.
            min_rooms = max(min_rooms, cnt_rooms)
            s += 1
        else:
            cnt_rooms -= 1  # Release a room.
            e += 1

    return min_rooms    

print(minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(minMeetingRooms([[7,10],[2,4]]))