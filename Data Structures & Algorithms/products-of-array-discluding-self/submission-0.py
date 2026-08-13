class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # Go through and make a prefix and suffix array for i 
        # [1, 2, 8, 48]

        # And a suffix array: [6, 24, 48, 48] -> [48,48, 24, 6]
        # Then, in final answer: 

        prefixes = []
        suffixes = []

        rev = nums[::-1]

        for i in range(len(nums)):

            if i == 0:
                prefixes.append(nums[i])
                suffixes.append(rev[i])
            else:
                prefixes.append(prefixes[i-1] * nums[i])
                suffixes.append(suffixes[i-1] * rev[i])

        suffixes.reverse()

        #print(suffixes, prefixes)

        prod_list = []
        for j in range(len(nums)):

            suff_idx = j+1
            pref_idx = j-1

            if pref_idx < 0:
                prod_list.append(suffixes[suff_idx])
            elif suff_idx >= len(nums):
                prod_list.append(prefixes[pref_idx])
            else:
                prod_list.append(prefixes[pref_idx] * suffixes[suff_idx])
        

        return prod_list


            

        
   

