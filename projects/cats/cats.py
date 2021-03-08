"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime



###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    #Implement choose, which selects which paragraph the user will type. 
    # It takes a list of paragraphs (strings), a select function that returns True for paragraphs that can be selected, and a non-negative index k. 
    # The choose function return's the kth paragraph for which select returns True. 
    # If no such paragraph exists (because k is too large), then choose returns the empty string.

    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    selected_paragraphs = []
    for element in paragraphs:
        if select(element):
            selected_paragraphs += [element] #selected_paragraphs.append(element) 
    
    if k <= len(selected_paragraphs)-1:
        return selected_paragraphs[k]
    else:
        return ""

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'

    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def is_topic_mentioned(paragraph): #parapraph is a string,choose from def choose
        lowered_paragraph = lower(paragraph)
        lowered_nopunc_paragraph = remove_punctuation(lowered_paragraph)
        lowered_nopunc_paragraph_list = split(lowered_nopunc_paragraph)
        for keyword in topic:
            if keyword in lowered_nopunc_paragraph_list:
                return True
        return False
    
    return is_topic_mentioned

    # END PROBLEM 2
 

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.') ###
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.') ###
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy("a  b  c  d", "b  a  c  d") ###
    50.0
    >>> accuracy("a b c d", " a d ")  ####
    25.0 
    >>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words ###
    100.0


    """
    typed_words = split(typed)
    reference_words = split(reference)

    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"

    if typed == "":
        return 0.0
    
    j=0

    for i in range(len(typed_words)):
        if (i+1) > len(reference_words):
            continue
        if typed_words[i] == reference_words[i]:
            j += 1
        
    return j/(i+1) * 100
    # END PROBLEM 3

    #If a typed word has no corresponding word in the reference because typed is longer than reference, then the extra words in typed are all incorrect.
    #If typed is empty, then the accuracy is zero.


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'

    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    length = len(typed)
    words = length / 5

    return words/(elapsed/60)

    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    #Important: if multiple strings have the same lowest difference according to the diff_function, 
    # autocorrect should return the string that appears first in valid_words.
    # Hint: Try using max or min with the optional key argument

    #However, if the lowest difference between user_word and any of the valid_words is greater than limit, then user_word is returned instead.


    difference_list = []

    if user_word in valid_words:
        return user_word

    for valid_single_word in valid_words:
        difference = diff_function(user_word ,valid_single_word, limit)
        difference_list += [difference]

    smallest_difference = min(difference_list)

    if smallest_difference > limit:
        return user_word
    
    i = 0

    for difference in difference_list:
        if smallest_difference == difference:
            return valid_words[i]
        i = i+1

    # END PROBLEM 5



# def shifty_shifts(start, goal, limit, depth = 0):
#     """A diff function for autocorrect that determines how many letters
#     in START need to be substituted to create GOAL, then adds the difference in
#     their lengths.
#     """
#     # BEGIN PROBLEM 6

#     if (start == "" and goal  == "") or depth > limit:
#         return 0

#     if start[:1] != goal[:1]:
#         depth += 1
#         return 1 + shifty_shifts(start[1:],goal[1:],limit,depth)
#     else:
#         return shifty_shifts(start[1:],goal[1:],limit,depth)


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

    def helper(start, goal,limit, depth):
        if (start == "" and goal  == "") or depth > limit:
            return 0
        if start[:1] != goal[:1]:
            depth += 1
            return 1 + helper(start[1:],goal[1:],limit,depth)
        else:
            return helper(start[1:],goal[1:],limit,depth)
    
    return helper(start, goal, limit, 0)

    # END PROBLEM 6
 




def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""  

    def helper(start, goal, limit, operation_times):
        """
        tell me the differnence between start and goal
        """
        if operation_times > limit:
            return 0
        if start == "":
            return len(goal)
        if goal == "":
            return len(start)
        if start[:1] == goal[:1]:
            return 0 + helper(start[1:], goal[1:], limit, operation_times)

        operation_times += 1
        post_add_diff =  helper(start, goal[1:], limit, operation_times)     #if add first letter
        post_remove_diff =  helper(start[1:], goal, limit, operation_times)  # if remove first
        post_substitute_diff =  helper(start[1:], goal[1:], limit, operation_times)  # if sub letter
        lowest_diff = min(post_add_diff,post_remove_diff,post_substitute_diff)
 
        return 1 + lowest_diff

    return helper(start, goal, limit, 0)


# >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
# 2
# >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring  ng ring ; ring ng
# 2
# >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus 


    # if len(start) == len(goal):
    #     subtimes = 0
    #     for i in range(len(start)):
    #         if start[i] == goal[i]:
    #             continue
    #         subtimes += 1
    #         if subtimes > limit:
    #             return subtimes
    #     return subtimes


    # def delete_func(start,goal,limit,delete_times = 0):
    # #     new_start_list = []
    # #     for letter in start:
    # #         if delete_times > limit:
    # #             return (new_start_list, delete_times)
    # #         if letter not in goal:
    # #             delete_times+=1
    # #             continue
    # #         new_start_list +=[letter] # new_start_list = ['k', 'i', 't', 'e', 's']
    # #     return (new_start_list, delete_times)
        
    

    # # def add_func(start,goal,limit,add_times = 0): # kites kittens ; es tens ; es ens; s  ns ; s s
    # #     """
    # #     how many modifications(add) from start to goal
    # #     """
    # #     start = "".join(start)    #concatenate new_start_list
    # #     if (start == "" and goal  == "") or (add_times + delete_times) > limit:
    # #         return 0
    # #     if start[:1] != goal[:1]:
    # #         add_times += 1
    # #         return 1 + add_func(start,goal[1:],limit,add_times)
    # #     else:
    # #         return add_func(start[1:],goal[1:],limit,add_times)
    
    
    # # new_start_list, delete_times = delete_func(start,goal,limit)
    # # add_times = add_func(new_start_list,goal,limit)

    # # return delete_times + add_times + subtimes

    # if ______________: # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # elif ___________: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # else:
    #     add_diff = ... # Fill in these lines
    #     remove_diff = ...
    #     substitute_diff = ...
    # #     # BEGIN
    # #     "*** YOUR CODE HERE ***"
    # #     # END


# #如果add了，分析add后的differnece
# 如果remove，分析differnce
# 如果sub，

# 然后选出最小的differnece。就说明更接近目标了。
# 执行那个操作。 并且 operation+1
# 然后把执行过的string再扔进去


# This is a recursive function with three recursive calls. One of these recursive calls will be similar to the recursive call in shifty_shifts.

# abcde
# uibcdef 不能单纯替换。del + add只要3步

# uibcdef
# abcde

#abcde
#bcdef

# >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
# 2
# >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring
# 2
# >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens ;把几种的组合都写出来，min ;
# 
#   
# 3 ckiteust  -> kittens     kitt; 找不到第二个t,找下一个e ; eust, tens找； 搜第二个t只要不是连续的，就先扔掉不看搜  eust ens

# 一旦有一个找不到。就考虑舍去t，找下一个。

# ckiteustab     kittenst       eustab   tenst(est)    eustab enst
# c iteustab        k iteuxstab

#    gvkoekem evmwoxz     ckg evmwoxz

    # comb_str_lst = [] #combined_string_list

    # def find_combined_string(start, goal ,limit, comb_str_lst=[]):
    #     drop = False         #是否可以要舍弃
    #     combined_string = ""

    #     for i in range(len(goal)):

    #         if goal[i:1+i] == start[i:1+i]:
    #             combined_string += goal[i:1+i]
    #         else:
    #             drop = not drop
    #             combined_string =       #不舍弃









def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########





def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"

    correctnum = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            correctnum+=1
        else:
            break
    
    progress_percentage = correctnum / len(prompt)

    send({'id': user_id, 'progress': progress_percentage})
    return progress_percentage

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    def helper(t):
        """
        given times_per_player [[1, 3, 5] player1, [2, 5, 6] player2], return timesspent [[2 first word, 2 second], [3, 1]] 
        """
        timespent = []
        for eachplayer_timestamp in t:      #eachplayer_timestamp [1, 3, 5] 
            eachplayer_timespent = []
            for i in range(len(eachplayer_timestamp)-1): 
                eachplayer_timespent += [eachplayer_timestamp[i+1] - eachplayer_timestamp[i]]  #eachplayer_timespent [2,2]
            timespent += [eachplayer_timespent]                                               #timespent  [[2, 2], [3, 1]] 
                
        return timespent

    return game(words, helper(times_per_player))   #game(words, times) ls:times should have the same amount of elements as ls:words


    #A game is a data abstraction that has a list of words and times. The times are stored as a list of lists of how long it took each player to type each word. 
    # times[i][j] indicates how long it took player i to type word j.
    # END PROBLEM 9


    #Timestamps are cumulative and always increasing, while the values in time are differences between consecutive timestamps. 
    # For example, if times_per_player = [[1, 3, 5], [2, 5, 6]], the corresponding time attribute of the game would be [[2, 2], [3, 1]] . 
    # Note that the first value of each list within times_per_player represents the initial starting time for each player.
    #Be sure to use the game constructor when returning a game, rather than assuming a particular data format. 
    # Read the definitions for the game constructor and selectors in cats.py to learn more about how the data abstraction is implemented.

# def game(words, times):
#     """A data abstraction containing all words typed and their times."""
#     assert all([type(w) == str for w in words]), 'words should be a list of strings'
#     assert all([type(t) == list for t in times]), 'times should be a list of lists'
#     assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
#     assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
#     return [words, times]

# def all_words(game):
#     """A selector function for all the words in the game"""
#     return game[0]

# def word_at(game, word_index):
#     """A selector function that gets the word with index word_index"""
#     assert 0 <= word_index < len(game[0]), "word_index out of range of words"
#     return game[0][word_index]


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word

    final_list = []
    for _ in player_indices:
        final_list += [[]] #final_list.append([])
        
    for word_index in word_indices:
        time_for_oneword = [time(game, play_num ,word_index) for play_num in player_indices]  
        #这里用了 list comprehension，套了()是generator，如果要调用index，必须先用list funct，调用geneexpress func生成一个list ; list(list comprehen)
        shortest_time = min(time_for_oneword)
        who_win = time_for_oneword.index(shortest_time)     #指定element直接 return index
        final_list[who_win] += [word_at(game, word_index)]

    return final_list
 

    # for word_index in word_indices:
    #     shortest_time = 100
    #     for play_num in player_indices:
    #         if time(game, play_num ,word_index) <= shortest_time:
    #             shortest_time = time(game, play_num ,word_index)

    #     for play_num in player_indices:
    #         if shortest_time == time(game, play_num ,word_index):
    #             final_list[play_num] += [word_at(game, word_index)]
    #             break

    # return final_list

                
# p0 = [2, 2, 3]
# p1 = [6, 1, 2]
# fastest_words(game(['What', 'great', 'luck'], [p0, p1]))




    # BEGIN PROBLEM 10

    # END PROBLEM 1[['What'], ['great', 'luck']]
#
#You can access words in the game with selectors word_at, which takes in a game and the word_index (an integer). 

#You can access the time it took any player to type any word using time.

#The fastest_words function returns a list of lists of words, one list for each player, and within each list the words they typed the fastest (against all the other players). 
#In the case of a tie, consider the earliest player in the list (the smallest player index) to be the one who typed it the fastest.



def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.



p0 = [2, 2, 3]
p1 = [6, 1, 2]
fastest_words(game(['What', 'great', 'luck'], [p0, p1]))


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)