class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = {}
        # count = [0]*26
        # for s in strs:
        #     for c in s:
        #         num = ord(c) - ord('a')
        #         print(num, count[num])

        #         count[num] = count[num]+1

        #     string_array = [str(x) for x in count]
        #     result_string = '#'.join(string_array)
        #     if result_string not in dic:
        #         dic[result_string] = [s]
        #     else:
        #         dic[result_string].append(s)
        #     count = [0]*26
        # res = []
        # for k in dic:
        #     res.append(dic[k])
        # return res

        dic = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            string_array = [str(x) for x in count]
            result_string = '#'.join(string_array)
            dic[result_string].append(s)
        return list(dic.values())
            

                    
        