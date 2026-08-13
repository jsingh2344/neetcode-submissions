class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Criteria for a container: any pair can make a container, 
        # Water stored = Index difference * minimum height
        # Can't 'only go inside if one is bigger', because there could be a huge pair in the middle 



        # What about 'what will make the storage bigger' hypothesis?
        # + if nothing will, choose the 

        # No -- what will keep the minimum the highest
        # Something to not leave big numbers. Always leave the smaller number?

        # If you always leave the smaller number: 
        # Miss out on that smaller number + an intermediate, when 

        # 1 500 500 2 3 


        # 1 7 2 3 500 1 500 1





        s = 0
        e = len(heights) - 1

        max_store = 0

        while s < e:

            curr_store = (e - s) * min(heights[s], heights[e])
            #print(heights[s], heights[e], curr_store)
            if curr_store > max_store:
                max_store = curr_store
            if heights[s] > heights[e]:
                e -= 1
            else:
                s += 1
        return max_store

        