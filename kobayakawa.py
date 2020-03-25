
import random

result = []

monte_max = 10000000

for monte_i in range(monte_max):

    player_num = 4

    yama = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    random.shuffle(yama)

    #print(yama)

    p = [0]*player_num
    total_point = [0]*player_num

    for i in range(player_num):
        p[i] = yama[i]
        #print(p[i])

    kobayakawa = yama[i+1]
    #print('kobayakawa', kobayakawa)

    min_er = p.index(min(p))

    #rint(min_er, p[min_er])

    for i  in range(player_num):
        if i == min_er:
            total_point[i] = p[i] + kobayakawa
        else:
            total_point[i] = p[i]

        #print(total_point[i])

    winner = total_point.index(max(total_point))
    #print('winner ', winner, ' has ' , total_point[winner], ' point.')
    koba_win = (min_er == winner)
    result.append([koba_win, total_point[winner]])


#print('result: ', result)

import numpy as np 

result = np.array(result)

print(result)

probability_koba_win = np.average(result, axis = 0)[0]
average_winner_total_point = np.average(result, axis = 0)[1]
print(probability_koba_win)
print(average_winner_total_point)