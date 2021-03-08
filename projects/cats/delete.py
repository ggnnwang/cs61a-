def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


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


#from cats import game, game_string, time_per_word, all_words, all_times, word_at, time
p = [[1, 4, 6, 7], [0, 4, 6, 9]]
words = ['This', 'is', 'fun']
game = time_per_word(p, words)


p0 = [2, 2, 3]
p1 = [6, 1, 2]
fastest_words(game(['What', 'great', 'luck'], [p0, p1]))