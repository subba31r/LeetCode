class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # print(meetings)
        temp = [meetings[0]]
        for st, en in meetings:
            pre = temp[-1][1]
            if st<=pre:
                temp[-1][1] = max(pre,en)
            else:
                temp.append([st,en])
        # print(temp)
        pre = temp[0][1]
        count = temp[0][0] - 1
        for i in range(1,len(temp)):
            count = count + (temp[i][0]-pre-1)
            pre = temp[i][1]
        count = count + (days-pre)
        return count