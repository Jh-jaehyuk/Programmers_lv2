# Linked-list 개념 정리에 좋은 문제
# 나중에 작동 원리에 대해 더 알아봐야 될 듯.
def solution(n, k, cmd):
    answer = ["O"] * n
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    tmp = []

    for command in cmd:
        command = command.split()

        if command[0] == "D":
            for _ in range(int(command[1])):
                k = linked_list[k][1]

        elif command[0] == "U":
            for _ in range(int(command[1])):
                k = linked_list[k][0]

        elif command[0] == "C":
            left, right = linked_list[k]
            answer[k] = "X"
            tmp.append((left, k, right))

            if right == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if left == -1:
                linked_list[right][0] = left
            elif right == n:
                linked_list[left][1] = right
            else:
                linked_list[left][1] = right
                linked_list[right][0] = left

        else:
            left, idx, right = tmp.pop()
            answer[idx] = "O"

            if left == -1:
                linked_list[right][0] = idx
            elif right == n:
                linked_list[left][1] = idx
            else:
                linked_list[left][1] = idx
                linked_list[right][0] = idx

    return "".join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
