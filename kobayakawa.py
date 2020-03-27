import random

result = []

monte_max = 1000000

cnt_winner_card = [0] * 15

# [[], []]
# [[player_card1,player_card2,player_card3,...], [player_card1,player_card2,player_card3,...]]
winner_player_kobayakawa = [[0] * 15 for i in range(15)]

for monte_i in range(monte_max):

    player_num = 4

    yama = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    random.shuffle(yama)

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

    winner_card = p[winner]
    cnt_winner_card[winner_card - 1] +=1

    winner_player_kobayakawa[kobayakawa-1][winner_card-1] += 1



#print('result: ', result)

import numpy as np 

result = np.array(result)

print(result)

probability_koba_win = np.average(result, axis = 0)[0]
average_winner_total_point = np.average(result, axis = 0)[1]
print(probability_koba_win)
print(average_winner_total_point)

result_total_point = [i[0] for i in result]

import scipy
from scipy.special import comb

C14_3 = comb(14, 3, exact=True)


probability_min = [0] * 15
for i in range(1,16):
    tmp_c = comb(15 - i, 3, exact=True)
    probability_min[i-1] = tmp_c / C14_3
    
    print(i, " : " , probability_min[i-1])



for i in range(15):
    print("card", i+1, " : ", cnt_winner_card[i]/monte_max)

print('winner player card - kobayakawa ', winner_player_kobayakawa)
for kobayakawa_i in range(15):
    print('kobayakawa ',kobayakawa_i)
    for player_card_i in range(15):
        print(winner_player_kobayakawa[kobayakawa_i][player_card_i])
