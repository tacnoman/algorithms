# Function to add bombs in a empty area
def mine_sweeper(bombs, num_rows, num_cols):
    board = [
        [0 for x in range(0, num_cols)] for y in range(0, num_rows)
    ]

    for bomb in bombs:
        row_i = bomb[0]
        col_i = bomb[1]
        board[row_i][col_i] = -1

        for col in range(max(row_i-1, 0), min(row_i+2, num_rows)):
            for row in range(max(col_i-1, 0), min(col_i+2, num_cols)):
                if (board[col][row] == -1):
                    continue
                board[col][row] += 1

    return board


bombs = [
    [0, 2],
    [1, 1],
]

board_with_bombs = mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)

print(board_with_bombs)
