def count_digits(A, n):
    digits = [0] * 10
    current_num = str(A)

    for _ in range(n):
        new_num = ""
        i = 0

        while i < len(current_num):
            j = i + 1
            while j < len(current_num) and current_num[i] == current_num[j]:
                j += 1

            count = j - i
            digits[int(current_num[i])] += count

            new_num += current_num[i] + str(count)
            i = j

        current_num = new_num

    return digits

A, n = map(int, input().split())
result = count_digits(A, n)
print(*result)
