class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0      
        for i, letter in enumerate(s):
            try:
                if roman[letter] >= roman[s[i+1]]: #compare the value of the current roman numeral to the next one, if the next one is equal or smaller, add it to the total, if smaller then subtract it
                    total += roman[letter]
                else:
                    total -= roman[letter]
            except IndexError:
                total += roman[letter]
                break
        return total
