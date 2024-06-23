from .constants import *
from .go_logic import get_dead_group
from typing import List

Board = List[List[str]]


def get_empty_board(size: int) -> Board:
  board = [[EMPTY] * size for _ in range(size)]
  return board

def is_legal_board(board: Board) -> int:
  p = [EMPTY, BLACK, WHITE]
  for i in range(len(board)):
    for j in range(len(board)):
      color = board[i][j]
      if color not in p:
        return -1
      dead_group = get_dead_group(board, (i, j), color)
      if dead_group:
        return -2
  return 1