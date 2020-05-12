# Intractability

![Euler diagram for P/NP/NP-Complete/NP-Hard](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/P_np_np-complete_np-hard.svg/2560px-P_np_np-complete_np-hard.svg.png)

## Decision Problems
- Problem with a YES or NO answer.

## Complexity Classes
### Polynomial Time (P)
- A decision problem A is in polynomial time if there exists a polynomial time algorithm that solves it.
- Given an input x, such an algorithm outputs YES for all x which satisfies A and NO for all x which does not satisfy A.
- Such a problem is denoted as A ∈ **P**.

### Non-Deterministic Polynomial Time (NP)
- A decision problem A(x) is in non-deterministic polynomial time if both:
  - There exists a problem B(x, y) such that for every input x, A(x) is true just in case there exists y such that B(x, y) is true.
  - The truth of B(x, y) can be verified by an algorithm running in polynomial time in the length of x only.
- We call y a certificate for x.
- Intuitively, **NP** problems can be verified in polynomial time.
- Such a problem is denoted as A ∈ **NP**.

### NP-Complete
- An **NP** decision problem U(x) is **NP**-complete if every other **NP** problem is polynomially reducible to U(x).
- **NP**-complete problems are universal: if we had an algorithm that solves one single **NP**-complete problem U, then we could use such an algorithm to solve every other **NP** problem.
- A solution of an instance x of any other **NP** problem V could be obtained by:
  - Computing polynomial reduction f(x) from V to U.
  - Running algorithm that solves U on instance f(x).
  
### NP-Hard
- An **NP** decision problem A(x) is **NP**-hard if there is an **NP**-complete problem B(x) that is polynomially reducible to A(x).
- All **NP**-complete problems are reducible to any other **NP**-complete problem in polynomial time. A polynomial time solution to 1 **NP**-hard problem would then indicate a polynomial time solution to all **NP** problems.
- Intuitively, **NP**-hard problems are problems at least as hard as the **NP**-complete problems.

## Polynomial Reduction
- Method of solving one problem using another. 
- A problem A(x) is polynomially reducible to B(x) if there exists a polynomial algorithm transforming A instances into B instances. 
- If A(x) is polynomially reducible to B(x) then:
  - B(x) is at least as hard as A(x), as solving B(x) allows you to solve A(x).
  - If a polynomial algorithm exists for B(x), then a polynomial algorithm exists for A(x) as polynomials compose.
  - If A(x) is not solveable in polynomial time, then B(x) is not solveable in polynomial time, as this contradicts the previous point.

