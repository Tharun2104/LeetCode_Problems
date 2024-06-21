"""
56. Merge Intervals
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

"""
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals)  #O(NLogN)
        final_list = [intervals[0]]
        for start, end in intervals[1:]:
            if(start>final_list[-1][1]):
                final_list.append([start,end])
            else:
                old_interval = final_list[-1][0]
                new_interval=max(final_list[-1][1],end)
                final_list[-1][1] = new_interval
        return final_list
        
test = Solution()
print(test.merge(intervals))