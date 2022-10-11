def  compose(notes, positions, startPosition):
    i = startPosition
    result = []
    while len(result) < len(notes) :
        result.append(notes[i])
        if len(positions) > 0:
            i = i + positions[0]
            positions.pop(0)
        if i >= len(notes):
            i = int(i % 5)  
    return result    

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))    