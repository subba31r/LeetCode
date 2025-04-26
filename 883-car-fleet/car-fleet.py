class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos -> 0 3 5 8 10
        # spe -> 1 3 1 4 2
        # res -> 12 3 7 1 1
        arr = [[p] for p in position]
        for i in range(0,len(speed)):
            arr[i].append(speed[i])
        arr.sort()
        for i in range(0,len(arr)):
            arr[i] = (target-arr[i][0])/arr[i][1]
        print(arr)
        ele = arr.pop()
        res = 1
        while arr:
            poped = arr.pop()
            if poped > ele:
                res += 1
                ele = poped
        return res
