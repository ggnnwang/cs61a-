def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:   #tree必须是个list，长度必须大于1。 []就不是，[0]就是
        return False
    for branch in branches(tree):             #tree的所有branches，必须也全部是tree； 没有branches的tree比如[0]，直接跳过了这个for判断条件。 #[5,6,7]就不是tree，因为假设[5,6,7]是tree
        if not is_tree(branch):               #[6,7]就是他的branches, 现在看6是不是tree？显然不是。 [5, [6], [7]] 才是tree
            return False
    return True
#A tree is well-formed only if it has a root label and all branches are also trees. 
# The is_tree function is applied in the tree constructor to verify that all branches are well-formed.

def is_leaf(tree):
    return not branches(tree)


#从来没有leaf，只有没有branches的branch。

def branches(tree):
    return tree[1:]

# constructor tree 
#  the selectors label and branches.

 
# t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])    # [3, [1], [2, [1], [1]]]

 
# >>> label(t)
# 3
# >>> branches(t) 有两个
# [      [1],      [ 2, [1], [1] ]         ]
# >>> label(branches(t)[1])
# 2
# >>> is_leaf(t)
# False
# >>> is_leaf(branches(t)[0])
# True







t1 = tree(1,
               [tree(2,
                     [tree(3),
                      tree(4)]),
                tree(5,
                     [tree(6,
                           [tree(7)]),
                      tree(8)])])

t2 = tree(1,
               [tree(2,
                     [tree(3),
                      tree(4)])])




def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if t.label == value:
        yield [value]
    for branch in t.branches:
        for path in path_yielder(branch, value):
            yield [t.label] + path


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()




t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
next(path_yielder(t1, 6))
