# Tree

def tree(lable, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'        #Verifirs the tree definition
    return  [lable] + list(branches)            #list(branches) <-- Creates a list from a sequence of branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:     #type(tree) != list <-- Verifies that tree is bound to a list
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left_tree, right_tree = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left_tree)+label(right_tree), [left_tree, right_tree])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(tree)])

def leaves(tree):
    """Return a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

###---------- Creating Trees ----------###
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)


def increment(t):
    """Return a tree like t but with all labels incremented"""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])