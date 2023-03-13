# import numpy as np
def solution(arr1, arr2):
    # np_arr1 = np.matrix(arr1)
    # np_arr2 = np.matrix(arr2)
    # answer = (np.array(np_arr1 * np_arr2)).tolist()
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*arr2)] for X_row in arr1]
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
