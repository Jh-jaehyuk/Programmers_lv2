import re
from itertools import permutations

def solution(user_id, banned_id):
    arr = '/'.join(banned_id).replace('*', '.')
    answer = set()

    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(arr, '/'.join(i)):
            answer.add(''.join(sorted(i)))

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
