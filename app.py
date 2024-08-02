import streamlit as st

def is_safe(board, row, col, N):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_n_queens(board, col, N):
    if col == N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[col] = i
            if solve_n_queens(board, col + 1, N):
                return True
    return False

def chessboard(board, N):
    board_representation = []
    for i in range(N):
        row_representation = ""
        for j in range(N):
            if board[j] == i:
                row_representation += "Q "
            else:
                row_representation += "* "
        board_representation.append(row_representation)
    return board_representation

def solve_queens():
    st.title("N-Queens Problem Solver")
    
    N = st.number_input("Enter the number of Queens:", min_value=1, max_value=20, value=8, step=1)
    
    board = [-1] * N
    if not solve_n_queens(board, 0, N):
        st.write(f"No solution exists for {N}-Queens.")
    else:
        st.write(f"Solution for {N}-Queens:")
        board_representation = chessboard(board, N)
        for row in board_representation:
            st.text(row)

if __name__ == "__main__":
    solve_queens()
