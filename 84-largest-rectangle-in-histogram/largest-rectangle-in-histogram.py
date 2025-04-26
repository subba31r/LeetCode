class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # https://www.youtube.com/watch?v=zx5Sw9130L0
        #creating a stack to keep track of both index and height position of the array
        stack = []
        area = 0
        for i in range(0,len(heights)):
            if len(stack) == 0:
                stack.append([i,heights[i]])
            prevIdx = i
            #here we need to consider both the left and right till where
            #the curretn rectangle can expand to calculate the area
            
            #if there is an element in top of the stack which height is greater
            #than the current element height the previous cannot extend further
            #so we start popping those elemnets that are higher than the current
            #and we insert the index of the current with respect to the index
            #till where we popped the last element in the stack
            #so that it makes easier for us to calculate the area 
            while stack and stack[-1][1] > heights[i]:
                curr = stack.pop()
                currArea = curr[1]*(i-curr[0])
                area = max(currArea,area)
                prevIdx = curr[0]
            stack.append([prevIdx,heights[i]])

        while stack:
            curr=stack.pop()
            currArea = curr[1]*(len(heights)-curr[0])
            area = max(currArea,area)
        return area


        