# Tic Tac Toe Game

Welcome to the README file for the Tic Tac Toe game project! This project is a console-based implementation of the classic Tic Tac Toe game using pure Python. In this document, you'll find an overview of the project, instructions on how to run the game, and a brief explanation of the game rules.

## Game Overview

The Tic Tac Toe game is a two-player game played on a 3x3 grid. Players take turns marking a cell in the grid with their respective symbols: 'X' or 'O'. The objective of the game is to get three of your symbols in a horizontal, vertical, or diagonal line on the grid. The first player to achieve this wins the game. If all the cells are filled and no player has won, the game ends in a draw.

## Requirements

To run the Tic Tac Toe game, you need to have Python 3 installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

## How to Run the Game

1. Clone this repository or download the project files to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the game:

```shell
python tic_tac_toe.py
```

4. The game will start, and you'll be prompted to enter the positions to place your symbols (X or O) on the grid. Follow the instructions displayed in the console to play the game.
5. Enjoy playing Tic Tac Toe!

## Game Rules

1. The game is played on a 3x3 grid.
2. Players take turns entering their symbols ('X' or 'O') in empty cells on the grid.
3. To make a move, enter the corresponding position number of the cell you want to mark. The positions are numbered from 1 to 9, starting from the top-left cell and going from left to right and top to bottom.
4. The game will validate your moves and display the updated grid after each turn.
5. The first player to get three of their symbols in a horizontal, vertical, or diagonal line wins the game.
6. If all the cells are filled and no player has won, the game ends in a draw.

## Additional Notes

- The game is implemented using pure Python, without any external libraries or dependencies.
- The code is structured into modular functions to handle different aspects of the game logic.
- The game provides input validation to ensure players enter valid moves.
- The console output is kept minimal and user-friendly for a smooth gaming experience.
