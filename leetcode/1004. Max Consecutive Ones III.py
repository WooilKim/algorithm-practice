# https://leetcode.com/problems/max-consecutive-ones-iii/


# Runtime: 524 ms, faster than 99.92% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 14.7 MB, less than 72.92% of Python3 online submissions for Max Consecutive Ones III.
class Solution:
    def longestOnes(self, A: list[int], K: int) -> int:
        left = right = 0

        for right in range(len(A)):
            # if we encounter a 0 the we decrement K
            if A[right] == 0:
                K -= 1
            # else no impact to K

            # if K < 0 then we need to move the left part of the window forward
            # to try and remove the extra 0's
            if K < 0:
                # if the left one was zero then we adjust K
                if A[left] == 0:
                    K += 1
                # regardless of whether we had a 1 or a 0 we can move left side by 1
                # if we keep seeing 1's the window still keeps moving as-is
                left += 1

        return right - left + 1


# # Runtime: 648 ms, faster than 46.62% of Python3 online submissions for Max Consecutive Ones III.
# # Memory Usage: 14.8 MB, less than 39.44% of Python3 online submissions for Max Consecutive Ones III.
# class Solution(object):
#     def longestOnes(self, A: list[int], K: int) -> int:
#         start = 0
#         cnt = 0
#         end = 0
#         M = 0
#         while end < len(A):
#             if A[end] == 0:
#                 cnt += 1
#                 end += 1
#                 while cnt > K and start < end:
#                     if A[start] == 0:
#                         cnt -= 1
#                     start += 1
#             else:
#                 end += 1
#
#             M = max(M, end - start)
#
#         return M


# Runtime: 568 ms, faster than 88.45% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 14.9 MB, less than 11.71% of Python3 online submissions for Max Consecutive Ones III.
# class Solution(object):
#     def longestOnes(self, A, K):
#         i = 0
#         for j in range(len(A)):
#             K -= 1 - A[j]
#             if K < 0:
#                 K += 1 - A[i]
#                 i += 1
#         return j - i + 1
# Runtime: 560 ms, faster than 92.42% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 15.4 MB, less than 5.96% of Python3 online submissions for Max Consecutive Ones III.
# class Solution(object):
#     def longestOnes(self, A: list[int], K: int) -> int:
#         zero_indices = [-1] + [i for i in range(len(A)) if A[i] == 0] + [len(A)]
#
#         if K >= len(zero_indices) - 2:
#             return len(A)
#
#         maxZeros = 0
#
#         for i in range(K, len(zero_indices) - 1):
#             zeros = zero_indices[i + 1] - zero_indices[i - K] - 1
#             maxZeros = max(zeros, maxZeros)
#
#         return maxZeros


# class Solution:
#     def longestOnes(self, A: list[int], K: int) -> int:
#         l = [[], []]
#         flag = 1
#         cnt = 0
#         for i, a in enumerate(A):
#             if a == flag:
#                 cnt += 1
#             else:
#                 l[flag].append(cnt)
#                 flag = a
#                 cnt = 1
#         l[A[-1]].append(cnt)
#         M = l[1][0]
#         for i in range(1, len(l[1])):
#             j = i
#             k_left = K
#             while k_left > 0 and j > 0:
#                 k_left -= l[0][j - 1]
#                 j -= 1
#             if k_left >= 0:
#                 if len(l[0]) > i:
#                     s = sum(l[1][j:i + 1]) + K - max(0, k_left - l[0][i])
#                 else:
#                     s = sum(l[1][j:i + 1]) + K - k_left
#             else:
#                 s = sum(l[1][j + 1:i + 1]) + K
#             M = max(M, s)
#         return M


print(Solution().longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
print(Solution().longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))
print(Solution().longestOnes(A=[0, 0, 0, 1], K=4))
