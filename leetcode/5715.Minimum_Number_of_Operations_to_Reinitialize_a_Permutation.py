class Solution:
    def reinitializePermutation(self, n: int) -> int:
        i = 0
        perm = list(range(n))
        arr = list(range(n))
        while i < n:
            if i % 2 == 0:
                arr[i] = perm[i // 2]
            else:
                arr[i] = perm[n // 2 + (i - 1) // 2]
            print(arr)

            i += 1
            perm = [x for x in arr]


print(Solution().reinitializePermutation(n=6))
