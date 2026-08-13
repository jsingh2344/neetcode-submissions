class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):

            if (target-num) in seen:
                return [seen[(target-num)], i]
            else:
                seen[num] = i
            
        return None



# 3: check {}, add {3: 0}
# 4: check {3:0 }, because 7-4 is in seen return [0, 1]


        