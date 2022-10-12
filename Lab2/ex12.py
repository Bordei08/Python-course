def solve(list):
    result = []
    i = 0
    while i < len(list):
        list1 = []
        list1.append(list[0])
        clist = []
        clist.append(list[0])
        list.remove(list1[0])
        j = 0
        while j < len(list):
            list1.append(list[j])
            if list1[0][len(list1[0]) - 1] == list1[1][len(list1[1]) - 1] and list1[0][len(list1[0]) - 2] == list1[1][len(list1[1]) - 2]:
                result.append(list1)
            list1 = clist.copy()
            j = j + 1
        
    print(result)          

solve(['ana', 'banana', 'carte', 'arme', 'parte'])