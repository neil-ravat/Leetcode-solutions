bool dfs(char** board, int boardSize, int* boardColSize, char* word, int x, int y, int index) {
    if (word[index] == '\0') return true; // All characters matched
    if (x < 0 || y < 0 || x >= boardSize || y >= boardColSize[0] || board[x][y] != word[index])
        return false;

    char temp = board[x][y];
    board[x][y] = '#'; // Mark as visited

    bool found = dfs(board, boardSize, boardColSize, word, x-1, y, index+1) ||
                 dfs(board, boardSize, boardColSize, word, x+1, y, index+1) ||
                 dfs(board, boardSize, boardColSize, word, x, y-1, index+1) ||
                 dfs(board, boardSize, boardColSize, word, x, y+1, index+1);

    board[x][y] = temp; // Restore the value after backtracking
    return found;
}

bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < boardColSize[0]; j++) {
            if (dfs(board, boardSize, boardColSize, word, i, j, 0))
                return true;
        }
    }
    return false;
}