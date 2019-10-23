#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def TicTacDraw(board):
    n=len(board)
    d={'0':'O','1':'X','2':' '}
    for i in range(n):
        s=' '
        for j in range(n):
            if j == (len(board[i])-1):
                s=s+d[str(board[i][j])]
            else:
                s=s+d[str(board[i][j])]+' | '
        if i == (len(board)-1):
            print(s)
        else:
            print(s)
            print('-'*(4*n-1))

if __name__ == '__main__':
    board = [[0, 1, 2], [2, 0, 0], [1, 1, 2]]
    TicTacDraw(board)