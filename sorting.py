import util
import time

def InsertionSort(array):
    ini = time.time()
    quantidade_troca = 0;
    quantidade_comparacao = 0;
    tempo_gasto = 0;
    
    i = 0
    temp = []
    for data in array:
        
        
        j = i
        i += 1
        
        quantidade_comparacao+=1
        while(j > 0 and array[j][0] < array[j - 1][0]):
            temp = array[j]
            array[j] = array[j - 1]
            j = j - 1
            array[j] = temp
            quantidade_troca+=1
            
    fim = time.time()
    tempo_gasto = fim - ini
    
    return quantidade_comparacao,quantidade_troca, tempo_gasto

def SelectionSort(self):
    pass


def MergeSort(self):
    pass


def QuickSort(self):
    pass
