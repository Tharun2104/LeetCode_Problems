class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        string = ""
        for i in s:
            try:
                if(i.isalnum()):
                    string +=i.lower()
            except:
                continue
        print(string)

        return string == string[::-1]
            


            