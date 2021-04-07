# https://leetcode.com/problems/word-search-ii/
# 212. Word Search II


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board[0]), len(board)
        answer = list()
        for word in words:
            stack = list()
            visited = list()
            start_coords = [(j, i) for i in range(m) for j in range(n) if board[j][i] == word[0]]
            i = 0
            for coord in start_coords:
                stack.append((i, coord))
            # print('stack', stack)
            while stack:
                item = stack.pop()
                if item[0] == len(word) - 1:
                    answer.append(word)
                    break
                # print('item', item)

                item_y, item_x = item[1][0], item[1][1]
                # print(m, n, item_y, item_x)
                if item_y < n - 1 and board[item_y + 1][item_x] == word[i + 1]:
                    if (item_y + 1, item_x) not in [v[1] for v in visited]:
                        stack.append((i + 1, (item_y + 1, item_x)))
                if item_y > 0 and board[item_y - 1][item_x] == word[i + 1]:
                    if (item_y - 1, item_x) not in [v[1] for v in visited]:
                        stack.append((i + 1, (item_y - 1, item_x)))
                if item_x < m - 1 and board[item_y][item_x + 1] == word[i + 1]:
                    if (item_y, item_x + 1) not in [v[1] for v in visited]:
                        stack.append((i + 1, (item_y, item_x + 1)))
                if item_x > 0 and board[item_y][item_x - 1] == word[i + 1]:
                    if (item_y, item_x - 1) not in [v[1] for v in visited]:
                        stack.append((i + 1, (item_y, item_x - 1)))
                print('stack after', stack)
                if stack:
                    if stack[len(stack) - 1][0] == item[0] + 1:
                        visited.append(item)
                        i += 1
                else:
                    if visited:
                        visited.pop()
                    i -= 1
                print('visited', visited)
        return sorted(answer)


if __name__ == '__main__':
    # print(Solution().findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
    #                                   ["i", "f", "l", "v"]], words=["oath", "eat", "pea", "rain"]))
    # print(Solution().findWords(board=[["a", "a"]], words=["aa"]))
    # print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
    #                            ["oath", "pea", "eat", "rain"]))
    # print(Solution().findWords([["a", "a"]], ["aaa"]))
    print(Solution().findWords([["a", "a"], ["a", "a"]], ["aaaaa"]))

    # print(Solution().findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
    #                                   ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]))
