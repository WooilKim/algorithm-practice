from itertools import permutations


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        global memo
        memo = dict()
        global m
        m = 10 ** 9 + 7
        if primeFactors == 1:
            return 1
        if primeFactors % 3 == 1:
            n = primeFactors // 3 - 1
            return (self.multiply(n) * 4) % m
        elif primeFactors % 3 == 2:
            n = primeFactors // 3
            return (self.multiply(n) * 2) % m
        else:
            n = primeFactors // 3
            return (self.multiply(n)) % m
        return answer

    def multiply(self, n):
        if n in memo:
            return memo[n]
        if n < 3:
            return 3 ** n
        if n % 2 == 0:
            memo[n // 2] = self.multiply(n // 2) % m
            return (memo[n // 2] * memo[n // 2]) % m
        else:
            memo[n // 2] = self.multiply(n // 2) % m
            memo[n // 2 + 1] = self.multiply(n // 2 + 1) % m
            return (memo[n // 2] * memo[n // 2 + 1]) % m

    def test(n):
        return 3 ** n % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().maxNiceDivisors(545918790))
    # print(3 ** 40 % (10 ** 9 + 7))
    print(Solution().maxNiceDivisors(primeFactors=4))
    # print(Solution().maxNiceDivisors(primeFactors=5))
    # print(Solution().maxNiceDivisors(primeFactors=73))
    # print(Solution().maxNiceDivisors(primeFactors=7))
    # print(Solution().maxNiceDivisors(primeFactors=18))
    # print(Solution().maxNiceDivisors(primeFactors=1))
    # print(Solution().maxNiceDivisors(primeFactors=64))
    # print(Solution().maxNiceDivisors(primeFactors=545918790))
    # print(test(5) * test(5) % (10 ** 9 + 7))
    # print(3 ** 18 < 10 ** 9 + 7)
    # print(test(10))
