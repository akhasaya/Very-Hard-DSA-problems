def lineThroughPoints(points):
    lines = {}    
    for index in range(len(points)):
        for index2 in range(index, len(points)):
            m, c = 0,0
            i = points[index]
            j = points[index2]
            if i[0] == j[0]:
                m = float("inf")
                c = i[0]
            else:
                m = (j[1]-i[1])/(j[0]-i[0])
                c = i[1] - m * i[0]

            string = f"{m}x{c}"
            if string not in lines.keys():
                lines[string] = set()
            lines[string].add(tuple(i))
            lines[string].add(tuple(j))
    
    maxx = float("-inf")
    for values in lines.values():
        if len(values) > maxx :
            maxx = len(values)

    return maxx
                
                
                

    