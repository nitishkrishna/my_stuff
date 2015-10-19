__author__ = 'nitish'
from Sorters import Sorters
import os
import sys
cur_dir = os.path.dirname(__file__)
sys_path_dir = os.path.join(cur_dir, '../../../')
sys.path.append(sys_path_dir)
from python.tools.Generators import Generators


class Searchers():
    def __init__(self):
        pass

    def binarySearch(self, input_list, item):  # O(logn)
        # Only for sorted arrays
        first = 0
        last = len(input_list)-1
        found = None

        while first <= last and not found:
            midpoint = (first + last)//2
            if input_list[midpoint] == item:
                found = midpoint
            else:
                if item < input_list[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return found


if __name__ == '__main__':
    generator = Generators()
    sorter = Sorters()
    input_list = generator.randomNumber(list_length=10, num_type="int", num_range=[0, 100])
    sorter.selectionSort(input_list)
    searcher = Searchers()
    search_number = generator.randomNumber("int", num_range=100)
    result1 = searcher.binarySearch(input_list, search_number)
    if result1 :
        print str(search_number) + " in list at index: " + str(result1)
    result2 = searcher.binarySearch(input_list, 55)
    if result2 :
        print "55 in list at index: " + str(result2)
    if result1 or result2:
        print "The random list was: " + str(input_list)
