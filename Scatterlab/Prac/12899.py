def solution(n):
    answer = ''
    country = [4, 1, 2]

    while n:
        answer = str(country[n % 3]) + answer
        if n % 3 == 0:
            n = (n // 3) - 1
        else:
            n = (n // 3)

    return answer

if __name__ == '__main__':
    ns = [1, 2, 3, 4]
    for n in ns:
        print(solution(n))