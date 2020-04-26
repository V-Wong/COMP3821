# Dynamic Programming (DP)

## Overview of DP
- Build an optimal solution to the problem from optimal solutions to subproblems.
- Subproblems chosen in a way that allows for recursive construction of optimal solutions to problems from optimal solutions to smaller size problems.
- Efficient because the sets of subproblems needed to solve larger problems heavily overlap. 
- Each subproblem is solved only once and its solution is stored in a table for multiple use for solving many larger problems.

## Cut and Paste Argument (Optimal Substructure)
- Assume that some piece of the optimal solution S* is not an optimal solution to a smaller subproblem.
- Show that replacing that piece with the optimal solution to the smaller subproblem
improves the alleged optimal solution S*.
- Conclude that S* must include an optimal solution to a smaller subproblem.
