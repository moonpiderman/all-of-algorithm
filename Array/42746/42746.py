def solution(numbers):
    l = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(numbers)))


# a = [3, 30, 34, 5, 9]
a = [0, 0, 0, 0]

print(solution(a))
