class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        use_dict = dict()
        for i in range(len(nums)):
            val = target - nums[i]
            if(val in use_dict):
                return [i, use_dict[val]]
            else:
                use_dict[nums[i]] = i