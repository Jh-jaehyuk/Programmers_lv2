# 크루스칼 알고리즘 이용
# 크루스칼 알고리즘은 간선의 개수가 E개일 때, O(ElogE)의 시간 복잡도를 가짐.
# 간선을 정렬하는 부분(sort 함수 이용)이 O(NlogN)의 시간 복잡도를 가지기 때문.


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x] # 경로 압축 >> 시간복잡도 이득


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    parent = [0] * (n + 1)
    edges = []
    result = 0

    for i in range(1, n + 1):
        parent[i] = i

    for i in costs:
        a, b, cost = i
        edges.append((cost, a, b))
        edges.append((cost, b, a))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
