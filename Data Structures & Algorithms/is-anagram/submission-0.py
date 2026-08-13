class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        s_dict = {}

        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 0

        t_dict = {}

        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 0
        
        if t_dict == s_dict:
            return True
        return False
            

        