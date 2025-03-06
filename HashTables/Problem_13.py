class Solution:
    def romanToInt(self, s: str) -> int:
        use = {
            0 : float('inf'),
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        check = 0
        total = 0
        for i in s:
            if (use[i]<=use[check]):
                total = total + use[i]
            else:
                total = total - use[check]
                k = check + i
                total = total + use[k]
            check = i
        return total


# working from backwards is much simpler