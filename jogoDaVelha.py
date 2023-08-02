def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    print("Bem-vindo ao Jogo da Velha!")

    while True:
        print_board(board)
        player = players[player_index]

        while True:
            try:
                row = int(input(f"Jogador {player}, informe a linha (0-2): "))
                col = int(input(f"Jogador {player}, informe a coluna (0-2): "))

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Movimento inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Parabéns! Jogador {player} venceu!")
            break

        if is_board_full(board):
            print_board(board)
            print("Empate!")
            break

        player_index = (player_index + 1) % 2


if __name__ == "__main__":
    main()
