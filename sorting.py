import util
import time


def InsertionSort(array):
    ini = time.time()
    quantidade_troca = 0
    quantidade_comparacao = 0
    tempo_gasto = 0

    i = 0
    temp = []
    for data in array:

        j = i
        i += 1

        quantidade_comparacao += 1
        while(j > 0 and array[j][0] < array[j - 1][0]):
            temp = array[j]
            array[j] = array[j - 1]
            j = j - 1
            array[j] = temp
            quantidade_troca += 1

    fim = time.time()
    tempo_gasto = fim - ini

    return quantidade_comparacao, quantidade_troca, tempo_gasto


def SelectionSort(array):
    ini = time.time()
    quantidade_troca = 0
    quantidade_comparacao = 0
    tempo_gasto = 0

    number_lines = util.count_array(array)
    i = 0
    for data in array:
        menor = i
        j = i + 1
        
        while( j < number_lines):
            if(array[j][0] < array[menor][0]):
                menor = j
            j +=1;
        
        if(menor != i):
            temp = array[i]
            array[i] = array[menor]
            array[menor] = temp
        
        i += 1

    fim = time.time()
    tempo_gasto = fim - ini
    return quantidade_comparacao, quantidade_troca, tempo_gasto


def MergeSort(self):
    pass


def QuickSort(self):
    pass
