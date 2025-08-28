<p align="center"><a href="https://group-9-minesweeper-project.vercel.app/" target="_blank"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCwIdCYJnRmDUQnpDKNvY31bHNh_3NevoPjg&s" alt="minesweeper"></a></p>

# Minesweeper Mini

## (Group 9 project - Phase 3 of SDF-FT14 - Python CLI)

### Setup.

To play the game, run the main.py file in the root folder:

###### In the terminal:

    - $git clone [git@github.com:Joseph-Hansel/python-minesweeper.git](git@github.com:Joseph-Hansel/python-minesweeper.git)
    - $cd python-minesweeper
    - Michael Kyalo - User interaction with CLI

   >$git clone [git@github.com:Joseph-Hansel/python-minesweeper.git](git@github.com:Joseph-Hansel/python-minesweeper.git)

   >$cd python-minesweeper

   >$python3 main.py


## Overview; About the Project.

MiniSweeper is a simplified version of the classic Minesweeper game. The goal is to create a functional and engaging game that can be played in a web browser.

### MVP Features:

1. **Game Board**: A grid-based game board with randomly placed mines.
2. **Gameplay**: Players can click on cells to reveal their contents. If a cell contains a mine, the game is over.
3. **Win Condition**: The game is won when all non-mine cells are revealed.

### User Interface

- The interface used is the command line interface.
- The game board will be displayed as a grid of cells.
- Empty cells will be white and undug cells are brown

### Technical Requirements

- The game was developed using the Python Language, with application of ORM to integrate a database.
- Packages installed include:
    * psycopg
    * sqlalchemy
    * alembic
    * python-dotenv

### Future Development

- Add additional features, such as:
    - Timer and score tracking.
    - Different difficulty levels (e.g., easy, medium, hard).
    - Customizable game board size.
    - Animations and sound effects.
    - Revealing the number of adjacent mines if a  dug cell is empty.
    - A button to reset the game and start a new round.
    
## Group members

    - Vanessa Tchappi - Scrum Master - Game logic
    - Joseph Hansel - Data Storage
    - Michael Kyalo - User interaction with CLI
    - Lyon Nganga - Game board generation