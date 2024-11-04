# 2D Lists

number_grid = [    # Creating 2D Lists
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])   # Accessing elements in a 2D list. We start with the row index then column index. we are accessing 2.

# Nested for loop - for loop inside another for loop

for row in number_grid:    
    for col in row:
        print(col)