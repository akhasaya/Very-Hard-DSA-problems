# given a bunch of points, find rectangles parallel to x, y angles
# return area of rectangle that is minimum among those rectangles

def minimumAreaRectangle(points):
    points.sort()
    vertical_lines = {}
    areas = set()
    for index, (x1,y1) in enumerate(points):
        index2 = index+1
        while index2 < len(points) and x1 == points[index2][0]:
            x2, y2 = points[index2]
            if (y1,y2) in vertical_lines.keys():
                prev_x = vertical_lines[(y1,y2)]
                areas.add(abs(y2-y1)*abs(x1-prev_x))
            vertical_lines[(y1,y2)] = x1
            index2 += 1


    return min(areas) if len(areas) > 0 else 0
        