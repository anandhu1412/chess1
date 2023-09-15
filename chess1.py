import chess
import chess.svg

board = chess.Board()

while not board.is_game_over():
    print(board)
    move_str = input("Enter your move :n")
    move = chess.Move.from_uci(move_str)
    
    if move in board.legal_moves:
        board.push(move)
    else:
        print("Invalid move. Try again.")

print("Game over. Result: " + board.result())
