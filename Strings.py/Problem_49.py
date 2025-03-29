class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using ASCII value
        hashMap = {}
        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[ord(j) - ord('a')] += 1
            key = tuple(freq) # cannot store list as a key in dict
            if(key in hashMap):
                hashMap[key].append(i)
            else:
                hashMap[key] = [i]
        opList = []
        for i in hashMap:
            opList.append(hashMap[i])
        return opList       
        """
        # using sort
        hashMap = {}
        for i in strs:
            curSort = "".join(sorted(i))
            if(curSort in hashMap):
                hashMap[curSort].append(i)
            else:
                hashMap[curSort] = [i]
        opList = []
        for i in hashMap:
            opList.append(hashMap[i])
        return opList
        """