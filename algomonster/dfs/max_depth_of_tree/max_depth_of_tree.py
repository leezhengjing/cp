class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    edges = 0
    edges += max(tree_max_depth(root.left), tree_max_depth(root.right)) + 1
    return edges

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    "Test Case 1"
    test_1 = "5 4 3 x x 8 x x 6 x x"
    test_2 = "1 x x"
    test_3 = "x"
    test_4 =  "6 x 9 x 11 x 7 x x"
    
    
    root = build_tree(iter(test_1.split()), int)
    res = tree_max_depth(root)
    expected = 2
    print("Test 1:")
    print("Expected:" + str(expected))
    print("Output:" + str(res))
    if res == expected:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
    
    root = build_tree(iter(test_2.split()), int)
    res = tree_max_depth(root)
    expected = 0
    print("Test 2 Expected:" + str(expected))
    print("Test 2 Output:" + str(res))
    if res == expected:
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
    
    root = build_tree(iter(test_3.split()), int)
    res = tree_max_depth(root)
    expected = 0
    print("Test 3 Expected:" + str(expected))
    print("Test 3 Output:" + str(res))
    if res == expected:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")
    
    root = build_tree(iter(test_4.split()), int)
    res = tree_max_depth(root)
    expected = 3
    print("Test 4 Expected:" + str(expected))
    print("Test 4 Output:" + str(res))
    if res == expected:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")
    
