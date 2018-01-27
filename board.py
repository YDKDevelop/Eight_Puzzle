#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#


class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for i in range(3):
            for j in range(3):
                self.tiles[i][j] = int(digitstr[3*i+j])
                if digitstr[3*i+j] == '0':
                    self.blank_r = i
                    self.blank_c = j
    
    ### Add your other method definitions below. ###
#Function 2
    def __repr__(self):
        """returns a string representation of a Board object
        """
        s = ''
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == 0:
                    s += '_'
                else:
                    s += str(self.tiles[i][j])
                if j == 2:
                    s += ' \n'
                else:
                    s += ' '
        return s
#Function 3
    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction in which the blank should move, and that attempts to modify the contents of the called Board object accordingly. 
        """
        r = self.blank_r
        c = self.blank_c
        if direction == 'left':
            if c > 0:
                self.blank_c -= 1
                c -= 1
                temp = self.tiles[r][c]
                self.tiles[r][c] = self.tiles[r][c+1]
                self.tiles[r][c+1] = temp
                return True
        elif direction == 'right':
            if c < 2:
                self.blank_c += 1
                c += 1
                temp = self.tiles[r][c]
                self.tiles[r][c] = self.tiles[r][c-1]
                self.tiles[r][c-1] = temp
                return True
        elif direction == 'up':
            if r > 0:
                self.blank_r -= 1
                r -= 1
                temp = self.tiles[r][c]
                self.tiles[r][c] = self.tiles[r+1][c]
                self.tiles[r+1][c] = temp
                return True
        elif direction == 'down':
            if r < 2:
                self.blank_r += 1
                r += 1
                temp = self.tiles[r][c]
                self.tiles[r][c] = self.tiles[r-1][c]
                self.tiles[r-1][c] = temp
                return True
        else:
            print('unknown direction:',direction)
        return False
#Function 4
    def digit_string(self):
        """returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute.
        """
        s = ''
        for i in range(3):
            for j in range(3):
                s += str(self.tiles[i][j])
        return s
#Function 5
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the called object
        """
        s = self.digit_string()
        b_copy = Board(s)
        return b_copy
#Function 6
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object that are not where they should be in the goal state.
        """
        c = 0
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != i*3+j:
                    c += 1
                    if self.tiles[i][j] == 0:
                        c -= 1
        return c
#Function 7
    def __eq__(self,other):
        """return True if the called object (self) and the argument (other) have the same values for the tiles attribute, and False otherwise
        """
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != other.tiles[i][j]:
                    return False
        return True
                    
#Heuristic 2
    def total_path(self):
        """counts and returns the total number of direct steps to take in order to reach the goal
        """
        c = 0
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != 0:
                    g_r = self.tiles[i][j]%3
                    g_c = self.tiles[i][j]//3
                    c += abs(j-g_r)
                    c += abs(i-g_c)
        return c
