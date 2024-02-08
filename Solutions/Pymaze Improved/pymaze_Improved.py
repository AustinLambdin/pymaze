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

# Add global variable to track the number of items collected
ITEMS_COLLECTED = 0

# Function to initialize the maze
def initialize_maze():
    global ITEMS_COLLECTED
    maze = [[EMPTY] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    # Place walls
    for i in range(MAZE_HEIGHT):
        maze[i][0] = WALL
        maze[i][-1] = WALL
    for j in range(MAZE_WIDTH):
        maze[0][j] = WALL
        maze[-1][j] = WALL
    
    # Place player randomly
    while True:
        player_x = random.randint(1, MAZE_WIDTH - 2)
        player_y = random.randint(1, MAZE_HEIGHT - 2)
        if maze[player_y][player_x] == EMPTY:
            maze[player_y][player_x] = PLAYER
            break
    
    # Place exit randomly
    while True:
        exit_x = random.randint(1, MAZE_WIDTH - 2)
        exit_y = random.randint(1, MAZE_HEIGHT - 2)
        if maze[exit_y][exit_x] == EMPTY:
            maze[exit_y][exit_x] = EXIT
            break
    
    # Place items
    ITEMS_COLLECTED = 3
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

# (NEW FEATURE) Function to find the exit's position
def find_exit(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == EXIT:
                return (i, j)

# Function to move the player
def move_player(maze, direction):
    global ITEMS_COLLECTED # Access the global variable
    player_pos = find_player(maze)
    new_pos = (player_pos[0] + direction[0], player_pos[1] + direction[1])
    if maze[new_pos[0]][new_pos[1]] != WALL:
        if maze[new_pos[0]][new_pos[1]] == ITEM:
            ITEMS_COLLECTED -= 1  # Decrement the number of items collected
            if ITEMS_COLLECTED == 0:
                print("Congratulations! You found all the items!")
            else:
                print(f"Item collected! Only {ITEMS_COLLECTED} items left.")
        if new_pos == find_exit(maze):  # Check if the new position is the exit
            print("Congratulations! You found the exit!")
            return True
        maze[player_pos[0]][player_pos[1]] = EMPTY
        maze[new_pos[0]][new_pos[1]] = PLAYER
        return new_pos  # Return the new position of the player
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
