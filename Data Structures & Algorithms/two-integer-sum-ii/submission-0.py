class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:



        # Hypothetical: if you have [1, 2, 4, 5, 6, 8], target is 8
        # 1, 8 
        # 1, 6
        # 2, 6
        # Note that values after target / 2 are irrelevant as a BASE
        # But you need both a base and top

        # Could hash on everything less than target / 2


        # 1 is looking for 2, as soon as you see a num > 2 then dw about it
        # 

        length = len(numbers)

        small_idx = 0
        big_idx = length - 1

        while True:

            s = numbers[small_idx] + numbers[big_idx]
            #print(s)
            if s > target:
                big_idx -= 1
            elif s < target:
                small_idx += 1
            else:
                return [small_idx + 1, big_idx + 1]



