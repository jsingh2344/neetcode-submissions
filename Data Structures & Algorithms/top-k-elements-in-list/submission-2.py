class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        sorted_counts = sorted(counts.items(), reverse=True, key=lambda item:item[1])
        

        selected_tuples = sorted_counts[:k]
        selected_nums = []
        for (a, b) in selected_tuples:
            selected_nums.append(a)

        return selected_nums
        