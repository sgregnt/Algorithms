#----------------------------------
# cards
#----------------------------------

from collections import Counter, Set
# card parse

def parse_hand(hand):

    hand_unique = list(set(hand))
    hand_unique.sort(key=Counter(hand).get, reverse=True)

    if len(hand_unique) == 1:
        type = (3, int(hand_unique[0]))

    if len(hand_unique) == 2:
        type = (2, int(hand_unique[0]), int(hand_unique[1]))

    if len(hand_unique) == 3:
        type = (1, int(hand_unique[0]), int(hand_unique[1]), int(hand_unique[2]))

    return type

p1_hand = parse_hand(hand1)
p2_hand = parse_hand(hand2)


# if p1[0] > p2[0]:
#     return 'P1'
#
# if p2[0] > p1[0]:
#     return 'P2'
#
# if p2[1] > p1[1]:
#     return 'P1'
#
# if p2[2] > p1[1]:
#     return 'P1'
#
# if p2[1] > p1[1]:
#     return 'P1'
#
# if p2[2] > p1[1]:
#     return 'P1'



#----------------------------------
# online solution
#----------------------------------


# Q1: Three of a kind > a pair> high card
# value of each card from 0 to 9
def p1_win_count(hands):
    hands1 = hands[:3]
    hands2 = hands[3:]
    max_hand1, value1 = calculate_hands(hands1)
    max_hand2, value2 = calculate_hands(hands2)
    if max_hand1 > max_hand2:
        output = -1
    elif max_hand1 == max_hand2:
        if value1 > value2:
            output = -1
        elif value1 == value2:
            output = 0
        else:
            output = 1
    else:
        output = 1
    return output


def calculate_hands(hands):
    D = {}
    for i in hands:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    max_hand = max(D.values())
    if max_hand > 1:
        value = [i for i, x in D.items() if x == max_hand]
        return max_hand, value[0]
    else:
        value = max(D.keys())
        return max_hand, value


# hands](https://leetcode.com/problems/couples-holding-hands) = [1,2,2,4,5,6]
# print(p1_win_count(hands))
