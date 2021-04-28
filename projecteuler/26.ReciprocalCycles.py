"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def reciprocal_cycles():
    ans = list()
    for n in range(2, 1001):
        i = 1
        s = list()
        while True:
            d, m = divmod(i * 10, n)
            if m == 0:
                break
            if (d, m) in s:
                ans.append((n, len(s) - s.index((d, m))))
                # ans = max(ans, len(s) - s.index((d, m)))
                break
            else:
                s.append((d, m))
            i = m

    ans.sort(key=lambda x: (-x[1], x[0]))
    return ans


if __name__ == '__main__':
    print(reciprocal_cycles())
