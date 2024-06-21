"""
57. Insert Interval
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        # print(intervals)
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
print(test.insert(intervals,newInterval))