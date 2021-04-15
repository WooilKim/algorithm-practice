# https://leetcode.com/problems/compare-version-numbers/
# Runtime: 28 ms, faster than 80.32% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 14.2 MB, less than 60.47% of Python3 online submissions for Compare Version Numbers.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        while v1 or v2:
            rev1 = v1.pop(0) if v1 else None
            rev2 = v2.pop(0) if v2 else None
            if not rev1 and rev2:
                if int(rev2) == 0:
                    continue
                else:
                    return -1
            elif rev1 and not rev2:
                if int(rev1) == 0:
                    continue
                else:
                    return 1
            elif int(rev1) < int(rev2):
                return -1
            elif int(rev1) > int(rev2):
                return 1
            else:
                continue
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion(version1="1.01", version2="1.001"))
    print(Solution().compareVersion(version1="1.0", version2="1.0.0"))
    print(Solution().compareVersion(version1="0.1", version2="1.1"))
    print(Solution().compareVersion(version1="1.0.1", version2="1"))
    print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))
