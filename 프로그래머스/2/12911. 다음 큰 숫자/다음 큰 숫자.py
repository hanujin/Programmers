def solution(n):
    count = bin(n).count('1')

    number = n + 1

    while True:
        if bin(number).count('1') == count:
            return number

        number += 1