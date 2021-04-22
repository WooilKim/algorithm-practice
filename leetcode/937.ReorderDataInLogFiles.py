# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List


class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def sorting_algorithm(log):
            left_side, right_side = log.split(" ", 1)

            if right_side[0].isalpha():
                return (0, right_side, left_side)
            else:
                return (1,)

        return sorted(logs, key=sorting_algorithm)


# Runtime: 72 ms, faster than 5.38% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 14.5 MB, less than 10.05% of Python3 online submissions for Reorder Data in Log Files.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_letter = list()
        logs_digit = list()
        for log in logs:
            log = log.split()
            if log[1].isdigit():
                logs_digit.append(log)
            else:
                logs_letter.append(log)
        logs_letter.sort(key=lambda x: (
            x[1:],
            x[0]
        ))
        return [' '.join(l) for l in logs_letter + logs_digit]


if __name__ == '__main__':
    print(Solution().reorderLogFiles(
        logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
