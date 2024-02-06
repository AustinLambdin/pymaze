# Maze Game

Welcome to the Maze Game! This is an intentionally incorrect python script to play through a maze. I was tasked with finding the error in the code and fix the script. The original script can be found in the 'Problem' folder, and the fixed script(s) within the 'Solutions' folder.

## How to Play

- Use the WASD keys to move the player character (P) up, down, left, or right in the maze.
- Try to find the exit (E) while collecting items (*) scattered throughout the maze.
- Be careful not to run into walls (#).

## Installation

1. Clone this repository to your local machine:

- git clone <repository_url>

2. Navigate to the directory containing the game files.

3. Run the game by executing the Python script:

- python maze_game.py

## Game Features

- **Randomly generated maze layout:** Each time the game starts, the maze layout is randomly generated, providing a unique experience.
- **Random player and exit placement:** The player character (P) and the exit (E) are placed randomly within the maze, ensuring different starting and ending points for each game session.
- **Item collection:** Items (*) are scattered throughout the maze, and the player can collect them while exploring. The game keeps track of the number of items collected.
- **Win condition:** The game ends when the player finds the exit. A congratulatory message is displayed upon successfully reaching the exit.

## Customization

- **Maze dimensions:** You can customize the width and height of the maze by modifying the `MAZE_WIDTH` and `MAZE_HEIGHT` constants in the code.
- **Number of items:** Adjust the number of items present in the maze by changing the value of the `ITEMS_COLLECTED` variable.

## Project Structure

The project contains the following folders:

1. **Problem:** Contains the initial broken code that provided by GitHub user: super-phreak.
2. **Resume:** Contains a README.md file with my resume.
3. **Solution:** Contains different solutions for fixing the broken code.

## Author

**Original Author:** super-phreak

**Edited By:** Austin Lambdin

## License

This project is licensed under the [MIT License](LICENSE).
