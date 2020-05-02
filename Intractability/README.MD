# Intractability

## Decision Problems
- Problem with a YES or NO answer.

## Polynomial Time (P)
- A decision problem A is in polynomial time if there exists a polynomial time algorithm that solves it.
- Given an input x, such an algorithm outputs YES for all x which satisfies A and NO for all x which does not satisfy A.
- Such a problem is denoted as A ∈ **P**.

## Non-Deterministic Polynomial Time (NP)
- A decision problem A(x) is in non-deterministic polynomial time if both:
  - There exists a problem B(x, y) such that for every input x, A(x) is true just in case there exists y such that B(x, y) is true.
  - The truth of B(x, y) can be verified by an algorithm running in polynomial time in the length of x only.
- We call y a certificate for x.
- Such a problem is denoted as A ∈ **NP**.

# NP Complete
- An **NP** decision problem U(x) is **NP**-complete if every other **NP** problem is polynomially reducible to U(x).
- **NP**-complete problems are universal: if we had an algorithm that solves one single **NP**-complete problem U, then we could use such an algorithm to solve every other **NP** problem.
- A solution of an instance x of any other **NP** problem V could be obtained by:
  - Computing polynomial reduction f(x) from V to U.
  - Running algorithm that solves U on instance f(x).