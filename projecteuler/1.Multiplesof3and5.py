# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def get_multiples_sum(a, b, limit):
    # print([k for k in range(0, limit, a)])
    # print([k for k in range(0, limit, b)])
    # print([k for k in range(0, limit, a * b)])
    return sum([k for k in range(0, limit, a)]) + sum([k for k in range(0, limit, b)]) - sum(
        [k for k in range(0, limit, a * b)])
    

if __name__ == '__main__':
    print(get_multiples_sum(3, 5, 10))
    print(get_multiples_sum(3, 5, 1000))
