class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # dict key should be relevant last digit of streak
        # Intermediate nums in streak don't matter

        # So, each bottom num :-> highest in streak
        if nums == []:
            return 0

        d = {}

        for num in nums:

            if num not in d:
                if (num-1) in d and (num+1) in d:
                    (low_length, lower) = d[num-1]
                    (high_length, upper) = d[num+1]
                    print((low_length, lower), (high_length, upper))

                    d[lower] = (low_length + 1 + high_length, upper)
                    d[upper] = (low_length + 1 + high_length, lower)   
                    d[num] = (1, num)             
                elif (num-1) in d:
                    (length, lower) = d[num-1]
                    d[num] = (length + 1, lower)
                    d[lower] = (length + 1, num)
                elif (num+1) in d:
                    (length, upper) = d[num+1]
                    d[num] = (length+1, upper)
                    d[upper] = (length+1, num)
                else:
                    d[num] = (1, num)
            #print(num, d)
        
        #print(d)
        sorted_d = sorted(d.items(), key=lambda item: item[1][0], reverse=True)


        #print(sorted_d)
        return (sorted_d[0][1][0])