# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)

        left, right = 0, m
        mid = (m + n + 1) // 2

        while left <= right:

            s1_sep = left + (right - left) // 2
            s2_sep = mid - s1_sep

            s1Left = float("-inf") if s1_sep == 0 else nums1[s1_sep - 1]
            s1Right = float("inf") if s1_sep == m else nums1[s1_sep]
            s2Left = float("-inf") if s2_sep == 0 else nums2[s2_sep - 1]
            s2Right = float("inf") if s2_sep == n else nums2[s2_sep]

            if s1Left <= s2Right and s2Left <= s1Right:
                if (m + n) % 2 == 0:
                    return (max(s1Left, s2Left) + min(s1Right, s2Right)) / 2
                else:
                    return max(s1Left, s2Left)

            elif s1Left > s2Right:
                right = s1_sep - 1

            elif s2Left > s1Right:
                left = s1_sep + 1

        # Method 1 ( time: log(min(m,n)), space: O(1) )


#         if len(nums1) > len(nums2):
#             return self.findMedianSortedArrays(nums2, nums1)

#         m, n = len(nums1), len(nums2)

#         left_size = (m + n + 1) // 2
#         left, right = 0, m

#         while left <= right:
#             a_sep = left + (right - left) // 2
#             b_sep = left_size - a_sep

#             aleftmax = float("-inf") if a_sep == 0 else nums1[a_sep - 1]
#             arightmin = float("inf") if a_sep == m else nums1[a_sep]
#             bleftmax = float("-inf") if b_sep == 0 else nums2[b_sep - 1]
#             brightmin = float("inf") if b_sep == n else nums2[b_sep]

#             if aleftmax <= brightmin and bleftmax <= arightmin:
#                 if (m + n) % 2 != 0:
#                     return max(aleftmax, bleftmax)
#                 else:
#                     return (max(aleftmax, bleftmax) + min(arightmin, brightmin))/ 2
#             elif aleftmax > brightmin:
#                 right = a_sep - 1
#             elif bleftmax > arightmin:
#                 left = a_sep + 1


#         # merge sort (O(m+n), O(m+n))
#         if not nums1 and not nums2:
#             return []

#         m, n = len(nums1), len(nums2)
#         pt1, pt2 = 0, 0
#         com = []

#         while pt1 < m and pt2 < n:

#             if nums1[pt1] < nums2[pt2]:

#                 com.append( nums1[pt1] )
#                 pt1 += 1

#             else:

#                 com.append( nums2[pt2] )
#                 pt2 += 1

#         com = com + (nums1[pt1:] or nums2[pt2:])

#         N = len(com)

#         return float( com[N//2] ) if N%2 == 1 else float( (com[N//2-1] + com[N//2])/2 )


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
    print(Solution().findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]))
    print(Solution().findMedianSortedArrays(nums1=[], nums2=[1]))
    print(Solution().findMedianSortedArrays(nums1=[2], nums2=[]))
    print(Solution().findMedianSortedArrays([3], [-2, -1]))
