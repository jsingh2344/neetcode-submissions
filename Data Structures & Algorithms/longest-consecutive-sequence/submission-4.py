class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # dict key should be relevant last digit of streak
        # Intermediate nums in streak don't matter

        # So, each bottom num :-> highest in streak
        if nums == []:
            return 0

        d = {}

        max_length = 0
        for num in nums:

            if num not in d:
                if (num-1) in d and (num+1) in d:
                    (low_length, lower) = d[num-1]
                    (high_length, upper) = d[num+1]

                    d[lower] = (low_length + 1 + high_length, upper)
                    d[upper] = (low_length + 1 + high_length, lower)   
                    d[num] = (1, num)
                    if low_length + 1 + high_length > max_length:
                        max_length = low_length + 1 + high_length             
                elif (num-1) in d:
                    (length, lower) = d[num-1]
                    d[num] = (length + 1, lower)
                    d[lower] = (length + 1, num)
                    if length + 1 > max_length:
                        max_length = length + 1
                elif (num+1) in d:
                    (length, upper) = d[num+1]
                    d[num] = (length+1, upper)
                    d[upper] = (length+1, num)
                    if length + 1 > max_length:
                        max_length = length + 1
                else:
                    d[num] = (1, num)
                    if max_length == 0:
                        max_length = 1
            #print(num, d)
        
        #print(d)
        return max_length