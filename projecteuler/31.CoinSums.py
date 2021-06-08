# https://projecteuler.net/problem=31
# Problem 31. Coin Sums


def coin_sums(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [1] + [0] * target

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]


if __name__ == '__main__':
    print(coin_sums(200))
