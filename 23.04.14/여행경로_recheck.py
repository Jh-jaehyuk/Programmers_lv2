from collections import defaultdict


def solution(tickets):
    answer = []
    # {출발점: [도착점리스트]} 형태로 그래프 생성
    arr = defaultdict(list)
    for (s, e) in tickets:
        arr[s].append(e)
    # 도착점 리스트를 역순 정렬
    for i in arr.keys():
        arr[i].sort(reverse=True)
    # 출발지는 고정이므로 stack에 'ICN' 먼저 넣기
    stack = ['ICN']
    # DFS로 모든 노드 순회
    while stack:
        # 스택에서 가장 위의 데이터 꺼내오기
        top = stack.pop()
        # top이 그래프에 없거나 top을 시작점으로 하는 티켓이 없는 경우 answer에 저장
        if top not in arr or not arr[top]:
            answer.append(top)
        # top을 다시 stack에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 stack에 저장
        else:
            stack.append(top)
            stack.append(arr[top].pop())
    # answer를 뒤집어서 반환
    return answer[::-1]



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
