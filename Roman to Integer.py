class Solution:
    # @return an integer
    #http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
    def romanToInt(self, s):
        roman_int_map = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        roman_map = dict(I=1, V=2, X=3, L=4, C=5, D=6, M=7)
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return roman_int_map[s[0]]
        
        if roman_map[s[0]] < roman_map[s[1]]:
            return self.romanToInt(s[1:]) - roman_int_map[s[0]]
        else:
            return roman_int_map[s[0]] + self.romanToInt(s[1:])
