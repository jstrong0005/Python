def win_percentage(wins, losses):
    total_games = wins + losses
    percent = (wins / total_games) * 100
    percent_formated = '{0:.4g}'.format(percent)
    print(percent_formated + '%')


print(win_percentage(10, 21))

#test the function
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100