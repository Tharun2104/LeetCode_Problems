class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opCount = 0
        useDict = dict()
        for i in nums:
            if(i!= 0 and i not in useDict):
                useDict[i] = True
                opCount +=1

        return opCount    





        """
        # brute force
        opCount = 0
        def minFun(num):
            minNum = float('inf')
            for i in num:
                if(i < minNum and i != 0 ):
                    minNum = i
            return minNum
        toggle = True
        value = minFun(nums)
        trackMin = float('inf')
        test = True
        while toggle:
            for i in nums:
                if(i != 0):
                    test = False
                    i = i - value
                    if(i<trackMin):
                        trackMin = i
                if(test):
                              se
                    return opCount
            value = trackMin
            opCount+=1
        """