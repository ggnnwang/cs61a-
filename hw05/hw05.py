class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, product, price, amount=0, balance=0):
        self.product = product
        self.price = price
        self.amount = amount
        self.balance = balance

    def vend(self):
        if self.amount == 0:
            self.vprint('Inventory empty. Restocking required.')
            return
        elif self.amount > 0:
            if self.balance < self.price:
                self.vprint('You must add ${0} more funds.'.format(
                    self.price - self.balance))
                return
            appendent = ' and ${0} change'.format(
                self.balance - self.price) if self.balance - self.price > 0 else ''
            self.vprint('Here is your {0}{1}.'.format(self.product, appendent))
            self.amount -= 1
            self.balance = 0

    def add_funds(self, k):
        self.balance += k
        if self.amount == 0:
            self.vprint(
                'Inventory empty. Restocking required. Here is your ${0}.'.format(self.balance))
            self.balance = 0
            return
        self.vprint('Current balance: ${0}'.format(self.balance))

    def restock(self, n):
        self.amount += n
        self.vprint('Current {0} stock: {1}'.format(self.product, self.amount))

    def vprint(self, string):
        print("'{0}'".format(string))


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        a = kind(self.year)
        #a.cents =kind.cents
        return a

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.current_year


class Coin:
    cents = 0

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + max(Mint.current_year - self.year - 50, 0)


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"

    # def length(n):
    #     """"""
    #     if n //10 == 0:
    #         return 1
    #     return 1 + length(n // 10)

    # if length(n) == 1:
    #     return Link(n)
    # first, remainder_link = n // (10**(length(n)-1)), store_digits(n % (10**(length(n)-1)))
    # return Link(first, remainder_link)

    # linkls = Link(n % 10)
    # while n // 10:
    #     n = n // 10
    #     linkls.rest = linkls.copy()
    #     linkls.first = n % 10
    # return linkls

    old_link = Link(n % 10)
    while n // 10:
        n = n // 10
        new_link = Link(n % 10, old_link)
        old_link = new_link
    return old_link


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"

    def maxtree(t):
        if t.is_leaf():
            return t.label
        return max(max([maxtree(branch) for branch in t.branches]), t.label)

    def mintree(t):
        if t.is_leaf():
            return t.label
        return min(min([mintree(branch) for branch in t.branches]), t.label)
        
    if t.is_leaf():
        return True
    if len(t.branches) > 2:
        return False

    if len(t.branches) == 1:
        newroot = t.branches[0]
        if newroot.label > t.label:
            if mintree(newroot) < t.label:
                return False
        elif newroot.label < t.label:
            if maxtree(newroot) > t.label:
                return False
        elif newroot.label == t.label:
            return is_bst(newroot)

    if len(t.branches) == 2:
        if maxtree(t.branches[0]) > t.label:
            return False
        if mintree(t.branches[1]) < t.label:
            return False

    for branch in t.branches:
        if not is_bst(branch):
            return False

    return True


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder travesal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"

    if t.is_leaf():
        return [t.label]
    return [t.label] + sum([preorder(branch) for branch in t.branches],[])



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
          7
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

    def copy(self):
        if self.rest == Link.empty:
            return Link(self.first)
        return Link(self.first, self.rest.copy())


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
