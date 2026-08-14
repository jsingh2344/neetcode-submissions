class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
        

        coll = set()

        l = 0

        r = 0

        coll.add(s[0])
        curr_length = 1

        max_length = 1

        while l != len(s) - 1: #invariant: coll represents stretch between l and r
            if r + 1 < len(s) and s[r+1] not in coll:
                
                r += 1
                coll.add(s[r])
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
            else:
                coll.remove(s[l])
                l += 1
                curr_length -= 1
        
        return max_length

            

                    
            
        
        return max_length