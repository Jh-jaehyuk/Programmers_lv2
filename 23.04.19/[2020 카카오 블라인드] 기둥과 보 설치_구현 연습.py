# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 설치된 것이 기둥인 경우
        if stuff == 0:
            # 바닥 위 혹은 보의 한쪽 끝 부분 위 혹은 다른 기둥 위 라면 가능
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            # 아니면 불가능
            return False
        # 설치된 것이 보인 경우
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 가능
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            # 아니면 불가능
            return False
    return True


def solution(n, build_frame):
    answer = []
    # frame의 개수는 최대 1000개
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제하는 경우라면
        if operate == 0:
            # 일단 삭제를 해보고
            answer.remove([x, y, stuff])
            # 삭제한 구조물이 가능하지 않다면
            if not possible(answer):
                # 다시 설치
                answer.append([x, y, stuff])
        # 설치하는 경우라면
        elif operate == 1:
            # 일단 설치해보고
            answer.append([x, y, stuff])
            # 설치된 구조물이 가능하지 않다면
            if not possible(answer):
                # 다시 삭제
                answer.remove([x, y, stuff])
    # 정렬된 결과를 반환
    return sorted(answer)
