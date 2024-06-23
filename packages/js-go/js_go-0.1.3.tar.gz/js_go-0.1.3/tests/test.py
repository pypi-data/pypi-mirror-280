import unittest
from js_go.go_game import Go_game
from js_go.function import get_empty_board

class TestMyClass(unittest.TestCase):
  def test_init(self):
    test_empty_board_3 = get_empty_board(3)
    test_empty_board_19 = get_empty_board(19)

    test_3 = Go_game(3)
    test_19 = Go_game(19)

    self.assertEqual(test_3.board, test_empty_board_3)
    self.assertEqual(test_19.board, test_empty_board_19)

  def test_size_error_small(self):
    with self.assertRaises(ValueError):
      Go_game(2)

  def test_size_error_big(self):
    with self.assertRaises(ValueError):
      Go_game(20)

  def test_specific_board(self):
    test_board = [
      [".", "b", "w"],
      ["w", ".", "."],
      [".", "b", "."]
    ]
    test = Go_game(3, test_board)
    self.assertEqual(test.board, test_board)

  def test_specific_board_dead_error(self):
    error_board = [
      ["b", "b", "w"],
      ["w", "w", "."],
      [".", "b", "."]
    ]
    with self.assertRaises(ValueError):
      Go_game(3, error_board)

  def test_specific_board_char_error(self):
    error_board = [
      [".", "b", "w"],
      ["w", ".", "h"],
      [".", "b", "."]
    ]
    with self.assertRaises(ValueError):
      Go_game(3, error_board)

  def test_color_error(self):
    with self.assertRaises(ValueError):
      Go_game(3, None, "t")

  def test_play_move(self):
    test_board = [
      [".", "b", "w"],
      ["w", ".", "."],
      [".", "b", "."]
    ]

    expected_board = [
      [".", "b", "w"],
      ["w", ".", "."],
      [".", "b", "b"]
    ]
       
    test = Go_game(3, test_board)
    test.play_move((2, 2))
    self.assertEqual(test.board, expected_board)

  def test_play_move_outside(self):
    expected_board = get_empty_board(3)
    test = Go_game(3)
    test.play_move((3, 3))
    self.assertEqual(test.board, expected_board)
    test.play_move((-1, 2))
    self.assertEqual(test.board, expected_board)

  def test_capturing_move(self):
    test_board = [
      [".", "b", "w"],
      ["w", ".", "."],
      [".", "b", "."]
    ]

    expected_board = [
      [".", "b", "."],
      ["w", ".", "b"],
      [".", "b", "."]
    ]
       
    test = Go_game(3, test_board)
    test.play_move((1, 2))
    self.assertEqual(test.board, expected_board)

  def test_capturing_move_huge(self):
    test_board = [
      ["w", "w", "w"],
      ["w", ".", "w"],
      ["w", "w", "w"]
    ]

    expected_board = [
      [".", ".", "."],
      [".", "b", "."],
      [".", ".", "."]
    ]
       
    test = Go_game(3, test_board)
    test.play_move((1, 1))
    self.assertEqual(test.board, expected_board)

  def test_suicide_move(self):
    init_board = [
      ["w", ".", "w"],
      ["w", "w", "."],
      [".", ".", "w"]
    ]
       
    test = Go_game(3, init_board)
    test.play_move((1, 2))
    self.assertEqual(test.board, init_board)

  def test_suicide_move_huge(self):
    init_board = [
      ["b", "b", "b"],
      ["b", ".", "b"],
      ["b", "b", "b"]
    ]
       
    test = Go_game(3, init_board)
    test.play_move((1, 1))
    self.assertEqual(test.board, init_board)

  def test_go_to_previous_and_next_move(self):
    init_board = [
      ["w", "b", "."],
      ["w", ".", "b"],
      ["b", ".", "."]
    ]

    last_board = [
      [".", "b", "."],
      [".", "b", "b"],
      ["b", ".", "."]
    ]

    test = Go_game(3, init_board)
    test.play_move((1, 1))
    test.go_to_previous_move()
    self.assertEqual(test.board, init_board)
    test.go_to_next_move()
    self.assertEqual(test.board, last_board)

  def test_go_to_init_and_last(self):
    init_board = [
      [".", ".", "."],
      [".", ".", "."],
      [".", ".", "."]
    ]

    last_board = [
      [".", ".", "."],
      [".", "b", "w"],
      [".", "w", "."]
    ]

    test = Go_game(3)
    test.play_move((1, 1))
    test.play_move((1, 2))
    test.play_move((2, 2))
    test.play_move((2, 1))
    test.go_to_init()
    self.assertEqual(test.board, init_board)
    test.go_to_last()
    self.assertEqual(test.board, last_board)
    


  def test_ko(self):
    test_board = [
      [".", "b", "w"],
      ["b", "w", "."],
      [".", ".", "w"]
    ]

    expected_ko_spot = (0, 2)
    expected_board = [
      [".", "b", "."],
      ["b", "w", "b"],
      [".", ".", "w"]
    ]

    test = Go_game(3, test_board)
    test.play_move((1, 2))
    self.assertEqual(test.ko_spot, expected_ko_spot)
    test.play_move((expected_ko_spot))
    self.assertEqual(test.board, expected_board)

  def test_white_plays_first(self):
    expected_board = [
      [".", ".", "."],
      [".", "w", "."],
      [".", ".", "."]
    ]

    test = Go_game(3, None, "w")
    test.play_move((1, 1))
    self.assertEqual(test.board, expected_board)

  def test_multiple_play_move(self):
    expected_board = [
      ["b", "w", "w"],
      ["b", "w", "."],
      [".", "b", "."]
    ]

    test = Go_game(3)
    test.play_move((0, 0))
    test.play_move((0, 1))
    test.play_move((1, 0))
    test.play_move((0, 2))
    test.play_move((2, 1))
    test.play_move((1, 1))
    self.assertEqual(test.board, expected_board)
  
  


  
  
  

  









if __name__ == '__main__':
    unittest.main()
