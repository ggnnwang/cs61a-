"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***" # Make sure you call dice exactly num_rolls times!

    sum = 0
    each_call_outcome = 0
    pig_pass = False

    for i in range(num_rolls):
        each_call_outcome = dice()
        sum = sum + each_call_outcome
        if each_call_outcome == 1:
            pig_pass = True
    
    if pig_pass == True:
        sum = 1

    return sum

    # END PROBLEM 1


def free_bacon(score): 
    #You may not use for loops or square brackets [ ] in your implementation, 
    # since we haven't covered those yet.
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    
    pi = pi // 10 ** (101-(score+1))
    return 3 + (pi % 10)


    # END PROBLEM 2

    return pi % 10 + 3


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """

    #Implement the take_turn function, which returns the number of points scored for a turn by rolling the given dice num_rolls times. 
    # Your implementation of take_turn should call both roll_dice and free_bacon when possible.


    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'

    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"

    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)

    # END PROBLEM 3


def extra_turn(player_score, opponent_score):
    """Return whether the player gets an extra turn."""
    return (pig_pass(player_score, opponent_score) or
            swine_align(player_score, opponent_score))


def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """

    # Implement swine_align, which takes the current player and opponent scores and returns 
    # whether the current player will take another turn due to Swine Align. 
    # Note: In the special case where one score is 0, return False.
    # Hint: The expression n % d == 0 is true if and only if n is a multiple of d.

    # BEGIN PROBLEM 4a
    "*** YOUR CODE HERE ***"

    if player_score ==0 or opponent_score ==0:
        return False
    
    gcd = 10
    
    while gcd <= min(player_score, opponent_score):
        if player_score % gcd == 0 and opponent_score % gcd == 0:
            return True
        gcd +=1
    
    return False

 
    # END PROBLEM 4a


def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> pig_pass(9, 12)
    False
    >>> pig_pass(10, 12)
    True
    >>> pig_pass(11, 12)
    True
    >>> pig_pass(12, 12)
    False
    >>> pig_pass(13, 12)
    False
    """
    # BEGIN PROBLEM 4b
    "*** YOUR CODE HERE ***"

    difference = opponent_score - player_score
    
    if difference == 1 or difference == 2:
        return True
    else:
        return False

    # END PROBLEM 4b


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """

    #. A strategy is a function that, given a player's score and their opponent's score, 
    # returns the number of dice that the current player will roll in the turn. 
    # Only call a strategy function once per turn (or risk breaking the GUI).

    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    current_player_score =0

    while True:

        if who == 0:
            strategy = strategy0
            current_player_score = score0
            opponent_score = score1
        else: #who ==1
            strategy = strategy1
            current_player_score = score1
            opponent_score = score0

        num_rolls = strategy(current_player_score,opponent_score)
        current_player_score += take_turn(num_rolls,opponent_score,dice)

        #立刻更新分数。
        if who == 0: 
            score0 = current_player_score
        else: #who ==1
            score1 = current_player_score

        
        # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
        # BEGIN PROBLEM 6
        "*** YOUR CODE HERE ***"
        say = say(score0, score1)    #  say:  The commentary function to call at the end of the first turn.
        # END PROBLEM 6
        
        if current_player_score >= goal:
            break

        if extra_turn(current_player_score, opponent_score) == False:
            who =other(who)     #换人
    

    return score0, score1

  
  #>>> # Ensure that say is properly updated within the body of play.
    #######>>> def total(s0, s1):
#...     print(s0 + s1)
#...     return echo
#>>> def echo(s0, s1):
#...     print(s0, s1)
##...     return total
#>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
    


#######
# s0      s1
#  0       0
#  4      12 
#  3+pi(12)

#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


    #Since commentary can differ from turn to turn depending on the current point situation in the game,
    # a commentary function always returns another commentary function to be called on the next turn. 
    # The only side effect of a commentary function should be to print.


# The return value of calling a commentary function gives you the commentary function to call on the next turn.
#For example, say(score0, score1) should be called at the end of the first turn. 
# Its return value (another commentary function) should be called at the end of the second turn. 
# Each consecutive turn, call the function that was returned by the call to the previous turn's commentary function.#


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"

    

    if who ==0:
        def say(score0,score1):
            a_running_high = running_high
            difference = score0 - last_score

            if difference > running_high:
                print (difference,"point(s)! The most yet for Player",who)
                a_running_high = difference
            a_last_score = score0
            return announce_highest(0, a_last_score, a_running_high)
        
    if who ==1:
        def say(score0,score1):
            a_running_high = running_high
            difference = score1 - last_score

            if difference > running_high:
                print (difference,"point(s)! The most yet for Player",who)
                a_running_high = difference
            a_last_score = score1
            return announce_highest(1, a_last_score, a_running_high)

    return say

 #f0 = announce_highest(1)

 #f0: 
 #==  def say(score0,score1):
            # a_running_high = 0
           # difference = score1 - 0
            #if difference > 0:
            #    print (difference,"point(s)! The most yet for Player", 1)
             #   a_running_high = difference
            #a_last_score = score1
            #return announce_highest(1, a_last_score, a_running_high)

#f0(0,9)





    # END PROBLEM 7

    #E.g., announce_highest(1) ignores Player 0 entirely and just print information about Player 1. 
    # (So does its return value; another commentary function about only Player 1.) 
    # To compute the gain, it must compare the score from last turn (last_score) to the score 
    # from this turn for the player of interest, which is designated by the who argument. 
    # This function must also keep track of the highest gain for the player so far, which is store as running_high


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, trials_count=5000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
 

    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"



    def averaged_function(*args):
        
        averaged_result = 0
        sum = 0

        for i in range(trials_count):
            sum = sum+ original_function(*args)
            
        averaged_result = sum / trials_count

        return averaged_result
        
    return averaged_function

    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, trials_count=5000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """ 
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***" #. Your implementation should use make_averaged and roll_dice.

    best_number = 1
    trying_number = 1
    average_turn_score = 0
    highest_score = 0

    function_returning_average_value = make_averaged(roll_dice,trials_count)

    while trying_number <= 10: 

        average_turn_score = function_returning_average_value(trying_number,dice)

        if average_turn_score > highest_score:
            highest_score = average_turn_score
            best_number = trying_number
            
        trying_number += 1
    return best_number

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test always_roll(3)
        print('always_roll(3) win rate:', average_win_rate(always_roll(3)))

    if False:  # Change to True to test always_roll(10)
        print('always_roll(10) win rate:', average_win_rate(always_roll(10)))


    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test bacon_strategy2
        print('bacon_strategy2 win rate:', average_win_rate(bacon_strategy2))

    if True:  # Change to True to test extra_turn_strategy
        print('extra_turn_strategy win rate:', average_win_rate(extra_turn_strategy))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """

    # BEGIN PROBLEM 10
    return 0 if free_bacon(opponent_score)>=cutoff else num_rolls
    # END PROBLEM 10

def bacon_strategy2(score, opponent_score, cutoff=9, num_rolls=6):     # 平均值每扔一次6个骰子+8.6左右
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """

    # BEGIN PROBLEM 10
    return 0 if free_bacon(opponent_score)>=cutoff else num_rolls
    # END PROBLEM 10


def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    return 0 if (extra_turn(score+free_bacon(opponent_score),opponent_score) == True) or (free_bacon(opponent_score)>=cutoff) else num_rolls
    # END PROBLEM 11


    #The extra turn strategy always rolls 0 if doing so triggers an extra turn. 
    # In other cases, it rolls 0 if rolling 0 would give at least cutoff points. 
    # Otherwise, the strategy rolls num_rolls.


def final_strategy(score, opponent_score, cutoff=8 ,num_rolls=6):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    score_to_goal = 100 - score
    assert score_to_goal >0, "score_to_goal must be +0"
    

    while score_to_goal >= 9:
        if extra_turn(score+free_bacon(opponent_score),opponent_score)  or free_bacon(opponent_score)>=cutoff:
            return 0
        else:
            return num_rolls

    if extra_turn(score+free_bacon(opponent_score),opponent_score)  or (free_bacon(opponent_score)>=cutoff):
        return 0
    if score_to_goal <= 3:
        return 0
    elif score_to_goal <= 4:
        return 2
    elif score_to_goal <= 6:
        return 3
    elif score_to_goal <= 7:
        return 4
    else:
        return 5

        
    # END PROBLEM 12


#extra_turn_strategy is a good default strategy to start with.
##There's no point in scoring more than 100. Check whether you can win by rolling 0, 1 or 2 dice. If you are in the lead, you might take fewer risks.
#Try to force extra turns.
#Choose the num_rolls and cutoff arguments carefully.
#Take the action that is most likely to win the game.




##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

