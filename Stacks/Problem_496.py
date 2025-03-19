class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            # using stack
            hash1 = {}
            for i in range(len(nums1)):
                hash1[nums1[i]] = i

            stack = []
            res = [-1]*len(nums1)
            for i in range(len(nums2)):
                cur = nums2[i]
                while stack and cur > stack[-1]:
                    val = stack.pop()
                    idx = hash1[val]
                    res[idx] = cur
                if(cur in hash1):
                    stack.append(cur)
                        
            return res     
            """
            # creating a hashmap
            hash1 = {}
            for i in range(len(nums1)):
                hash1[nums1[i]] = i
            
            nextMax = 0
            res = [-1]*len(nums1)
            for i in range(len(nums2)):
                if(nums2[i] in hash1):
                    p1 = i+1
                    for j in range(i+1, len(nums2)):
                        if(nums2[i] < nums2[p1]):
                            res[hash1[nums2[i]]] = nums2[p1]
                            break
                        else:
                            p1+=1
            return res
            """
