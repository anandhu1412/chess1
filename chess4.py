import chess

board = chess.Board()

while not board.is_game_over():
    print(board)

    # Get the player's color (White or Black) for the current turn
    player_color = "White" if board.turn == chess.WHITE else "Black"

    while True:
        move_str = input(f"{player_color}'s move (e.g., 'e2e4'): ")
        move = chess.Move.from_uci(move_str)

        if move in board.legal_moves:
            board.push(move)
            break
        else:
            print(f"Invalid move for {player_color}. Try again.")

print("Game over. Result: " + board.result())
