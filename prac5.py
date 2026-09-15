# implement alpha beta pruning

# Alpha-Beta Pruning (Min-Max)
# 1. Traverse the game tree depth-first (Minimax)
# 2. Maintain two values:
#    - alpha  = best value found so far for MAX player (initially -infinity)
#    - beta   = best value found so far for MIN player (initially +infinity)
# 3. MAX node: pick the maximum of child values and update alpha
# 4. MIN node: pick the minimum of child values and update beta
# 5. Prune: if beta <= alpha at a node, stop exploring its remaining children
# 6. Return the best value evaluated from the root

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, path):
    if isinstance(node, int):  # leaf node -> utility value
        return node, path

    if maximizing_player:  # MAX node
        best = float('-inf')
        best_path = None
        for child in node:
            value, child_path = alpha_beta_pruning(child, depth + 1, alpha, beta, False, path + [id(child)])
            if value > best:                  # MAX picks the highest
                best = value
                best_path = child_path
            alpha = max(alpha, value)         # update alpha
            if beta <= alpha:                 # prune condition
                break
        return best, best_path

    else:  # MIN node
        best = float('inf')
        best_path = None
        for child in node:
            value, child_path = alpha_beta_pruning(child, depth + 1, alpha, beta, True, path + [id(child)])
            if value < best:                  # MIN picks the lowest
                best = value
                best_path = child_path
            beta = min(beta, value)           # update beta
            if beta <= alpha:                 # prune condition
                break
        return best, best_path


def minimax_value(node, maximizing_player):
    # plain minimax to show MIN values of each branch (answer 1)
    if isinstance(node, int):
        return node
    if maximizing_player:
        return max(minimax_value(c, False) for c in node)
    return min(minimax_value(c, True) for c in node)


# Game tree given as a nested list (leaf values at the bottom)
# Depth 1 (root) is a MAX node, alternating MAX / MIN afterwards
tree = [
    [
        [5, 6],
        [7, 4, 5]
    ],
    [
        [3],
        [1, 2],
        [6]
    ]
]

# Answer 1: MAX value at the root
max_value, _ = alpha_beta_pruning(tree, 0, float('-inf'), float('inf'), True, [])
print("1) MAX value at root:", int(max_value))

# Answer 2: MIN value of each branch (children of the root)
print("2) MIN values of each branch:", [int(minimax_value(c, False)) for c in tree])

# Answer 3: Optimal path (decision) chosen by MAX
branch_values = [minimax_value(c, False) for c in tree]
best_child_index = max(range(len(tree)), key=lambda i: branch_values[i])
print("3) Optimal move: choose branch", best_child_index, "-> MIN value", int(branch_values[best_child_index]))