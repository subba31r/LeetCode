class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            count = ['0']*26
            for c in s:
                t = ord(c) - ord('a')
                count[t] = str(int(count[t]) + 1)
            hm["#".join(count)].append(s)
        return list(hm.values())
            