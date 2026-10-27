# Author: Homero Vazquez
# Dynamic programming assignment. top-down and bottom-up approach.

#Top-down version
def dna_match_topdown(DNA1, DNA2):
    memo = {}

    def lcs(i, j):
        # Base case: one string is empty
        if i == len(DNA1) or j == len(DNA2):
            return 0

        # Check if already calculated
        if (i, j) in memo:
            return memo[(i, j)]

        # Characters match
        if DNA1[i] == DNA2[j]:
            memo[(i, j)] = 1 + lcs(i + 1, j + 1)

        # Characters don't match
        else:
            memo[(i, j)] = max(
                lcs(i + 1, j),
                lcs(i, j + 1)
            )

        return memo[(i, j)]

    return lcs(0, 0)


def dna_match_bottomup(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)

    # Create DP table filled with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table from the bottom up
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if DNA1[i - 1] == DNA2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]

DNA1 = "TAGTTCCGTCAAA"
DNA2 = "GTGTTCCCGTCAAA"

#print(dna_match_topdown(DNA1, DNA2))
#print(dna_match_bottomup(DNA1, DNA2))