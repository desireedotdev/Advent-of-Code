# --- Day 1: Historian Hysteria ---
# The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.
# As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.
# Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?
# Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.
# There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

# For example:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
# In the example list above, the pairs and distances would be as follows:

#     The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
#     The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
#     The third-smallest number in both lists is 3, so the distance between them is 0.
#     The next numbers to pair up are 3 and 4, a distance of 1.
#     The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
#     Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.

# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!
# Your actual left and right lists contain many location IDs. What is the total distance between your lists?

# This reads the supplied file and converts each column into a list
def read_input():
  list_a, list_b = [], []
  with open("day_1_input.txt") as input:
    for line in input:
      values = line.split("   ");
      list_a.append(int(values[0]))
      list_b.append(int(values[1]))

    # This is simple test data
    # list_a, list_b = [3, 2, 1, 4], [2, 2, 2, 4]

  list_a.sort()
  list_b.sort()

  return list_a, list_b

def calculate_distance(list_a, list_b): 
    total = 0
    if len(list_a) != len(list_b):
        return -1
    else:
        for index, number in enumerate(list_a):
            total = total + abs(list_a[index] - list_b[index])
    print(total)

def calculate_similarity(list_a, list_b):
    total = 0
    if len(list_a) != len(list_b):
            return -1
    else:
        hashmap = {}
        for number in list_b:
            hashmap[number] = hashmap.get(number, 0) + 1 

        for number in list_a:
            if number in hashmap:
                total += number * hashmap[number]
                
    print(total)


# Quicksort implementation - for reference only
def quick_sort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1

list_a, list_b = read_input()

calculate_distance(list_a, list_b)
# 1873376

calculate_similarity(list_a, list_b)
# 18997088