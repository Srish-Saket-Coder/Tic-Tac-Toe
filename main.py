def calculate_win(a, b, c):
    return a + b + c


def print_board(x_values: list, o_values: list):

    if x_values and o_values:
        in_case_of_zero = 'X' if x_values[0] else 'O' if o_values[0] else 0
        in_case_of_one = 'X' if x_values[1] else 'O' if o_values[1] else 1
        in_case_of_two = 'X' if x_values[2] else 'O' if o_values[2] else 2
        in_case_of_three = 'X' if x_values[3] else 'O' if o_values[3] else 3
        in_case_of_four = 'X' if x_values[4] else 'O' if o_values[4] else 4
        in_case_of_five = 'X' if x_values[5] else 'O' if o_values[5] else 5
        in_case_of_six = 'X' if x_values[6] else 'O' if o_values[6] else 6
        in_case_of_seven = 'X' if x_values[7] else 'O' if o_values[7] else 7
        in_case_of_eight = 'X' if x_values[8] else 'O' if o_values[8] else 8
        print(f"{ in_case_of_zero } | { in_case_of_one } | { in_case_of_two }")
        print('--|---|---')
        print(f"{ in_case_of_three } | { in_case_of_four } | { in_case_of_five }")
        print('--|---|--')
        print(f"{ in_case_of_six } | { in_case_of_seven } | { in_case_of_eight }")


def check_win(x_value, o_value):
    wins_possibility = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [0, 4, 8],
        [2, 4, 6],
        [6, 4, 2]
    ]
    for win in wins_possibility:
        if calculate_win(x_value[win[0]], x_value[win[1]], x_value[win[2]]) == 3:
            print('X won the match!🎆')
            return 1
        if calculate_win(o_value[win[0]], o_value[win[1]], o_value[win[2]]) == 3:
            print('O won the match!🎆')
            return 0
        return -1


if __name__ == "__main__":
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for x, 2 for o
    print('Welcome to the Tic Tac Toe game!')
    print('Rules: Players take turns putting their marks in empty squares. The first player to get 3 of her marks in '
          'a row (up, down, across, or diagonally) is the winner. When all 9 squares are full, the game is over. If '
          'no player has 3 marks in a row, the game ends in a tie. ')
    print_board(x_state, o_state)
    while True:
        if turn == 1:
            print('X goes next.')
            value: int = int(input('Enter the value: '))
            x_state[value] = 1
        else:
            print('O goes next.')
            value: int = int(input('Enter the value: '))
            o_state[value] = 1
        print_board(x_state, o_state)
        is_win = check_win(x_state, o_state)
        if is_win != -1:
            break

        turn = 1 - turn
