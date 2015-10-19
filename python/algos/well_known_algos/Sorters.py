__author__ = 'nitish'
import os
import sys
cur_dir = os.path.dirname(__file__)
sys_path_dir = os.path.join(cur_dir, '../../../')
sys.path.append(sys_path_dir)
from python.tools.Generators import Generators


class Sorters():
    def __init__(self):
        pass

    def insertionSort(self, input_list):  # O(n^2)
        for index in range(1, len(input_list)):
            cur_val = input_list[index]
            position = index
            # Find the correct place to put cur_val in the unsorted list
            # Insertion sort takes elements one by one and "inserts" them in the correct index
            while position > 0 and input_list[position-1] > cur_val:
                input_list[position] = input_list[position-1]
                position -= 1
            # Position is the correct index for cur_val in the sub_list 0 uptil size index -> this sublist is sorted
            input_list[position] = cur_val

    def bubbleSort(self, input_list):  # O(n^2)
        for sublist_size in range(len(input_list)-1, 0, -1):
            # Unsorted sublist is of size sublist_size
            # Idea is to keep swapping right such that Largest number is put at last index in first pass, etc.
            for i in range(sublist_size):
                if input_list[i]>input_list[i+1]:
                    # Swap
                    tmp = input_list[i+1]
                    input_list[i+1] = input_list[i]
                    input_list[i] = tmp

    def selectionSort(self, input_list):  # O(n^2)
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

    def quickSort(self, input_list):  # O(nlogn)
        # Call to resursive funtion passing full list
        self.quickSortSplitter(input_list, 0, len(input_list) - 1)

    def quickSortSplitter(self, input_list, first, last):

        if first < last:  # Sublist is of size>1
            # Find Pivot point
            pivot = self.partition(input_list, first, last)
            # Sort the sublists recursively
            self.quickSortSplitter(input_list, first, pivot - 1)
            self.quickSortSplitter(input_list, pivot + 1, last)

    def partition(self, input_list, first, last):
        pivotvalue = input_list[first]
        # Find the place to put pivotvalue such that sublist A has all values in input_list < pivotvalue and
        # sublist B has all values in input_list > pivotvalue
        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and \
                    input_list[leftmark] <= pivotvalue:
                leftmark += 1

            while input_list[rightmark] >= pivotvalue and \
                    rightmark >= leftmark:
                rightmark -= 1

            if rightmark < leftmark:
                done = True
            else:
                # Swap element in sublist A to B
                temp = input_list[leftmark]
                input_list[leftmark] = input_list[rightmark]
                input_list[rightmark] = temp

        temp = input_list[first]
        input_list[first] = input_list[rightmark]
        input_list[rightmark] = temp
        return rightmark


if __name__ == '__main__':
    generator = Generators()
    sorter = Sorters()

    rand_list = generator.randomNumber(list_length=10, num_range=100, num_type="int")
    sorter.insertionSort(rand_list)
    print "Insertion sorted list = " + str(rand_list)

    rand_list = generator.randomNumber(list_length=7, num_range=100, num_type="int")
    sorter.bubbleSort(rand_list)
    print "Bubble sorted list = " + str(rand_list)

    rand_list = generator.randomNumber(list_length=14, num_range=100, num_type="int")
    sorter.selectionSort(rand_list)
    print "Selection sorted list = " + str(rand_list)

    rand_list = generator.randomNumber(list_length=11, num_range=100, num_type="int")
    sorter.selectionSort(rand_list)
    print "Quick sorted list = " + str(rand_list)
