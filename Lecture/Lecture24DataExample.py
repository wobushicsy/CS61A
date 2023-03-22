"""Using Built-in Functions & Comprehensions"""
from re import L


def min_abs_indices1(s):
    """Indices of all elements in list s that have
    the smallest absolute value."""
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

def min_abs_indices2(s):
    """Indices of all elements in list s that have
    the smallest absolute value."""
    min_abs = min(map(abs, s))
    f = lambda i: s[i] == min_abs
    return list(filter(f, range(len(s))))


def largest_adj_sum1(s):
    """Largest sum of two adjacent elements in a list s"""
    return max([s[i] + s[i+1] for i in range(len(s)-1)])

def largest_adj_sum2(s):
    """Largest sum of two adjacent elements in a list s"""
    return max([a + b for a, b in zip(s[:-1], s[1:])])


def digit_dict(s):
    """Map each digit d to the lists of elements in s that 
    end with d."""
    return {d:[x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}


def all_have_an_equal(s):
    """Does every element equal some other element in s?"""
    return min([sum([1 for y in s if y == x] for x in s)]) > 1



"""Linked List Exercise"""
def ordered(s, key=lambda x:x):
    """Is Link s ordered?"""
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest, key)


def merge(s, t):
    """Return a sorted Link with the elements of sorted s & t"""
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))


def merge_in_place(s, t):
    """Return a sorted Link with the elements of sorted s & t, 
    but never call Link"""
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t



class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
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