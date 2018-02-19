#!/usr/bin/env python3
#
# Given numRows, generate the first numRows of Pascal's triangle.
# for example, given numRows = 5,
#   [     [1],
#        [1,1],
#       [1,2,1],
#      [1,3,3,1],
#     [1,4,6,4,1]   ]

def pascals(num_rows):
    if num_rows == 0:
        return []

    triangle = [[1]]
    for row in range(1, num_rows):
        prev_row = triangle[row - 1]
        new_row = [1]      
        for idx in range(len(prev_row) - 1):
            new_row.append(prev_row[idx] + prev_row[idx + 1])
        new_row.append(1)  
        triangle.append(new_row)

    return triangle


# Tests
print(pascals(5))
print(pascals(0))
print(pascals(1))
print(pascals(2))
print(pascals(10))
