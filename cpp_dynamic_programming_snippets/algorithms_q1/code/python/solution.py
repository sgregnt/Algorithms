# The problem (quoted from pdf)
# Binary string is sparse if there are no three consecutive 1's in B.
# For instance, strings 1, 110101, 0001011 are sparse, but 111, 1100011100, 010101110101 are
# not. Given sequence of non-negative weights w_0, w_1, ..., w_{n-1} define the value of the string.
# sum_i b_iw_i. Given w_0, ..., w_{n-1} write polynomial algorithm that finds the most valuable sparse string.


# Idea of a solution.
# Use memorization in the form of a table where you store the maximum possible score going down the
# sequence, where you keep track of the last 4 alternatives, so that at place [i][11] this is the maximum
# score that can be attained if we have a subsequence 11 at place i. Then for i-1 we can calculate the
# maximum if we put there 1 or maximum if we put there 0, if a sequence is illegal we can store -infty.
# for each n we have limited number of alternatives.









