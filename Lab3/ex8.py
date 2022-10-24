def ex8(input):
    viz = []
    if 'start' not in input.keys():
        return "'start' key not found!"

    key = input.get('start')
    viz.append(key)
    while True:
        if input.get(key) is None:
            return 'No loop found!'
        if input.get(key) in viz:
            return viz
        key = input.get(key)
        viz.append(key)

print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))        