try:
    fhand = open('scores.txt', 'r')
except:
    print("File does not exist")


score_array = []


def scores_to_array():
    for row in fhand:
        print()
        print(row)
        row = row.rstrip().split(',')
        score_array.append(int(row[1]))

    print()

    return score_array
scores_to_array()


def grade_scores():
    highscore = max(score_array)
    lowscore = min(score_array)
    total = 0

    for score in (score_array):
        total = total + int(score)
    
    avg = round((total / len(score_array)), 2)
    all_scores = [highscore, avg, lowscore]
    return all_scores


def displayscore():
    all_scores = grade_scores()
    print()
    print("High Score: ", all_scores([0]))
    print()
    print("Average: ", all_scores[1])
    print()
    print("Low Score: ", all_scores[2])
    print()


# Main
displayscore()
