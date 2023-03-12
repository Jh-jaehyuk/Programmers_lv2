def solution(brown, yellow):
    w, h = int((brown + yellow)**0.5), int((brown + yellow)**0.5)
    while w >= h:
        if w * h == brown + yellow and (w - 2) * (h - 2) == yellow:
            return [w, h]
        elif w * h >= brown + yellow:
            h -= 1
        elif w * h < brown + yellow:
            w += 1

    answer = [w, h]
    return answer

print(solution(18, 6))
