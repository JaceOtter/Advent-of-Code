card_value = {"J":0, "2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "Q":10, "K":11, "A":12}

def hand_type(hand):
    card_values = [0]*13
    for i in range(5):
        card = hand[i]
        card_values[card_value[card]] += 1

    m = sorted(card_values[1:])
    tot = m[-1] + card_values[0]

    if tot == 5:
        return 6
    elif tot == 4:
        return 5
    elif tot == 3 and m[-2] == 2:
        return 4
    elif tot == 3:
        return 3
    elif len([i for i in range(13) if card_values[i] == 2]) == 2:
        return 2
    elif tot == 2:
        return 1
    else:
        return 0

# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
def is_less_than_or_equal(a, b):
    for i in range(5):
        if card_value[a[i][0]] < card_value[b[i][0]]:
            return True
        elif card_value[a[i][0]] > card_value[b[i][0]]:
            return False
 
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high][0]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if is_less_than_or_equal(array[j][0], pivot):
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)



File_object = open(r"./AoC23/Inp.txt", "r")
lines = File_object.readlines()

hands = [[], [], [], [], [], [], []]
for line in lines:
    [hand, bid] = line.strip().split()
    hands[hand_type(hand)].append([hand, bid])

#print(hands)

big_list = []
for i in range(7):
    n = len(hands[i])
    if n > 1:
        quickSort(hands[i], 0, len(hands[i])-1)
    for pair in hands[i]:
        big_list.append(pair)
    
s = 0
for i in range(len(big_list)):
    s += (i+1)*int(big_list[i][1])

print(s)
