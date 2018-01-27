#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   


from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    """open the file with the specified filename for reading, and it should use a loop to process the file one line at a time
    """
    f = open(filename,'r')
    c = 0
    ttl_m = 0
    ttl_s = 0
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        print(line+':',end=' ')
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        s = create_searcher(algorithm,param)
        if s == None:
            return
        soln = None
        try:
            soln = s.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
        if soln == None:
            print('no solution')
        else:
            print(soln.num_moves,'moves,',s.num_tested,'states tested')
            c += 1
            ttl_m += soln.num_moves
            ttl_s += s.num_tested
    print()
    print('solved',c,'puzzles')
    if c != 0:
        print('average:',ttl_m/c,'moves,',ttl_s/c,'states tested')
    f.close()
