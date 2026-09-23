# Given a 2-D grid of characters board and a string word, 
# return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. 
# The same cell may not be used more than once in a word.

def grid(board, word):

    row = len(board)
    cols = len(board[0])

    visited = set()

    def search(i, r, c):

        if i == len(word):
            return True

        if r < 0 or r >= row or c < 0 or c >= cols or board[r][c] != word[i] or (r,c) in visited:
            return False 

        visited.add((r, c))

        res = search(i + 1, r + 1, c) or search(i + 1, r - 1, c) or search(i + 1, r, c + 1) or search(i + 1, r, c - 1)

        visited.remove(r,c)
        return res


    for r in range(row):
        for c in range(cols):
            if board[r][c] == word[0]:
                if search(0, r, c):
                    return True
    return False