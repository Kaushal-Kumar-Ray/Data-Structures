class DecisionNode:
    def __init__(self, question, true_branch=None, false_branch=None):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def traverse_decision_tree(node):
    if isinstance(node, str):  # leaf node
        return node
    answer = input(f"{node.question} (yes/no): ").strip().lower()
    if answer == 'yes':
        return traverse_decision_tree(node.true_branch)
    else:
        return traverse_decision_tree(node.false_branch)
# Build the tree
# Decision: Is it raining?
# If yes -> Stay inside
# If no -> Go outside
tree = DecisionNode(
    "Is it raining?",
    true_branch="Stay inside",
    false_branch="Go outside"
)
# Run the decision
print("Decision:", traverse_decision_tree(tree))
