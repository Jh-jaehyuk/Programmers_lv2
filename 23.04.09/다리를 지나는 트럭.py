from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque([0] * bridge_length)
    queue = deque(truck_weights)
    bridge_sum = 0

    while bridge_queue:
        answer += 1
        bridge_sum -= bridge_queue[0]
        bridge_sum += bridge_queue[-1]
        bridge_queue.popleft()

        if queue:
            if bridge_sum + queue[0] <= weight:
                bridge_queue.append(queue.popleft())

            else:
                bridge_queue.append(0)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
