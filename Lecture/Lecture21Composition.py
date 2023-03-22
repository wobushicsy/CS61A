from re import S
from turtle import right


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

def range_link(start, end):
    """Return a Link containing consecutive integers from start to end"""

    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def map_link(f, s):
    """Retuen a Link that contains f(x) for each x in Link s"""

    if s is Link.empty:
        return S
    else:
        return Link(f.start, map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x)
    is a true value"""

    if s is Link.empty:
        return s
    filter_rest = filter_link(f, s.rest)
    if f(s.start):
        return Link(s.start, filter_link(f, s.rest))
    else:
        return filter_rest

def add(s,v):
    """Add v to an ordered list s with no repeats, returning modified s."""
    """(Note: If v is already in s, then don't modify s, but still return it.)"""
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and not(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


"""Tree class"""
class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Yree(){0}{1}',format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  '+line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    """A Fibonacci tree"""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def leaves(t):
    """Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves

def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])

def prune(t, n):
    """Prune all sub-trees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)