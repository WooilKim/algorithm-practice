# https://leetcode.com/problems/text-justification/

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, j = 0, 0
        ans = list()
        queue = list()
        while i < len(words) and j < len(words):
            if not queue or sum(queue) + len(queue) - 1 < maxWidth:
                queue.append(len(words[j]))
                j += 1
            else:
                spaces = maxWidth - sum(queue[:-1])
                r, k = spaces // (len(queue) - 2), spaces % (len(queue) - 2)
                if k == 0:
                    ans.append((' ' * r).join(words[i:j - 1]))
                else:
                    ans.append((' ' * (r + 1)).join(words[i:i + k])
                               + ' ' * r
                               + (' ' * r).join(words[i + k:j - 1]))
                queue = [queue[-1]]
                i = j - 1

        spaces = maxWidth - sum(queue)
        r, k = spaces // (len(queue)), spaces % (len(queue))
        if k == 0:
            ans.append((' ' * r).join(words[i:j - 1]))
        else:
            ans.append((' ' * (r + 1)).join(words[i:i + k])
                       + ' ' * r
                       + (' ' * r).join(words[i + k:j - 1]))
            # print(ans)
        return ans


if __name__ == '__main__':
    print(Solution().fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
