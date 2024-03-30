## Write-up:

- The problem asks for the **maximum depth** of the tree, which means we must find the path from the **root** to the **deepest node** of the tree. Since we **don't know where the deepest node** is, we will visit every node. Therefore, **a complete traversal** of the tree is needed, and the best way to do that is to use **DFS**.

- The max depth is given by the edge count. First, we obtain the number of nodes in the longest root-to-leaf path in the tree. Then, subtracting 1 from the node count gives the edge count (max depth).

### Build dfs helper using steps outlined in DFS on Tree Introduction
1. Determine the return value
We return the node-count of the longest subroot-to-leaf path in the current subtree after we visit a node.

1. Identify states
To determine the depth of current node, we only need depth from its children and don't need any additional state.

Now, we can write the DFS using the above states and return value.

### Time Complexity: O(n)
There are n nodes and n - 1 edges in a tree so if we traverse each once then the total traversal is O(2n - 1) which is O(n).

### Space Complexity: O(h)
The call stack uses at most O(h) memory where h is the height of the tree, which is worst case O(n) when the tree is skewed (each node has one or no children).

```python
# Algo Monster's Solution
def tree_max_depth(root: Node) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root) - 1 if root else 0

# My solution
def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    edges = 0
    edges += max(tree_max_depth(root.left), tree_max_depth(root.right)) + 1
    return edges
```