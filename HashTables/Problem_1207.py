class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash1 = {}
        for i in range(len(arr)):
            cur = arr[i]
            if(cur in hash1):
                hash1[cur] +=1
            else:
                hash1[cur] = 1
        checkList = set() 
        for i, j in hash1.items():
            if(j in checkList):
                return False
            else:
                checkList.add(j)
        return True