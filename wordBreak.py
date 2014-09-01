class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        ptr = 1 
        
        if len(s) == 0:
            return True
        
        while ptr <= len(s):
            temp_str = s[0:ptr]
            if temp_str in dict:
                if self.wordBreak(s[ptr:], dict):
                    return True
                
            ptr = ptr + 1 
            
        return False
