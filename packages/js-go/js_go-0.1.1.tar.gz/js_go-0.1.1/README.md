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

Here is a basic example of how to use the Go game implementation:

```python
from go_game import GoGame

# Initialize a 19x19 game
game = GoGame(19)

# Play a move at coordinate (3, 3) with black stone
game.play_move((3, 3))

# Print the current board state
for row in game.board:
    print(' '.join(row))



# go-game
