# Highest Value Longest Common Subseequence
Computes the Highest-Value Longest Common Subsequence of two strings over a fixed alphabet with assigned character values, and outputs both the maximum value and one optimal subsequence

## Usage
* No compilation needed - requires Python 3
* Example inputs and outputs are located in 'examples/'
* Run example 1 using

## Written Component:
### Question 1: Empirical Comparison

### Question 2: Recurrence Equation

Let dp[i][j] = max value of any common subsequence of A[1..i] and B[..j]


Base Cases:

dp[i][0] = 0 for all i = 0, 1, ..., n

dp[0][j] = 0 for all j = 0, 1, ..., m


Recurrence:

dp[i][j] = dp[i - 1][j - 1] + v(A[i])	if A[i] == B[j]

dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])	if A[i] != B[j]


Why Recurrence is Correct:

Case 1: A[i] == B[j]: Characters match, so we include this character in the common subsequence. Since all character values are nonnegative, including a matching character only helps, so we take it. The best value we can achieve is whatever was optimal for A[1..i - 1] and B[1..j - 1] plus v(A[i])

Case 2: A[i] != B[j]: Characters differ, so at least one must be skipped. We try both options and take the better one:

- Skip A[i]: inherits dp[i - 1][j]
- Skip B[j]: inherits dp[i][j - 1]

The optimal solution at dp[i][j] is always built from the optimal solution of a smaller subproblem, so no greedy choices needed. The same subproblems are reused multiple times, which is why we store results in a table rather than recompute recursively. The final answer is dp[n][m]

### Question 3: Big-Oh
HVLCS(A, B, val):
	n = length(A)
	m = length(B)

	// Initialize DP table with base cases
	for i = 0 to n:
		dp[i][0] = 0
	for j = 0 to m:
		dp[0][j] = 0

	// Fill DP table
	for i = 1 to n:
		for j = 1 to m:
			if A[i] == B[j]:
				dp[i][j] = dp[i - 1][j - 1] + val[A[i]]
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

	return dp[n][m]


Runtime Analysis

Initialize base cases = O(n + m)
Filling DP table = O(n x m)
Return = O(1)

TOTAL = O(n x m)

## Authors:
* Ansh Gupta
* Philip Baptist
