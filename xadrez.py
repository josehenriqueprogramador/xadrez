import chess

board = chess.Board()

print("♟️ Xadrez no Termux (digite 'sair' para encerrar)\n")

while not board.is_game_over():
    print(board)
    print("\nTurno:", "Brancas" if board.turn else "Pretas")

    move = input("Digite o movimento (ex: e2e4): ").strip()

    if move.lower() == "sair":
        break

    try:
        board.push_uci(move)
    except:
        print("❌ Movimento inválido!\n")
        continue

    if board.is_check():
        print("⚠️ CHEQUE!\n")

if board.is_checkmate():
    print("\n♚ CHEQUE-MATE!")
    print("Vencedor:", "Pretas" if board.turn else "Brancas")
elif board.is_stalemate():
    print("\n🤝 Empate!")
