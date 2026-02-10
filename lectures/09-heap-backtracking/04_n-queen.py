def is_valid(row, col, board):
    #
    return False
    return True

def n_queens(row, board):
    if row == len(board):
        solutions.append([r[:] for r in board])
        return
    for col in range(4):
        #
        # 이번 행/렬에 퀸을 놓을 수 있다면
        if is_valid(row, col, board):
            board[row][col] = 1
            n_queens(row+1, board)
            board[row][col] = 0

n = 4
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트

n_queens(0, board)

for solution in solutions:
    print(solution)
