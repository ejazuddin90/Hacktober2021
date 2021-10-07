"""
Famous Mathematical Game 2048 in python. 
Play on Online Compiler: http://www.codeskulptor.org

Just open http://www.codeskulptor.org in your browser paste the code and run it !

"""

try:
    import poc_2048_gui
except ImportError:
    import ext.poc_2048_gui as poc_2048_gui
try:
    import poc_simpletest
except ImportError:
    import ext.poc_simpletest as poc_simpletest
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # local variables
    zero_shift = []
    number_merge = []
    result = []
    blank = 0
    cache = 0

    # initializing blank list
    for idx in range(len(line)):
        number_merge.append(0)

    # shifting zeroes in initial list
    for val in line:
        if val != 0:
            zero_shift.append(val)
        else:
            blank += 1

    for idx in range(blank):
        zero_shift.append(0)

    # merging values in shifted list
    for idx, val in enumerate(zero_shift):
        #print("cache:", cache, "value:", val, "index:", idx, "shift_list", zero_shift, "merge_list", number_merge)
        if val == cache and val != 0:
            number_merge[idx-1] = val*2
            number_merge[idx] = 0
            cache = 0
        else:
            number_merge[idx] = val
            cache = val

    # shifting zeroes in merged list
    blank = 0
    for val in number_merge:
        if val != 0:
            result.append(val)
        else:
            blank += 1

    for idx in range(blank):
        result.append(0)

    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self._move_dir = {UP: [], DOWN: [], LEFT: [], RIGHT: []}
        # "UP" =[(0, 0), (0, 1), (0, 2), (0, 3)]
        #self._move_dir["UP"] = "test"
        for col in range(self._grid_width):
            self._move_dir[UP].append((0, col))
            self._move_dir[DOWN].append((self._grid_height - 1, col))
        for row in range(self._grid_height):
            self._move_dir[LEFT].append((row, 0))
            self._move_dir[RIGHT].append((row, self._grid_width - 1))
        self.new_tile()
        self.new_tile()


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        #return self._cells

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction in (UP, DOWN):
            num_steps = self._grid_height
        elif direction in (LEFT, RIGHT):
            num_steps = self._grid_width
        moved = False
        temp_list = []
        for start_cell in self._move_dir[direction]:
            # step 1: iterate through each line, write results to temp list
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                temp_list.append(self._cells[row][col])
            # step 2: merge temp list
            temp_list_snap = temp_list[:]
            temp_list = merge(temp_list)
            print(temp_list_snap, temp_list)
            if temp_list_snap != temp_list:
                moved = True
            # step 3: store merged temp list back on grid
            idx = 0
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                if direction in (UP, DOWN):
                    self._cells[row][col] = temp_list[idx]
                    idx += 1
                elif direction in (LEFT, RIGHT):
                    self._cells[row][col] = temp_list[idx]
                    idx += 1
            temp_list = []
        if moved:
            self.new_tile()
            moved = False
        score = sum(map(sum, self._cells))
        print("Your score: %s" % score)
        #return self._cells

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zero_list = []
        zero_cell = ()
        # self._cells = [[0 for col in range(self._grid_width)] for row in range(self._grid_height)]
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == 0:
                    zero_cell = (row, col)
                    zero_list.append(zero_cell)
        if len(zero_list) > 0:
            chance = random.randrange(0,10)
            cell_idx = random.randrange(len(zero_list))
            if chance == 9:
                self._cells[zero_list[cell_idx][0]][zero_list[cell_idx][1]] = 4
            else:
                self._cells[zero_list[cell_idx][0]][zero_list[cell_idx][1]] = 2
        else:
            print("You lost! Better luck next time!")

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


if __name__ == "__main__":
    
    poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
