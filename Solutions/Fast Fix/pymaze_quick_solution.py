import random

# Maze dimensions
MAZE_WIDTH = 10
MAZE_HEIGHT = 10

# Maze symbols
WALL = '#'
EMPTY = ' '
PLAYER = 'P'
EXIT = 'E'
ITEM = '*'

# Function to initialize the maze
def initialize_maze():
    maze = [[EMPTY] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    # Place walls
    for i in range(MAZE_HEIGHT):
        maze[i][0] = WALL
        maze[i][-1] = WALL
    for j in range(MAZE_WIDTH):
        maze[0][j] = WALL
        maze[-1][j] = WALL
    # Place player
    maze[1][1] = PLAYER
    # Place exit
    maze[MAZE_HEIGHT - 2][MAZE_WIDTH - 2] = EXIT
    # Place items
    for _ in range(3):  # Adjust the number of items as needed
        while True:
            x = random.randint(1, MAZE_WIDTH - 2)
            y = random.randint(1, MAZE_HEIGHT - 2)
            if maze[y][x] == EMPTY:
                maze[y][x] = ITEM
                break
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Function to move the player
def move_player(maze, direction):
    player_pos = find_player(maze)
    new_pos = (player_pos[0] + direction[0], player_pos[1] + direction[1])
    if maze[new_pos[0]][new_pos[1]] != WALL:
        maze[player_pos[0]][player_pos[1]] = EMPTY
        maze[new_pos[0]][new_pos[1]] = PLAYER
        print("New position:", new_pos)  # Debug print statement
        print("Cell value at new position:", maze[new_pos[0]][new_pos[1]])  # Debug print statement
        if new_pos == (MAZE_HEIGHT - 2, MAZE_WIDTH - 2):  # Check if the new position is the exit
            print("Congratulations! You found the exit!")
            return True
        return new_pos # Return the new position of the player
    return False  # Return the current position if the move is invalid



# Function to find the player's position
def find_player(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == PLAYER:
                return (i, j)

# Main function to run the game
def main():
    maze = initialize_maze()
    print("Welcome to the maze game!")
    print("Use WASD to move. Try to find the exit (E) while collecting items (*)!")
    while True:
        print_maze(maze)
        direction = input("Enter your move (WASD): ").upper()
        if direction == 'W':
            new_pos = move_player(maze, (-1, 0))
        elif direction == 'S':
            new_pos = move_player(maze, (1, 0))
        elif direction == 'A':
            new_pos = move_player(maze, (0, -1))
        elif direction == 'D':
            new_pos = move_player(maze, (0, 1))
        else:
            print("Invalid move! Use WASD.")
            continue
        if not new_pos:
            print("Cannot move there! Try another direction.")
        if new_pos is True:  # Check if the game should end
            break

if __name__ == "__main__":
    main()
