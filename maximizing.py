def evaluate(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]            # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            if board[combo[0]] == 'X':
                return 10
            elif board[combo[0]] == 'O':
                return -10
    return 0

def is_moves_left(board):
    return any(cell == ' ' for cell in board)

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_score = max(best_score, minimax(board, depth + 1, not is_maximizing))
                board[i] = ' '
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_score = min(best_score, minimax(board, depth + 1, not is_maximizing))
                board[i] = ' '
        return best_score

def find_best_move(board):
    best_move = -1
    best_score = -float('inf')
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_score = minimax(board, 0, False)
            board[i] = ' '

            if move_score > best_score:
                best_score = move_score
                best_move = i

    return best_move

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('---------')

if __name__ == "__main__":
    board = [' '] * 9
    print("Initial board:")
    print_board(board)

    while is_moves_left(board):
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] == ' ':
            board[player_move] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        if is_moves_left(board):
            ai_move = find_best_move(board)
            print(f"AI's move: {ai_move}")
            board[ai_move] = 'X'
        else:
            break

        print_board(board)

    result = evaluate(board)
    if result == 10:
        print("AI wins!")
    elif result == -10:
        print("Player wins!")
    else:
        print("It's a draw!")
