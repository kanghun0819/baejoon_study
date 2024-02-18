def solution(n, times):
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        total_people = 0

        for time in times:
            total_people += mid // time

        if total_people >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left
