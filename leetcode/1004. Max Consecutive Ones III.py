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
        cnt = 0
        k_left = 0
        for zero_cnt in l[0]:
            k_left = zero_cnt
            if zero_cnt < K:
                if A[0] == 0:
                    cnt =
                else:
                    cnt
        #
        # for i, a in enumerate(A):
        #     cnt = 0
        #     j = i
        #     while cnt <= K:
        #         if j == len(A):
        #             break
        #         if A[j] == 0:
        #             cnt += 1
        #             if cnt > K:
        #                 break
        #         j += 1
        #     M = max(j - i, M)
        # return M
        return


print(Solution().longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
print(Solution().longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))
