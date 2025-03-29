class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:        
        hashMap ={}
        for i in nums:
            if(i in hashMap):
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        
        freqList = [[] for _ in range(len(nums) + 1)]

        for m, n in hashMap.items():
            freqList[n].append(m)
        res = []
        for i in range(len(freqList)-1, -1, -1):
            for n in freqList[i]:
                res.append(n)
                if (len(res) == k):
                    return res
        