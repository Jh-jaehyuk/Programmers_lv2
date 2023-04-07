def solution(files):
    arr = [[] for _ in range(len(files))]
    answer = []
    idx = 0
    for file in files:
        head = ''
        number = ''

        for i in range(len(file)):
            if file[i].isdigit():
                arr[idx].append(idx)
                arr[idx].append(head.lower())
                break
            else:
                head += file[i]

        for j in range(i, len(file)):
            if file[j].isdigit():
                number += file[j]
            else:
                arr[idx].append(int(number))
                break
            if len(number) == 5:
                arr[idx].append(int(number))
                break
        else:
            arr[idx].append(int(number))
        idx += 1

    arr = sorted(arr, key=lambda x:(x[1], x[2], x[0]))

    for k in arr:
        answer.append(files[k[0]])

    return answer


print(solution(["F13.png", "F14", "f013", "F014", "F013.TXT"]))

# 정규표현식을 이용한 head, number, tail 구분하기
# import re
#
# def solution(files):
#
#     def key_function(fn):
#         head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
#         return [head,int(number)]
