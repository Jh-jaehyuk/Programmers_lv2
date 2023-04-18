# 남아있는 풍선의 번호가 그 풍선 좌, 우측의 최솟값보다 작으면 안됨.


def solution(a):
    answer = 1

    left_idx = 0
    right_idx = len(a) - 1

    min_left = a[left_idx]
    min_right = a[right_idx]

    while left_idx < right_idx:
        if min_left < min_right:
            right_idx -= 1
            right = a[right_idx]
            if right < min_right:
                answer += 1
                min_right = right

        else:
            left_idx += 1
            left = a[left_idx]
            if left < min_left:
                answer += 1
                min_left = left

    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
