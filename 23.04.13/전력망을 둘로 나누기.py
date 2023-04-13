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

def solution(n, wires):
    answer = []
    area = []

    for i in range(len(wires)):
        root = {}
        parent = [i for i in range(n + 1)]

        for j in range(len(wires)):
            if i == j:
                continue
            union_parent(parent, wires[j][0], wires[j][1])

        for k in range(1, len(parent)):
            if find_parent(parent, parent[k]) in root:
                root[find_parent(parent, parent[k])] += 1
            else:
                root[find_parent(parent, parent[k])] = 1

        area = list(root.values())
        answer.append(abs(area[0] - area[1]))
    return min(answer)


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
