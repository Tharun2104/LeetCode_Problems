class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)): return False
        p1, p2 = 0, 0
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in s1:
            index = ord(i) - ord("a")
            s1Count[index] += 1
        
        while p2 < len(s1):
            index = ord(s2[p2]) - ord("a")
            # print("test")
            s2Count[index] += 1
            p2+=1
        
        matches = 0
        for i in range(26):
            if(s1Count[i] == s2Count[i]):
                matches += 1

        p2 -= 1
        while p2 < len(s2):
            # final check
            if( matches == 26):
                return True

            # adding the next character
            p2 += 1
            if(p2 == len(s2)):
                break
            aindex = ord(s2[p2]) - ord("a")
            s2Count[aindex] += 1
            
             # checking with matches
            if(  s2Count[aindex] == s1Count[aindex] ):
                matches += 1
            elif (s2Count[aindex] == s1Count[aindex] + 1):  # they were equal 
                matches -= 1
            # removing the first char
            rindex = ord(s2[p1]) - ord("a")
            s2Count[rindex] -= 1

            # checking with matches
            if(  s2Count[rindex] == s1Count[rindex] ):
                matches += 1
            elif (s2Count[rindex] == s1Count[rindex] - 1):  # they were equal 
                matches -=1

            p1 += 1
    
        return False


