class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        res = ""
        for i in strs[1:]:
            for k in range(min(len(check), len(i))):
                if(check[k] == i[k]):
                    res += check[k]
                else:
                    break
            check = res
            res = ""
        return check