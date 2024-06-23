from .go_logic import *
from .function import *
from typing import List, Tuple
from .constants import *

Coordinate = Tuple[int, int]
Board = List[List[str]]
State = Tuple[Board, str]

class Go_game:
  def __init__(self, size: int, board: Board | None = None, color: str = BLACK) -> None:
    if size < min_size:
      raise(ValueError("size is too small"))
    if size > max_size:
      raise(ValueError("size is too big"))
    if color != BLACK and color != WHITE:
      raise(ValueError("invalid color"))


    self.board: Board = board if board else get_empty_board(size)
    self.size = size
    is_legal = is_legal_board(self.board)
    if is_legal < 0:
      if is_legal == -1:
        raise(ValueError("invalid character exist"))
      else:
        raise(ValueError("Dead group exist"))
    self.color: str = color
    self.init_state: State = (self.board, self.color)
    self.record: List[State] = [self.init_state]
    self.idx: int = 0
    self.ko_spot: Coordinate = None

  def _change_color(self):
    self.color = WHITE if self.color == BLACK else BLACK

  def go_to_init(self) -> None:
    self.board, self.color = self.init_state
    self.idx = 0
    return
  
  def go_to_last(self) -> None:
    self.board, self.color = self.record[-1]
    self.idx = len(self.record) - 1
    return

  def go_to_next_move(self) -> Board:
    if self.idx < len(self.record) - 1:
      self.idx += 1
      self.board, self.color = self.record[self.idx]
    return self.board
  
  def go_to_previous_move(self) -> Board:
    if self.idx > 0:
      self.idx -= 1
      self.board, self.color = self.record[self.idx]
    return self.board


  def _add_records(self, board: Board) -> None:
    new_state: State = (board, self.color)
    self.idx += 1
    if self.idx == len(self.record):
      self.record.append(new_state)
      return
    if board == self.record[self.idx][0]:
      return
    record = self.record[:self.idx]
    record.append(new_state)
    self.record = record
    return

  def play_move(self, move: Coordinate) -> Board:
    if move == self.ko_spot:
      return self.board
    new_board, new_ko_spot = handle_move(self.board, move, self.color)
    if self.board == new_board:
      return self.board
    self.board = new_board
    self._change_color()
    self._add_records(new_board)
    self.ko_spot = new_ko_spot
    return new_board
  



  
