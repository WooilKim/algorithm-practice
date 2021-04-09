# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2968/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        qi = -1
        ans = 0
        if haystack == needle or needle == "":
            return 0
        elif len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[qi + 1]:
                qi += 1
            else:
                if qi > -1:
                    i -= qi + 1
                qi = -1
                ans = -1
                i += 1
                continue
            if qi == len(needle) - 1:
                ans = i - qi
                break
            i += 1
        return ans


if __name__ == '__main__':
    print(Solution().strStr(haystack="hello", needle="ll"))
    print(Solution().strStr(haystack="aaaaa", needle="bba"))
    print(Solution().strStr(haystack="", needle=""))
    print(Solution().strStr(haystack="", needle="a"))
    print(Solution().strStr(haystack="a", needle=""))
    print(Solution().strStr(haystack="mississippi", needle="issip"))
    print(Solution().strStr(haystack="mississippi", needle="pi"))
