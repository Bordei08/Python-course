def function(*list):
    totalList = []
    i = 0
    for x in list:
        if i < len(list) - 1:
            totalList = totalList + x
        i = i + 1
    i = 0
    result = []
    while i < len(totalList):
        if totalList.count(totalList[i]) == list[len(list) - 1]:
            result.append(totalList[i])
            totalList.remove(totalList[i])
        else:
            i = i + 1
    return result        



print(function([1,2],[3,4],[2,3], 2))        