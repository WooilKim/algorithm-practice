# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, A: list[int], K: int) -> int:
        l = [[], []]
        flag = 1
        cnt = 0
        for i, a in enumerate(A):
            if a == flag:
                cnt += 1
            else:
                l[flag].append(cnt)
                flag = a
                cnt = 1
        l[A[-1]].append(cnt)
        M = l[1][0]
        for i in range(1, len(l[1])):
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
            M = max(M, s)
        return M


print(Solution().longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
print(Solution().longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))
print(Solution().longestOnes(A=[0, 0, 0, 1], K=4))
