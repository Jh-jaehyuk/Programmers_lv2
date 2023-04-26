def solution(plans):
    answer = []
    stack = []
    d = dict()

    for plan in plans:
        h, m = plan[1].split(":")
        plan[1] = int(h) * 60 + int(m) # 시간을 분으로 변경
        plan[2] = int(plan[2]) # 플레이타임을 int형으로 변환
        # 시작 시간을 key로 이름과 플레이타임을 value로 dict에 저장
        d[plan[1]] = [plan[0], plan[2]]
    # 시작 시간이 빠른 순서로 정렬
    plans.sort(key=lambda x: x[1])
    # 현재 시간을 첫번째 과제의 시작 시간으로 설정
    time = plans[0][1]
    # 과제를 다 하기 전까지 반복
    while len(answer) < len(plans):
        # 진행중인 과제가 있다면
        if stack:
            # 가장 마지막에 진행중이었던 과제의 시간을 -1 해줌
            stack[-1][1] -= 1
            # 그 과제의 시간이 0이 되면
            if stack[-1][1] == 0:
                # 그 과제의 이름을 진행중인 과제 목록에서 제거하고 정답에 추가
                answer.append(stack.pop()[0])
        # 현재 시간에 진행해야될 과제가 있다면
        if time in d:
            # 진행중인 과제 목록에 포함시킴
            stack.append(d[time])
        # 현재 시간을 1분 증가
        time += 1

    return answer


print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
