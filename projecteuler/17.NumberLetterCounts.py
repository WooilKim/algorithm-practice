"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


def number_letter_counts(n):
    d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred', 1000: 'onethousand'}
    ans = 0
    for i in range(1, n + 1):
        print(i, end=' ')
        s = ''
        if i in d:
            ans += len(d[i])
            s = d[i]
        else:
            if i >= 100:
                ans += len(d[i // 100])
                ans += len(d[100]) - 3
                s += d[i // 100]
                s += d[100][3:]
                i %= 100
                if i > 0:
                    ans += len('and')
                    s += 'and'
            if i >= 20:
                ans += len(d[i // 10 * 10])
                s += d[i // 10 * 10]
                i %= 10
                if i != 0:
                    ans += len(d[i])
                    s += d[i]
            elif i > 0:
                ans += len(d[i])
                s += d[i]
        print(s, ans)

    return ans


if __name__ == '__main__':
    print(number_letter_counts(5))
    print(number_letter_counts(1000))
