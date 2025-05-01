class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
    
        def can_assign(k):
            """
            Check if we can assign k tasks to k workers (using pills if needed).
            """
            available_workers = SortedList(workers[-k:])  # Take k strongest workers
            pills_left = pills
            
            for i in range(k - 1, -1, -1):  # Start from hardest task
                task_req = tasks[i]
                
                # Check if the strongest available worker can do it without pill
                if available_workers[-1] >= task_req:
                    available_workers.pop(-1)
                # Else, check if weakest worker + pill can handle it
                elif pills_left > 0:
                    idx = available_workers.bisect_left(task_req - strength)
                    if idx == len(available_workers):
                        return False  # No suitable worker even with pill
                    available_workers.pop(idx)
                    pills_left -= 1
                else:
                    return False  # No pill left, cannot assign task
            return True
        
        # Binary search for maximum k
        left, right = 0, min(len(tasks), len(workers))
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
