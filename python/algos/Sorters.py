__author__ = 'nitish'

class Sorters():
    def __init__(self):
        pass

    def insertionsort(self, input_list):
        for index in range(1, len(input_list)):
            cur_val = input_list[index]
            position = index
            # Find the correct place to put cur_val in the unsorted list
            # Insertion sort takes elements one by one and "inserts" them in the correct index
            while position>0 and input_list[position -1]>cur_val:
                input_list[position] = input_list[position-1]
                position = position-1
            # Position is the correct index for cur_val in the sub_list 0 uptil size index -> this sublist is sorted
            input_list[position] = cur_val

    def bubblesort(self, input_list):
        for sublist_size in range(len(input_list)-1, 0, -1):
            # Unsorted sublist is of size sublist_size
            # Idea is to keep swapping right such that Largest number is put at last index in first pass, etc.
            for i in range(sublist_size):
                if input_list[i]>input_list[i+1]:
                    # Swap
                    tmp = input_list[i+1]
                    input_list[i+1] = input_list[i]
                    input_list[i] = tmp

    def selectionsort(self, input_list):
        for slot_to_fill in range(len(input_list)-1, 0, -1):
            # Unsorted sublist is of size slot_to_fill
            # Idea is to find the largest number in sublist and then swap once to correct position (last, 2nd last, etc)
            pos_of_largest = 0
            for i in range(1,slot_to_fill+1):
                if input_list[i]>input_list[pos_of_largest]:
                    pos_of_largest = i

            # Swap
            tmp = input_list[slot_to_fill]
            input_list[slot_to_fill] = input_list[pos_of_largest]
            input_list[pos_of_largest] = tmp


if __name__ == '__main__':
    input_list = [54,26,93,17,77,31,44,55,20]
    sorter = Sorters()
    sorter.insertionsort(input_list)
    print "Insertion sorted list = " + str(input_list)
    input_list_2 = [55,26,93,90,77,31,11,55,04]
    sorter.bubblesort(input_list_2)
    print "Bubble sorted list = " + str(input_list_2)
    input_list_3 = [54,33,93,17,77,31,22,55,20]
    sorter.selectionsort(input_list_3)
    print "Selection sorted list = " + str(input_list_3)
