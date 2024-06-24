# Go Game

A Python implementation of the Go board game. This project includes game logic, rules enforcement, and unit tests to ensure correctness.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a Python-based implementation of the classic board game Go. It includes all the fundamental rules of Go, such as capturing stones, ko, and suicide prevention. The game is implemented in a modular way, making it easy to extend and integrate with other systems.

## Features

- Full implementation of Go game rules
- Support for different board sizes (3x3, 19x19, etc.)
- Unit tests for all critical components
- Easy to use API for playing moves and managing game state

## Installation

To install and run this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/go-game.git
    cd go-game
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```


## Usage


The board consists of a two-dimensional list, with one character at each position. “.” stands for empty space, “b” stands for black, and “w” stands for white. Each location can be accessed by row and column values, and board sizes range from 3 * 3 to 19 * 19.

When creating a new Go_game, you must pass the size as the first argument. If the size is n, a board of size n * n is created. Secondly, the initial status of the board can be provided if not provided, an empty board is created by default. Lastly, you need to set the color for the first player, which defaults to "b" (BLACK).

You can make a move using the play_move() function. If the move is valid, the newly updated board state will be returned. If the move is invalid, the same board state will be returned. Ensure to handle errors when the board state does not change.

Here is a basic example of how to use the Go game implementation:

```python
from go_game import GoGame

# Initialize a 19x19 board with the default color "b" (BLACK)
game = GoGame(19)

# Create a 5x5 board with an initial board state and color "w" (WHITE)
initial_board = [
    [".", ".", ".", ".", ".", ],
    [".", "b", ".", "w", ".", ],
    [".", ".", ".", ".", ".", ],
    [".", "w", ".", "b", ".", ],
    [".", ".", ".", ".", ".", ],
]
game_with_initial_state = Go_game(size=19, board=initial_board, color="w")

# Play a move at coordinate (3, 3) with black stone
game.play_move((3, 3))

# Print the current board state
for row in game.board:
    print(' '.join(row))



# go-game
