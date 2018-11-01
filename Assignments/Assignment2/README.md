## Checkpoints
- [X] Implement the reading of the file for start and the goal state
- [X] Implement the heuristic functions
- [X] Implement the action function
- [] Contain everything in single class 
- [] Print the number of state explored and the iteration requited
- [] print the length of the shortest path  found
- [] print the path found
- [] Print the state explored
- [] make a a class ot handle all the verbose information
- [] Implement a non admissible heuristic


1. `run_from_file.py` can run the required A* from using a start state from the file 
`python run_from_file.py <start_state> <goal state>`
2. `run_from_generate.py` run the required the heurisitc by generating puzzle from the goal
3. `run_h1/2/3/4.py` are programs to run and store verbose using different heurtistic for same state for comparison
4. `Result1.py` will contain the result for publishing the data
## These contain the normal interatino wala result
results_h3.pkl
results_h2.pkl
results_h1.pkl




## These file contains the result for the A* object
results_h3_3.pkl
results_h2_3.pkl
results_h1_3.pkl


## A link explaining about the solvability of 8 puzzle
https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/



## A non addmissible heursiitc
http://ai.stanford.edu/~latombe/cs121/2011/slides/D-heuristic-search.pdf


### Result from non admissible heuristic
#### function to test it sui get_pessimistic_path
```
[[0 3 8]
 [6 1 7]
 [2 5 4]]
Success Found Path
The Start State :
[[5 2 3]
 [7 6 0]
 [1 8 4]]
The Goal State : 
[[1 2 3]
 [4 5 6]
 [7 8 0]]
States Explored : 1529
Iterations Requried to Reach Success : 964

Total Number of States on Path : 21
Optimal Path 
[[5 2 3]
 [7 6 0]
 [1 8 4]]

[[5 2 3]
 [7 0 6]
 [1 8 4]]

[[5 2 3]
 [0 7 6]
 [1 8 4]]

[[0 2 3]
 [5 7 6]
 [1 8 4]]

[[2 0 3]
 [5 7 6]
 [1 8 4]]

[[2 3 0]
 [5 7 6]
 [1 8 4]]

[[2 3 6]
 [5 7 0]
 [1 8 4]]

[[2 3 6]
 [5 7 4]
 [1 8 0]]

[[2 3 6]
 [5 7 4]
 [1 0 8]]

[[2 3 6]
 [5 0 4]
 [1 7 8]]

[[2 3 6]
 [0 5 4]
 [1 7 8]]

[[2 3 6]
 [1 5 4]
 [0 7 8]]

[[2 3 6]
 [1 5 4]
 [7 0 8]]

[[2 3 6]
 [1 0 4]
 [7 5 8]]

[[2 3 6]
 [1 4 0]
 [7 5 8]]

[[2 3 0]
 [1 4 6]
 [7 5 8]]

[[2 0 3]
 [1 4 6]
 [7 5 8]]

[[0 2 3]
 [1 4 6]
 [7 5 8]]

[[1 2 3]
 [0 4 6]
 [7 5 8]]

[[1 2 3]
 [4 0 6]
 [7 5 8]]

[[1 2 3]
 [4 5 6]
 [7 0 8]]

[[1 2 3]
 [4 5 6]
 [7 8 0]]

Optimal Cost of the Path , Same as Depth : 21
None
Success Found Path
The Start State :
[[5 2 3]
 [7 6 0]
 [1 8 4]]
The Goal State : 
[[1 2 3]
 [4 5 6]
 [7 8 0]]
States Explored : 693
Iterations Requried to Reach Success : 432

Total Number of States on Path : 19
Optimal Path 
[[5 2 3]
 [7 6 0]
 [1 8 4]]

[[5 2 3]
 [7 0 6]
 [1 8 4]]

[[5 2 3]
 [0 7 6]
 [1 8 4]]

[[5 2 3]
 [1 7 6]
 [0 8 4]]

[[5 2 3]
 [1 7 6]
 [8 0 4]]

[[5 2 3]
 [1 7 6]
 [8 4 0]]

[[5 2 3]
 [1 7 0]
 [8 4 6]]

[[5 2 0]
 [1 7 3]
 [8 4 6]]

[[5 0 2]
 [1 7 3]
 [8 4 6]]

[[0 5 2]
 [1 7 3]
 [8 4 6]]

[[1 5 2]
 [0 7 3]
 [8 4 6]]

[[1 5 2]
 [7 0 3]
 [8 4 6]]

[[1 5 2]
 [7 4 3]
 [8 0 6]]

[[1 5 2]
 [7 4 3]
 [0 8 6]]

[[1 5 2]
 [0 4 3]
 [7 8 6]]

[[1 5 2]
 [4 0 3]
 [7 8 6]]

[[1 0 2]
 [4 5 3]
 [7 8 6]]

[[1 2 0]
 [4 5 3]
 [7 8 6]]

[[1 2 3]
 [4 5 0]
 [7 8 6]]

[[1 2 3]
 [4 5 6]
 [7 8 0]]

Optimal Cost of the Path , Same as Depth : 19
None
[dhawal.cs15@cseresearch Assignment2]$ 
```
```h4_non_optimal.txt``` contain one such run0