def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        nonlocal balance

        if message == "deposit":
            balance += amount
            return balance

        elif message == "withdraw":
            if balance < amount:
                return 'Insufficient funds'
            balance -= amount
            return balance

        else:
            return 'Invalid message'

        "*** YOUR CODE HERE ***"
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"

    incorrect_pwls = []

    def withdraw(amount, pwinput):
        nonlocal balance

        if len(incorrect_pwls) == 3:
            return "Frozen account. Attempts: " + str(incorrect_pwls)

        if pwinput == password:
            if amount < balance:
                balance -= amount
                return balance
            return 'Insufficient funds'
        else:
            incorrect_pwls.append(pwinput)
            return 'Incorrect password'

    return withdraw


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    i = 1
    x = next(t)
    y = next(t)

    while True:
        if x == y:
            i += 1
            if i >= k:
                break
        else:
            i = 1
        x = y
        y = next(t)

    return x


def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
 
#########
    seq = list(seq)

    if len(seq) == 1:
        yield seq
        return

    for i in range(len(seq)):
        seq_copy = seq[:]
        first_element = seq_copy.pop(i)
        for perm in permutations(seq_copy):
            yield [first_element] + perm

###########
    # if len(seq) == 1:
    #     yield seq
    #     return

    # first_element = seq[0]
    # generator_remaining = permutations(seq[1:])x

    # for output in generator_remaining:
    #     output = list(output)
    #     output_backup = list(output) #output_backup = output[:]    .copy()

    #     for i in range(len(seq)):
    #         output.insert(i, first_element)
    #         yield output
    #         output = list(output_backup)

    # say teq:【3，4，2，6】
    


########
    # seq = list(seq)
    # ls = [0 for _ in range(len(seq))] # variations of [0, 0, 0, 0] [1,2,0,0] [2,1,1,0] ...
    # # when ls meet stop_ls [3, 2, 1, 0] stop loop
    # stop_ls = [i for i in range(len(seq)-1, -1, -1)]
    # total_perms = []

    # while True:
    #     seq_copy = seq[:]
    #     # pick up element from seq instructed by ls
    #     perm = [seq_copy.pop(k) for k in ls]
    #     total_perms.append(perm)

    #     if ls == stop_ls:
    #         break

    #     # over
    #     ls[-1] += 1

    #     # digit in
    #     i = 1
    #     while i <= len(ls):
    #         if ls[-i] == i:
    #             ls[-i] = 0
    #             ls[-i-1] += 1
    #         i += 1

    # yield from iter(total_perms)



    # [1,4,5,3,3]

    # leng = len(seq)
    # pos = 0
    # def helper(seq, pos, leng):
    #     for pos in range(len(seq)):
    #         seq[pos]




#withdraw(amount, pwinput)
def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
 
#withdraw(amount, pwinput)
# def make_joint(withdraw, old_pass, new_pass):
    message = withdraw(0, old_pass)
    if type(message) == str:
        return message

    def joint_account(amount, passinput):
        if passinput == new_pass:
            return withdraw(amount, old_pass)
        return withdraw(amount, passinput)

    return joint_account
        
# w = make_withdraw(100, 'hax0r')
# make_joint(w, 'my', 'secret')
# j = make_joint(w, 'hax0r', 'secret')
# j(25, 'secret')
# j(100, 'secret')
# j2 = make_joint(j, 'secret', 'code')
# j2(5, 'code')
# j2(5, 'secret')
# j2(5, 'hax0r')
# j2(25, 'password')
# j2(25, 'password')
# j2(25, 'password')


    #The solution is short (less than 10 lines) and contains no string literals! 
    # The key is to call withdraw with the right password and amount, then interpret the result. 
    # You may assume that all failed attempts to withdraw will return some string (for incorrect passwords, locked accounts, or insufficient funds), 
    # while successful withdrawals will return a number. type(value) == str to test if some value is a string:





def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"

    for i in range(m):
        def generator_func(i):
            natural_num = naturals()
            for number in natural_num:
                output = (number-1) * 4 + i % 4
                if output == 0:
                    continue
                yield output
        yield generator_func(i)

