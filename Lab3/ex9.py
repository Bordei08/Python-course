def ex9(*input1, **input2):
    counter = 0
    for value in input1:
        if value in input2.values():
            counter += 1
    return counter


print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))