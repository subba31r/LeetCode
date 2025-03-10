class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #letter logs before digit logs
        map = defaultdict((list))
        for log in range(len(logs)):
            if logs[log].split()[1].isdigit():
                map["dig"].append(logs[log])
            else:
                map["let"].append(logs[log])
        
        map["let"].sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))

        return map["let"] + map["dig"]
