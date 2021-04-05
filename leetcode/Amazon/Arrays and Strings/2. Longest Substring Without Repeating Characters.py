# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2961/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length


# Your runtime beats 63.57 % of python3 submissions.
# Your memory usage beats 26.12 % of python3 submissions.
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        M, i, j = 0, 0, 0
        queue = list()
        s = list(s)
        if len(s) == 1:
            return 1
        while j < len(s):
            if s[j] not in queue:
                queue.append(s[j])
            else:
                M = max(M, j - i)
                while True:
                    i += 1
                    if queue.pop(0) == s[j]:
                        break

                queue.append(s[j])
            j += 1

        return max(M, len(queue))


if __name__ == '__main__':
    # print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
    # print(Solution().lengthOfLongestSubstring(s="bbbbb"))
    # print(Solution().lengthOfLongestSubstring(s="pwwkew"))
    # print(Solution().lengthOfLongestSubstring(s=""))
    # print(Solution().lengthOfLongestSubstring(s=" "))
    print(Solution().lengthOfLongestSubstring(s="au"))
