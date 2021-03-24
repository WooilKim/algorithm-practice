# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, A: list[int], K: int) -> int:
        M = 0
        l = [[], []]

        zeros = list()
        ones = list()
        flag = 1
        cnt = 0
        for i, a in enumerate(A):
            if a != flag:
                l[flag].append(cnt)
                flag = a
                cnt = 1
            else:
                cnt += 1
        l[A[-1]].append(cnt)
        print(l)
        print(len(l[0]), len(l[1]))

        for i in range(len(l[1])):
            if i == 0:
                M = l[1][0]
                continue
            j = i
            k_left = K
            while k_left > 0 and j > 0:
                k_left -= l[0][j - 1]
                j -= 1
            if k_left >= 0:
                if len(l[0]) > i:
                    s = sum(l[1][j:i + 1]) + K - max(0, k_left - l[0][i])
                else:
                    s = sum(l[1][j:i + 1]) + K - k_left
            else:
                s = sum(l[1][j + 1:i + 1]) + K
            print(j, i, s, k_left)
            M = max(M, s)
        return M


