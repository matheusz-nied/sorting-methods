import util
import time

# InsertionSort


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


# SelectionSort
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

        while(j < number_lines):
            if(array[j][0] < array[menor][0]):
                menor = j
            j += 1

        if(menor != i):
            temp = array[i]
            array[i] = array[menor]
            array[menor] = temp

        i += 1

    fim = time.time()
    tempo_gasto = fim - ini
    return quantidade_comparacao, quantidade_troca, tempo_gasto


# MergeSort
def MergeSort(array):
    ini = time.time()
    quantidade_troca = 0
    quantidade_comparacao = 0
    tempo_gasto = 0
    
    
    
    
    

    def ordena_mergesort(A, aux, esquerda, direita):
        if direita <= esquerda:
            return
        meio = (esquerda + direita) // 2

        # Ordena a primeira metade do arranjo.
        ordena_mergesort(A, aux, esquerda, meio)

        # Ordena a segunda metade do arranjo.
        ordena_mergesort(A, aux, meio + 1, direita)

        # Combina as duas metades ordenadas anteriormente.
        merge(A, aux, esquerda, meio, direita)


    def merge(A, aux, esquerda, meio, direita):

        for k in range(esquerda, direita + 1):
            aux[k] = A[k]
        i = esquerda
        j = meio + 1
        for k in range(esquerda, direita + 1):
            if i > meio:
                A[k] = aux[j]
                j += 1
            elif j > direita:
                A[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                A[k] = aux[j]
                j += 1
            else:
                A[k] = aux[i]
                i += 1



    aux = [0] * len(array)
    ordena_mergesort(array, aux, 0 , len(array) - 1)
    
    fim = time.time()
    tempo_gasto = fim - ini
    return quantidade_comparacao, quantidade_troca, tempo_gasto
        

# QuickSort
def QuickSort(self):
    pass
