class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def checkCuts(rectangles, dim):
            count = 0
            rectangles.sort(key=lambda x : x[dim])
            end = rectangles[0][dim+2]

            for i in range(1,len(rectangles)):
                temp = rectangles[i]

                if end <= temp[dim]:
                    count += 1
                
                end = max(end,temp[dim+2])
            if count >= 2:
                return True
            return False
        return checkCuts(rectangles,0) or checkCuts(rectangles,1)