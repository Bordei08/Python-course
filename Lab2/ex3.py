def intersection(a, b):
    result = []
    for i in range(0, len(a)):
        if a[i] in b:
            result.append(a[i])
    return result


def reunion(a, b):
    result = list(set(a) | set(b))
    return result


def minus(a,b):
    result = a
    for i in range(0, len(a)):
        if a[i] in b:
            result.remove(a[i])
    return result



def solution(a,b):
    return intersection(a,b), reunion(a,b), minus(a,b), minus(a,b)

print(solution([1,2], [2,3]))

