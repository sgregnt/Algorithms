#
# Complete the 'maxHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY wallPositions
#  2. INTEGER_ARRAY wallHeights
#
#
# def maxHeight(wallPositions, wallHeights):
#     # Write your code here
#
#     def process_segment(l, r, l_h, r_h):
#         """Auxillary function to process single walls segment.
#
#          r, r_h right wall position and its height
#          l, l_h left wall position and its height
#         """
#
#         # free distance between walls
#         dist_d = (r - l) - 1
#
#         if dist_d < 1:
#             return 0
#
#         heights = sorted([r_h, l_h])
#         # wall height difference
#
#         heights_d = heights[1] - heights[0]
#
#         # check if enough free space between walls
#         # to fill in the diff
#         if heights_d - 1 > dist_d:
#             return -1
#
#         # available space to construct
#         # up and down stairs
#         free = dist_d - (heights_d)
#
#         # can build up and down stairs
#         if free > 0:
#             stairs_half = (free - 1) // 2
#             total_raise = heights[1] + 1 + stairs_half
#             return total_raise
#
#         else:  # cant't build stairs
#             if free == 0:
#                 return heights[1]
#             elif free == -1:
#                 return heights[0] + heights_d
#             else:
#                 return heights[0] + heights_d - 1
#
#     n = len(wallPositions)
#
#     if n < 2:
#         return 0
#
#     heights = []
#
#     for i in range(1, n):
#
#         l, l_h = wallPositions[i - 1], wallHeights[i - 1]
#         r, r_h = wallPositions[i], wallHeights[i]
#
#         res = process_segment(l, r, l_h, r_h)
#         if res < 0:
#             return 0
#         else:
#             heights.append(res)
#
#     return max(heights)


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

        # distance to get even
        free = dist_d - (heights_d)

        # can build up and down stairs
        if free > 0:
            total_raise = heights[1] + free // 2 + free % 2
            return total_raise

        else:  # cant't build stairs
            if free == 0:
                return heights[1]
            elif free == -1:
                return heights[1] - 1
            else:
                pass

wallPositions = [0, 7]
wallHeights = [4, 4]
n = len(wallPositions)

heights = []

for i in range(1, n):

    l, l_h = wallPositions[i - 1], wallHeights[i - 1]
    r, r_h = wallPositions[i], wallHeights[i]
    res = process_segment(l, r, l_h, r_h)
    print(res)