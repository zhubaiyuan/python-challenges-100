from common.print_array import print_array


def solve_sudoku(board):
    return _solve_sudoku_helper(board, 0, 0)


def _solve_sudoku_helper(board, start_row, start_col):
    if start_row > 8:
        return True
    row = start_row
    col = start_col
    while board[row][col] != 0:
        col += 1
        if col > 8:
            col = 0
            row += 1
            if row > 8:
                return True
    solved = False
    for num in range(1, 10):
        board[row][col] = num
        if is_valid_position(board):
            if col < 8:
                solved = _solve_sudoku_helper(board, row, col + 1)
            else:
                solved = _solve_sudoku_helper(board, row + 1, 0)
            if not solved:
                board[row][col] = 0
            else:
                return True
        else:
            board[row][col] = 0
    return False


def is_valid_position(board):
    return check_horizontally(board) and \
        check_vertically(board) and \
        check_boxes(board)


def check_horizontally(board):
    for row in range(9):
        row_values = [board[row][x] for x in range(9)]
        if not all_desired_numbers(row_values):
            return False
    return True


def check_vertically(board):
    for x in range(9):
        column_values = [board[row][x] for row in range(9)]
        if not all_desired_numbers(column_values):
            return False
    return True


def check_boxes(board):
    for y_box in range(3):
        for x_box in range(3):
            box_values = collect_box_values(board, y_box, x_box)
            if not all_desired_numbers(box_values):
                return False
    return True


def collect_box_values(board, y_box, x_box):
    box_values = []
    for y in range(3):
        for x in range(3):
            real_y = y_box * 3 + y
            real_x = x_box * 3 + x
            box_values.append(board[real_y][real_x])
    return box_values


def all_desired_numbers(all_collected_values):
    relevant_values = list(all_collected_values)
    relevant_values = remove_all_occurences(relevant_values, 0)
    values_set = set(relevant_values)
    if len(relevant_values) != len(values_set):
        return False
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}.issuperset(values_set)


def remove_all_occurences(values, val):
    return [value for value in values if value != val]


def is_sudoku_valid(board):
    return check_vertically(board) and check_horizontally(board) and check_boxes(board)


def main():
    board = [
        [1, 2, 0, 4, 5, 0, 7, 8, 9],
        [0, 5, 6, 7, 0, 9, 0, 2, 3],
        [7, 8, 0, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 0, 6, 0, 8, 0, 7],
        [3, 6, 0, 8, 9, 7, 2, 1, 4],
        [0, 9, 7, 0, 1, 4, 3, 6, 0],
        [5, 3, 1, 6, 0, 2, 9, 0, 8],
        [6, 0, 2, 9, 7, 8, 5, 3, 1],
        [9, 7, 0, 0, 3, 1, 6, 4, 2]]
    print(board)
    print("V: ", check_vertically(board))
    print("H: ", check_horizontally(board))
    print("B: ", check_boxes(board))
    print("S: ", is_sudoku_valid(board))
    if solve_sudoku(board):
        print("Solved!")
    print_array(board)
    print("-------------------------")
    board2 = [
        [6, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 3, 0, 0, 0, 8, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [5, 0, 0, 2, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 1],
        [0, 0, 0, 6, 0, 0, 0, 0, 0]]
    if solve_sudoku(board2):
        print("Solved!")
    print_array(board2)


if __name__ == "__main__":
    main()
