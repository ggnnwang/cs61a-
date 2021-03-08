# make_city(name, lat, lon): Creates a city object with the given name, latitude, and longitude.
# We also have the following selectors in order to get the information for each city:

# get_name(city): Returns the city's name
# get_lat(city): Returns the city's latitude
# get_lon(city): Returns the city's longitude

from math import sqrt

def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(1,[tree(3)]), tree(1)])])
    >>> height(t)
    3
    """
    
    if not branches(t):
        return 0
    branches_height = []
    for branch in branches(t):
        branches_height.append(height(branch))
    return max(branches_height) + 1


#Write a function that takes in a tree and returns the maximum sum of the values
#along any path in the tree. Recall that a path is from the tree’s root to any leaf.

def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    label_num = label(t)
    if not branches(t):
        return label_num
    path_sums = []
    for branch in branches(t):
        path_sums.append(max_path_sum(branch))
    return max(path_sums) + label_num




def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if not branches(tree):
        return [x] if label(tree) == x else None
    for branch in branches(tree):
        path = find_path(branch,x)
        if path:
            return [label(tree)] + path




def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    return [[s[i], t[i]] for i in range(len(s))]


def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"

    alat = get_lat(city_a)
    # 尽量用selector，而不是city_a[0]，因为我不需要去弄清楚city_a的数据结构是如何的，不需要研究 city_a underlying implementation。
# The nature of the abstraction barrier guarantees that changing the implementation of an ADT shouldn't affect the functionality of any programs that use that ADT,
# as long as the constructors and selectors were used properly.
    alon = get_lon(city_a)
    blat = get_lat(city_b)
    blon = get_lon(city_b)
    return sqrt((alat-blat)**2 + (alon-blon)**2)


def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"

    # Hint: How can you use your distance function to find the distance between the given location and each of the given cities?

    # 尽量用constructor，而不是想办法city_a[1]找到city_a的latlon。
    city_temp = make_city('city_temp_name', lat, lon)

    if distance(city_a, city_temp) >= distance(city_b, city_temp):
        return get_name(city_b)
    else:
        return get_name(city_a)


def check_city_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """


# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name": name, "lat": lat, "lon": lon}
    else:
        return [name, lat, lon]


def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]


def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]


def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]


def change_abstraction(change):
    change_abstraction.changed = change


change_abstraction.changed = False


#########################################################
# def tree(root_label, branches=[]):
#     for branch in branches:
#         assert is_tree(branch), 'branches must be trees'
#     return [root_label] + list(branches)

# def label(tree):
#     return tree[0]

# def is_tree(tree):
#     if type(tree) != list or len(tree) < 1:
#         return False
#     for branch in branches(tree):
#         if not is_tree(branch):
#             return False
#     return True
# #A tree is well-formed only if it has a root label and all branches are also trees.
# # The is_tree function is applied in the tree constructor to verify that all branches are well-formed.

# def is_leaf(tree):
#     return not branches(tree)

# def branches(tree):
#     return tree[1:]

# constructor tree
#  the selectors label and branches.
#########################################################

def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree( 'roots',   [   tree('branch1', [tree('leaf'), tree('berry')]),   tree('branch2')  ]           )
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"

    # def helper(t,result):
    #     if label(t) == "berry":
    #         return True
    #     else:
    #         for branch in branches(t):
    #             result += int(helper(branch, result))
    #         return (True if result > 0 else False)

    # return helper(t,0)

    if label(t) == "berry":
        return True

    for branch in branches(t):
        if berry_finder(branch):
            return True

    return False

    # The squirrels on campus need your help! There are a lot of trees on campus and the squirrels would like to know which ones contain berries.
    # Define the function berry_finder, which takes in a tree and returns True if the tree contains a node with the value 'berry' and False otherwise.
# Hint: Considering using a for loop to iterate through each of the branches recursively!


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"

    #sprout_leaves(t, [5, 6])

    if is_leaf(t):
        leaves_branches = []
        for leaf in leaves:
            leaves_branches += [tree(leaf)]
        # leaves_branches = [ [5] ,[6] ]
        return tree(label(t), leaves_branches)

    # Wrong
    # if is_leaf(t):
    #     for leaf in leaves:
    #         t += [[leaf]]
    #     return t

    allbranches = []
    for branch in branches(t):
        allbranches += [sprout_leaves(branch, leaves)]

    return tree(label(t), allbranches)

# python3 ok -q sprout_leaves --local
# python3 ok -q check_abstraction --local


# Abstraction tests for sprout_leaves and berry_finder
def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    >>> change_abstraction(False)
    """


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if (fn(x) >= lower and fn(x) <= upper)]


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    return [(deck[i//2] if i % 2 == 0 else deck[i//2+len(deck)//2]) for i in range(len(deck))]

    # Assuming the deck (sequence) contains an even number of cards, write a list comprehension that produces the shuffled sequence.


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    # built-in zip function to iterate over multiple sequences at once.

    if not t1:     #下面中间绿的那段如果用了，这一段就删掉。
        return t2
    if not t2:
        return t1

    label_new = label(t1) + label(t2)
    branches_t1, branches_t2 = branches(t1), branches(t2)
    branchest1t2 = []

    for i in range(max(len(branches_t1), len(branches_t2))):
        a = branches_t1[i:i+1]
        b = branches_t2[i:i+1]
        if a:
            a = a[0]
        if b:
            b = b[0]
        branchest1t2.append((a, b))

    branches_new = []

    for branch_t1, branch_t2 in branchest1t2:
        # if branch_t1 == []:
        #     branches_new.append(branch_t2)
        #     continue
        # elif branch_t2 == []:
        #     branches_new.append(branch_t1)
        #     continue
        branches_new.append(add_trees(branch_t1, branch_t2))

    return tree(label_new, branches_new)

# python3 ok -q add_trees --local
#(tree(2),       tree(3, [tree(4), tree(5)]))
#[]           [ [4] , [5]    ]

    # >>> print_tree(add_trees(numbers, numbers))
    # 2
    #   4
    #     6
    #     8
    #   10
    #     12
    #       14
    #     16

    # label_new = label(t1) + label(t2)

    # branches_t1, branches_t2 = branches(t1) ,branches(t2)
    # branchest1t2 = (zip(branches_t1,branches_t2))
    # branches_new = []

    # for branch_t1,branch_t2 in branchest1t2:
    #     branches_new += [add_trees(branch_t1, branch_t2)]

    # for branch_t1 in branches_t1[len(branches_t2):]:
    #     branches_new += [branch_t1]

    # for branch_t2 in branches_t2[len(branches_t1):]:
    #     branches_new += [branch_t2]

    # return tree(label_new, branches_new)


def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists ofl successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev]=[]
        table[prev].append(word)
        prev = word
    return table


def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        ls = table[word]
        next_word = random.choice(ls)

        if result == '':
            result = word

        if next_word in ['.', '!', '?']:
            return result.strip() + next_word

        result = result + " " + next_word
        word = next_word
 
# table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
# construct_sent('Wow', table)
# python3 ok -q construct_sent --local

    #Hint: to randomly select from a list, import the Python random library with import random and use the expression random.choice(my_list)


def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open(path, encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)


def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)


# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change


change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
 