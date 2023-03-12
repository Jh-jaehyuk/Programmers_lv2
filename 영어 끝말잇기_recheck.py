def solution(n, words):
    start = [words[0][0]]
    for idx, word in enumerate(words):
        if word not in start and start[-1][-1] == word[0]:
            start.append(word)
        else:
            return [idx % n + 1, (idx//n) + 1]
    return [0, 0]

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
