#Import the modules here

from pprint import pprint

#Define the minesweeper grid and adjacent cells

Grid = [["-", "-", "-", "#", "#"],
           ["-", "#", "-", "-", "-"],
           ["-", "-", "#", "-", "-"],
           ["-", "#", "#", "-", "-"],
           ["-", "-", "-", "-", "-"]]

AdjacentCells = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (0, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]

#Function to count the mines around a specific grid location

def count_mines(mine_grid):
    mine_counts = []
    for row_number, row in enumerate(mine_grid):
        new_row = [count_neighbours(row_number, col_number, mine_grid) for col_number, col in enumerate(row)]
        mine_counts.append(new_row)
    return mine_counts

#Function that delivers a string of the count of the mines in the adjacent cells

def count_neighbours(row_number, col_number, mine_grid):
    count = 0
    if mine_grid[row_number][col_number] == "#":
        return "#"
    for dc, dr in AdjacentCells:
        r, c = row_number + dr, col_number + dc
        if r < 0 or c < 0:
            continue
        try:
            count += 1 if mine_grid[r][c] == "#" else 0
        except IndexError:
            pass
    return str(count)

result = count_mines(Grid)
pprint(result)