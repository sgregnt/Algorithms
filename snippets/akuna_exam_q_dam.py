def process_segment(l, r, l_h, r_h):
    """Auxillary function to process single walls segment.

     r, r_h right wall position and its height
     l, l_h left wall position and its height
    """

    # free distance between walls
    dist_d = (r - l) - 1

    if dist_d < 1:
        return 0

    heights = sorted([r_h, l_h])
    # wall height difference

    heights_d = heights[1] - heights[0]

    # check if enough free space between walls
    # to fill in the diff
    if heights_d - 1 > dist_d:
        return -1

    # available space to construct
    # up and down stairs
    free = dist_d - (heights_d)

    if free > 0:  # can build up and down stairs
        stairs_half = (free-1) // 2
        total_raise = heights[1] + 1 + stairs_half
        return total_raise
    else:  # cant't build stairs
        if free == 0:
            return heights[1]
        elif free == -1:
            return heights[0] + heights_d
        else:
            return heights[0] + heights_d - 1

# wallPositions = [1, 2, 4, 7]
# wallPositions = [0, 7]
wallPositions = [0, 5]
# wallHeights = [4, 6, 8, 11]
wallHeights = [3, 4]

n = len(wallPositions)
heights = []
for i in range(1, n):

    l, l_h = wallPositions[i-1], wallHeights[i-1]
    r, r_h = wallPositions[i],  wallHeights[i]

    res = process_segment(l, r, l_h, r_h)
    if res < 0:
        print("problem")
        1/0
    else:
        heights.append(res)

print(max(heights))
#
# r = 1
# l = 0
# r_h = 0
# l_h = 3
# print(max_segment(l, r, l_h, r_h))


