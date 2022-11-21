import util

def InsertionSort(array):
    number_lines = util.count_array(array)
    i = 0
    temp = []
    for data in array:
        
        
        j = i
        i += 1
        
        while(j > 0 and array[j][0] < array[j - 1][0]):
            temp = array[j]
            array[j] = array[j - 1]
            j = j - 1
            array[j] = temp




def SelectionSort(self):
    pass


def MergeSort(self):
    pass


def QuickSort(self):
    pass
