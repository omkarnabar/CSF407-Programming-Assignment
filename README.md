# Done as a programming assignment for the course CSF407

Othello is a two-player strategy game played on an 8x8 grid with black and white pieces called "discs". The objective is to have more of your color discs on the board than your opponent at the end of the game. Players take turns placing discs on the board, outflanking their opponent's discs to flip them to their color. The game ends when the board is full or neither player can make a move. The player with the most discs of their color on the board at the end of the game wins.

# The game
This makes two agents play against each other. By commenting and uncommenting out certain lines of code in the given function, it could be modified to play against a human user as well as print board state after each move. The reason for having two agents play against each other was to compare between different search depths, evaluation functions and assessing how improved move ordering affects the time taken for the agent to make a move.

# Different Search Depths
Here I tested the game with 2 agents, one with search depth of 10 and the other with 20 and both having the same evaluation function. I tested it on 1000 runs of the game. And the agent with higher search depth performs better. This is due to it having search more possibilities and having a more accurate utility for each move. 
PS: It takes quite a while for 1000 runs. With just 100 or lesser runs I was getting slightly random results.

# Different Evaluation Functions
Here I ran the game with two agents playing against each other. Both searched till a depth of 10. One used a simple evaluation function (evaluate_simple) and the other used a modified version which I expected to capture the game state better (evaluate_improved). The new function basically adds upon the simple difference of piece count used earlier. It gives more importance to corner pieces being occupied by the player, each position now has a weight associated with it. The more unlikely it is to be flipped, the more positive the value of its weight would be. Also, I captured the number of moves each player has which would result in opponent pieces being flipped. I worked with an assumption that this would perform better as an utility function for a non terminal node in the minimax tree. At times it performed better slightly but wasn't significantly outperforming the simpler function either.

# With and Without move ordering
The move ordering function is as explained above near its definition. On an average, the agent with move ordering is about 3-4 times faster than the one without(random). This is due to the agent exploring the more preferable branches earlier, thus promoting pruning.
The EBF is calculated as (node_count)^(1/search_depth) as an approximate solution.
On multiple runs, i get the Average EBF of with ordering to be lesser than Average EBF with random ordering. This means that my move ordering has come slightly closer to the case with perfect move ordering. Also, in this case the ordering uses the simpler evaluation function. If we used the improved function, the EBF might come out to be lower.

# Comparative Analysis of A* and B* search
I did A* and B* search over the romania map given in AIMA. I used the time taken and path cost as a metric to compare between the two search strategies.  I took all possible combinations of start and goal cities and ran both algorithms on it. I used the straight line distance heuristic for the same.

The A* search algorithm evaluates nodes based on two cost functions: the cost to reach the node from the start node (g(n)) and the estimated cost to reach the goal node from the current node (h(n))(heuristic). The total cost of a node is the sum of these two costs (f(n) = g(n) + h(n)). The algorithm then chooses the node with the lowest f-value as the next node to expand.

B* search is similar to A* search, but uses the estimated cost as a backup value instead of the primary heuristic function. Nodes are evaluated based on the actual cost and estimated cost to reach the goal. The backup value used in B* search is the difference between the heuristic value of the node's parent and the current node's heuristic value. B* search is useful when the heuristic function is unreliable, but requires more computational resources than A* search.

# Results
As seen in the results of the code  block, even in multiple runs due to some randomness the number of times when B* is faster does fluctuate a bit, but it never gives a more optimal path than A*.
