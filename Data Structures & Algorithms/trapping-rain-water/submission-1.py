class Solution:
    def trap(self, height: List[int]) -> int:

        #Front traverse, back traverse, take min at each index!
        
        
        forward = []
        prev_high = 0
        

        for h in height:
            if h >= prev_high:
                prev_high = h
                forward.append(0)
            else:
                forward.append(prev_high - h)
            
        rev = height[::-1]
        backward = []
        prev_high = 0

        for h in rev:
            if h >= prev_high:
                prev_high = h
                backward.append(0)
            else:
                backward.append(prev_high - h)

        
        total = 0
        backward.reverse()
        for i in range(len(forward)):
            total += min(forward[i], backward[i])

        #print(forward, backward)
        return total
