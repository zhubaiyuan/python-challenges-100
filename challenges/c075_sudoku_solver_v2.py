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
        if is_valid_position(board, row, col, num):
            board[row][col] = num
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


def is_valid_position(board, row, col, num):
    return check_num_not_in_column(board, col, num) and \
        check_num_not_in_row(board, row, num) and \
        check_num_not_in_box(board, row, col, num)


def check_num_not_in_column(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return False
    return True


def check_num_not_in_row(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return False
    return True


def check_num_not_in_box(board, row, col, num):
    adjusted_row = row // 3 * 3
    adjusted_col = col // 3 * 3
    for y in range(3):
        for x in range(3):
            if board[adjusted_row + y][adjusted_col + x] == num:
                return False
    return True


def all_desired_numbers(all_collected_values):
    relevant_values = list(all_collected_values)
    remove_all_occurences(relevant_values, 0)
    values_set = set(relevant_values)
    if len(relevant_values) != len(values_set):
        return False
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}.issuperset(values_set)


def remove_all_occurences(the_list, val):
    return [value for value in the_list if value != val]


def main():
    board1 = [
        [1, 2, 0, 4, 5, 0, 7, 8, 9],
        [0, 5, 6, 7, 0, 9, 0, 2, 3],
        [7, 8, 0, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 0, 6, 0, 8, 0, 7],
        [3, 6, 0, 8, 9, 7, 2, 1, 4],
        [0, 9, 7, 0, 1, 4, 3, 6, 0],
        [5, 3, 1, 6, 0, 2, 9, 0, 8],
        [6, 0, 2, 9, 7, 8, 5, 3, 1],
        [9, 7, 0, 0, 3, 1, 6, 4, 2]]
    if solve_sudoku(board1):
        print("Solved!")
    print_array(board1)
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
