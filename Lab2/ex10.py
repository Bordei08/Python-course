def maxLen(list):
    maxim = 0
    for x in list:
        if maxim < len(x):
            maxim = len(x)
    return maxim      

def makeTuples(*listIn):
    list = []
    for x in listIn:
        list.append(x)
    mLen = maxLen(list)
    totalList = []
    for x in list:
        totalList = totalList + x
        if len(x) < mLen:
            diff = mLen - len(x)
            while diff > 0:
                totalList.append("none")
                diff = diff - 1
    result = []
    for i in range(0, mLen):
        list1 = []
        for x in range(0, len(list)):
            list1.append(totalList[x*mLen + i])
        result.append(tuple(list1))            
    return result

print(makeTuples([1,2,3], [5,6,7], ["a", "b", "c"]))
print(makeTuples([1,2], [2,3,5]))
