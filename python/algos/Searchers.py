__author__ = 'nitish'
from Sorters import Sorters


class Searchers():
    def __init__(self):
        pass

    def binarySearch(self, input_list, item): # O(logn)
        # Only for sorted arrays
        first = 0
        last = len(input_list)-1
        found = False

        while first<=last and not found:
            midpoint = (first + last)//2
            if input_list[midpoint] == item:
                found = True
            else:
                if item < input_list[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return found


if __name__ == '__main__':
    input_list = [54,26,93,17,77,31,44,55,20]
    sorter = Sorters()
    sorter.selectionSort(input_list)
    searcher = Searchers()
    print "24 in list: " + str(searcher.binarySearch(input_list, 24))
    print "55 in list: " + str(searcher.binarySearch(input_list, 55))