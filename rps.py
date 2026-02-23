def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def common_divisors(a, b):
    result = []
    limit = min(a, b)
    for i in range(1, limit + 1):
        if a % i == 0 and b % i == 0:
            result.append(i)
    return result


def divisors_upto(n):
    result = {}
    for i in range(1, n + 1):
        divs = []
        for j in range(1, i + 1):
            if i % j == 0:
                divs.append(j)
        result[i] = divs
    return result