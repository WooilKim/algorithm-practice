import re


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {key: value for key, value in knowledge}
        for m in re.findall(r"\(([a-z]+)\)", s):
            if m in d:
                s = s.replace(f'({m})', d[m])
            else:
                s = s.replace(f'({m})', '?')
        return s


print(Solution().evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
