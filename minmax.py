import math

# Take leaf node values as input
values = list(map(int, input("Enter leaf values: ").split()))

# Find depth of the tree
depth = int(math.log2(len(values)))

# Minimax function
def minimax(depth, index, is_max, values, max_depth):

    # If leaf node is reached
    if depth == max_depth:
        return values[index]

    # MAX chooses maximum value
    if is_max:
        return max(
            minimax(depth + 1, index * 2, False, values, max_depth),
            minimax(depth + 1, index * 2 + 1, False, values, max_depth)
        )

    # MIN chooses minimum value
    else:
        return min(
            minimax(depth + 1, index * 2, True, values, max_depth),
            minimax(depth + 1, index * 2 + 1, True, values, max_depth)
        )

# Start from root as MAX
result = minimax(0, 0, True, values, depth)

print("Optimal Value:", result)



# Algorithm:
# 1.	Take the leaf node values of the game tree as input. 
# 2.	Traverse the game tree in a depth-first manner using recursion. 
# 3.	At a MAX node, select the maximum value from its child nodes. 
# 4.	At a MIN node, select the minimum value from its child nodes. 
# 5.	Continue this process until the root node is reached. 
# 6.	Return the value obtained at the root as the optimal value. 
# Explanation:
# Minimax is a decision-making algorithm used in game playing. It assumes two players: MAX, who tries to maximize the score, and MIN, who tries to minimize the score. The algorithm recursively evaluates the leaf nodes and passes their values upward, taking the maximum at MAX levels and minimum at MIN levels. The value obtained at the root represents the best possible outcome for MAX, assuming both players play optimally.
